// Main JavaScript functionality for UNICORN BRAND

gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeAlerts();
    initializeCart();
    initializeProductFilters();
    initializeImageGallery();
    initializeForms();

    // Kiểm tra nếu đang ở trang chủ
    if (window.location.pathname === '/' || window.location.pathname === '/index' || window.location.pathname === '/index.html') {
        document.querySelectorAll('.split-animate').forEach(el => {
            const split = new SplitType(el, { types: 'chars' });
            gsap.from(split.chars, {
                scrollTrigger: {
                    trigger: el,
                    start: "top 80%",
                    toggleActions: "play none none none",
                    once: true
                },
                opacity: 0,
                y: 40,
                stagger: 0.05,
                duration: 0.6,
                ease: "power3.out"
            });
        });
    }

    // Realtime product update via SocketIO
    if (typeof io !== 'undefined') {
        var socket = io.connect(window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : ''));
        socket.on('product_update', function(data) {
            // Nếu đang ở trang sản phẩm, tự động reload
            if (window.location.pathname.startsWith('/products')) {
                location.reload();
            }
        });
    }

    syncCartToBackendIfNeeded();
    if (window.isAuthenticated) {
        updateCartCountFromBackend();
    }
});

// Alert system
function initializeAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Auto-hide alerts after 5 seconds
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
        
        // Add close button functionality
        const closeBtn = alert.querySelector('.alert-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                alert.style.opacity = '0';
                setTimeout(() => {
                    alert.remove();
                }, 300);
            });
        }
    });
}

// Cart functionality
function initializeCart() {
    if (window.isAuthenticated) {
        updateCartCountFromBackend();
    } else {
        updateCartCount();
    }
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const form = this.closest('form');
            const productId = form.querySelector('input[name="product_id"]').value;
            const quantity = parseInt(form.querySelector('.quantity-input')?.value || 1);
            const size = form.querySelector('select[name="size"]')?.value;
            const color = form.querySelector('select[name="color"]')?.value;
            
            addToCart(productId, quantity, size, color);
            // updateCartCount() is called inside addToCart based on authentication status
            showToast('Added to cart!', 'success');
        });
    });
    
    // Quantity controls
    const quantityControls = document.querySelectorAll('.quantity-control');
    quantityControls.forEach(control => {
        const minusBtn = control.querySelector('.quantity-minus');
        const plusBtn = control.querySelector('.quantity-plus');
        const input = control.querySelector('.quantity-input');
        
        if (minusBtn && plusBtn && input) {
            minusBtn.addEventListener('click', () => {
                const currentValue = parseInt(input.value);
                if (currentValue > 1) {
                    input.value = currentValue - 1;
                    input.dispatchEvent(new Event('change'));
                }
            });
            
            plusBtn.addEventListener('click', () => {
                const currentValue = parseInt(input.value);
                const maxValue = parseInt(input.getAttribute('max')) || 99;
                if (currentValue < maxValue) {
                    input.value = currentValue + 1;
                    input.dispatchEvent(new Event('change'));
                }
            });
        }
    });
}

// Thêm hàm lấy giỏ hàng từ backend (dùng cho trang view cart)
function getCartFromBackend(callback) {
    fetch('/api/cart')
        .then(res => res.json())
        .then(data => {
            if (data.cart) {
                callback(data.cart);
            } else {
                callback([]);
            }
        });
}

function addToCart(productId, quantity, size, color) {
    if (window.isAuthenticated) {
        fetch('/api/cart/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId, quantity, size, color })
        })
        .then(res => res.json())
        .then(data => {
            updateCartCountFromBackend();
            showToast('Added to cart!', 'success');
        });
    } else {
        let cart = JSON.parse(localStorage.getItem('cart')) || {};
        // Lưu thêm size, color nếu có
        const key = `${productId}_${size || ''}_${color || ''}`;
        if (cart[key]) {
            cart[key].quantity += quantity;
        } else {
            cart[key] = { quantity, size, color };
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
        showToast('Added to cart!', 'success');
    }
}

function getCartItemCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let count = 0;
    for (let key in cart) {
        count += cart[key];
    }
    return count;
}

// Product filters
function initializeProductFilters() {
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        const inputs = filterForm.querySelectorAll('input, select');
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                filterForm.submit();
            });
        });
    }
    
    // Price range slider
    const priceRange = document.getElementById('price-range');
    if (priceRange) {
        priceRange.addEventListener('input', function() {
            const value = this.value;
            const output = document.getElementById('price-output');
            if (output) {
                output.textContent = `$${value}`;
            }
        });
    }
}

