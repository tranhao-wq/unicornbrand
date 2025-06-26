import qrcode

# Thông tin chuyển khoản BIDV
account_number = '123456789'  # Thay bằng số tài khoản thật
account_name = 'NGUYEN VAN A'  # Thay bằng tên chủ tài khoản thật
bank_name = 'BIDV'
amount = ''  # Có thể để trống hoặc nhập số tiền cố định
content = 'Thanh toan don hang UnicornBrand'

# Dữ liệu QR theo chuẩn VietQR (nếu muốn chuẩn hóa, có thể dùng thêm thư viện vietqr, ở đây dùng text đơn giản)
data = f'BIDV|{account_number}|{account_name}|{amount}|{content}'

# Tạo mã QR
img = qrcode.make(data)
img.save('static/assets/images/bidv_qr.png')

print('Đã tạo mã QR BIDV tại static/assets/images/bidv_qr.png') 