// Image gallery for product details
function initializeImageGallery() {
    const thumbnails = document.querySelectorAll('.product-thumbnail');
    const mainImage = document.getElementById('main-product-image');
    
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            // Remove active class from all thumbnails
            thumbnails.forEach(t => t.classList.remove('active'));
            
            // Add active class to clicked thumbnail
            this.classList.add('active');
            
            // Update main image
            if (mainImage) {
                mainImage.src = this.src;
                mainImage.alt = this.alt;
            }
        });
    });
}

// Form enhancements
function initializeForms() {
    // Form validation
    const forms = document.querySelectorAll('form[data-validate]');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });
    
    // Password strength indicator
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(input => {
        if (input.name === 'password') {
            input.addEventListener('input', function() {
                updatePasswordStrength(this);
            });
        }
    });
    
    // Confirm password validation
    const confirmPasswordInputs = document.querySelectorAll('input[name="password2"]');
    confirmPasswordInputs.forEach(input => {
        input.addEventListener('input', function() {
            validatePasswordConfirmation(this);
        });
    });
}

// Form validation helper
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            showFieldError(field, 'This field is required');
            isValid = false;
        } else {
            clearFieldError(field);
        }
    });
    
    // Email validation
    const emailFields = form.querySelectorAll('input[type="email"]');
    emailFields.forEach(field => {
        if (field.value && !isValidEmail(field.value)) {
            showFieldError(field, 'Please enter a valid email address');
            isValid = false;
        }
    });
    
    return isValid;
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Password strength checker
function updatePasswordStrength(input) {
    const password = input.value;
    const strengthIndicator = document.getElementById('password-strength');
    
    if (!strengthIndicator) return;
    
    let strength = 0;
    let feedback = '';
    
    if (password.length >= 8) strength++;
    if (/[a-z]/.test(password)) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^A-Za-z0-9]/.test(password)) strength++;
    
    switch (strength) {
        case 0:
        case 1:
            feedback = 'Very Weak';
            strengthIndicator.className = 'password-strength weak';
            break;
        case 2:
            feedback = 'Weak';
            strengthIndicator.className = 'password-strength weak';
            break;
        case 3:
            feedback = 'Fair';
            strengthIndicator.className = 'password-strength fair';
            break;
        case 4:
            feedback = 'Good';
            strengthIndicator.className = 'password-strength good';
            break;
        case 5:
            feedback = 'Strong';
            strengthIndicator.className = 'password-strength strong';
            break;
    }
    
    strengthIndicator.textContent = feedback;
}

// Password confirmation validation
function validatePasswordConfirmation(input) {
    const password = document.querySelector('input[name="password"]');
    if (password && input.value !== password.value) {
        showFieldError(input, 'Passwords do not match');
    } else {
        clearFieldError(input);
    }
}

// Field error display
function showFieldError(field, message) {
    clearFieldError(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.color = '#ef4444';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    
    field.parentNode.appendChild(errorDiv);
    field.style.borderColor = '#ef4444';
}

// Clear field error
function clearFieldError(field) {
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
    field.style.borderColor = '';
}

// Update cart count in navbar
function updateCartCount() {
    const cartCount = getCartItemCount();
    const cartBadge = document.getElementById('cart-count');
    if (cartBadge) {
        cartBadge.textContent = cartCount;
        cartBadge.style.display = cartCount > 0 ? 'inline' : 'none';
    }
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Loading states for buttons
function showButtonLoading(button, loadingText = 'Loading...') {
    button.dataset.originalText = button.innerHTML;
    button.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${loadingText}`;
    button.disabled = true;
}

function hideButtonLoading(button) {
    if (button.dataset.originalText) {
        button.innerHTML = button.dataset.originalText;
        delete button.dataset.originalText;
    }
    button.disabled = false;
}

// Toast notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <div class="toast-content">
            <span>${message}</span>
            <button class="toast-close">&times;</button>
        </div>
    `;
    
    // Add styles
    toast.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    // Animate in
    setTimeout(() => {
        toast.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button
    const closeBtn = toast.querySelector('.toast-close');
    closeBtn.addEventListener('click', () => {
        removeToast(toast);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        removeToast(toast);
    }, 5000);
}

function removeToast(toast) {
    toast.style.transform = 'translateX(100%)';
    setTimeout(() => {
        if (toast.parentNode) {
            toast.parentNode.removeChild(toast);
        }
    }, 300);
}

// Đồng bộ cart localStorage lên backend khi đăng nhập
function syncCartToBackendIfNeeded() {
    if (window.isAuthenticated && localStorage.getItem('cart')) {
        const cart = JSON.parse(localStorage.getItem('cart'));
        // Chuyển về dạng {product_id: {quantity, size, color}}
        fetch('/api/cart/sync', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cart })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                localStorage.removeItem('cart');
                updateCartCountFromBackend();
            }
        });
    }
}

function updateCartCountFromBackend() {
    fetch('/api/cart/count')
        .then(res => res.json())
        .then(data => {
            const cartBadge = document.getElementById('cart-count');
            if (cartBadge) {
                cartBadge.textContent = data.cart_count;
                cartBadge.style.display = data.cart_count > 0 ? 'inline' : 'none';
            }
        });
}

// Render cart items từ backend (dùng cho trang view cart)
function renderCartItems(cartItems) {
    const cartContainer = document.getElementById('cart-items-container');
    const orderSummary = document.getElementById('order-summary');
    if (!cartContainer || !orderSummary) return;

    cartContainer.innerHTML = '';
    let total = 0;
    cartItems.forEach((item, idx) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'cart-item';
        itemDiv.innerHTML = `
            <img src="${item.image_url || '/static/images/placeholder-shoe.jpg'}" alt="${item.name}">
            <div class="cart-item-info">
                <h3 class="cart-item-title">${item.name}</h3>
                <div class="cart-item-details">
                    ${item.size ? `Size: ${item.size}` : ''} 
                    ${item.color ? ` | Color: ${item.color}` : ''}
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <input type="number" min="1" max="99" value="${item.quantity}" class="form-control cart-qty-input" data-product-id="${item.product_id}" data-size="${item.size || ''}" data-color="${item.color || ''}" style="width: 80px;">
                <div class="cart-item-price">$${(item.price * item.quantity).toFixed(2)}</div>
                <button class="btn-outline cart-remove-btn" data-product-id="${item.product_id}" data-size="${item.size || ''}" data-color="${item.color || ''}" style="color: #ef4444; border-color: #ef4444; padding: 0.5rem;">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;
        cartContainer.appendChild(itemDiv);
        total += item.price * item.quantity;
    });

    // Cập nhật order summary
    orderSummary.innerHTML = `
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <span>Subtotal (${cartItems.length} items)</span>
            <span>$${total.toFixed(2)}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <span>Shipping</span>
            <span>${total >= 100 ? 'Free' : '$9.99'}</span>
        </div>
        <hr style="margin: 1rem 0;">
        <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1.125rem; margin-bottom: 1.5rem;">
            <span>Total</span>
            <span>$${(total + (total >= 100 ? 0 : 9.99)).toFixed(2)}</span>
        </div>
        <a href="/cart/checkout" class="btn-primary" style="width: 100%; text-align: center; text-decoration: none; margin-bottom: 1rem;">
            Proceed to Checkout
        </a>
        <a href="/products" class="btn-outline" style="width: 100%; text-align: center; text-decoration: none;">
            Continue Shopping
        </a>
    `;

    // Gắn sự kiện cập nhật số lượng
    document.querySelectorAll('.cart-qty-input').forEach(input => {
        input.addEventListener('change', function() {
            const productId = this.dataset.productId;
            const size = this.dataset.size;
            const color = this.dataset.color;
            const quantity = parseInt(this.value);
            updateCartItem(productId, quantity, size, color);
        });
    });

    // Gắn sự kiện xóa sản phẩm
    document.querySelectorAll('.cart-remove-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const size = this.dataset.size;
            const color = this.dataset.color;
            removeCartItem(productId, size, color);
        });
    });
}

// Cập nhật số lượng sản phẩm
function updateCartItem(productId, quantity, size, color) {
    fetch('/api/cart/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: productId, quantity, size, color })
    })
    .then(res => res.json())
    .then(data => {
        getCartFromBackend(renderCartItems);
        updateCartCountFromBackend();
        showToast('Cart updated!', 'success');
    });
}

// Xóa sản phẩm khỏi giỏ
function removeCartItem(productId, size, color) {
    fetch('/api/cart/remove', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: productId, size, color })
    })
    .then(res => res.json())
    .then(data => {
        getCartFromBackend(renderCartItems);
        updateCartCountFromBackend();
        showToast('Item removed from cart!', 'info');
    });
}