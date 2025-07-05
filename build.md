Kết nối database (Supabase) bị lỗi
Lỗi SSL hoặc pool connection (như đã phân tích ở trên).
Database Supabase có thể đang sleep hoặc bị ngắt kết nối.
Cấu hình pool SQLAlchemy chưa tối ưu, giữ kết nối cũ đã hết hạn.
Worker Gunicorn bị timeout hoặc kill
Do quá tải, thiếu RAM, hoặc request truy vấn DB bị treo.
Lỗi code backend khi truy vấn DB
Khi không kết nối được DB, mọi truy vấn (kể cả lấy user admin) đều lỗi 500.
Cách kiểm tra & khắc phục
1. Kiểm tra log chi tiết
Xem log server trên Render hoặc local để xác định lỗi 500 là do đâu (thường sẽ thấy dòng OperationalError: SSL error: decryption failed or bad record mac).
2. Kiểm tra trạng thái Supabase
Đăng nhập Supabase, kiểm tra database có đang sleep không.
Nếu sleep, hãy "wake up" bằng cách truy cập Supabase hoặc chạy một truy vấn nhỏ.
3. Kiểm tra lại cấu hình DATABASE_URL
Đảm bảo có sslmode=require ở cuối URL.
Ví dụ:
Apply to continue.con...
4. Tối ưu pool SQLAlchemy
Đảm bảo đã cấu hình pool như sau (trong config.py hoặc nơi khởi tạo SQLAlchemy):
Apply to continue.con...
Nếu dùng Flask-SQLAlchemy:
Apply to continue.con...
5. Restart lại service trên Render
Đôi khi worker bị treo hoặc pool bị "dính" kết nối cũ, cần restart lại service để reset pool.
Checklist khắc phục nhanh
[ ] Đảm bảo Supabase đang hoạt động, không sleep.
[ ] Đảm bảo DATABASE_URL có sslmode=require.
[ ] Đảm bảo pool SQLAlchemy đã tối ưu.
[ ] Restart lại service trên Render.
[ ] Kiểm tra lại log nếu vẫn lỗi.
Nếu vẫn lỗi, bạn hãy:
Gửi file config.py hoặc nơi khởi tạo SQLAlchemy để mình kiểm tra cấu hình.
Gửi log chi tiết lỗi 500 (stacktrace) để mình phân tích sâu hơn.

2025-07-05T12:16:46.895058433Z Using cached PyJWT-2.10.1-py3-none-any.whl (22 kB)
2025-07-05T12:16:46.896407314Z Using cached realtime-2.5.3-py3-none-any.whl (21 kB)
2025-07-05T12:16:46.897649063Z Using cached storage3-0.12.0-py3-none-any.whl (18 kB)
2025-07-05T12:16:46.898872811Z Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2025-07-05T12:16:46.900217882Z Using cached supafunc-0.10.1-py3-none-any.whl (8.0 kB)
2025-07-05T12:16:46.90227715Z Using cached StrEnum-0.4.15-py3-none-any.whl (8.9 kB)
2025-07-05T12:16:46.903470108Z Using cached websockets-15.0.1-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-07-05T12:16:46.904778038Z Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-07-05T12:16:46.906143579Z Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-07-05T12:16:46.907357478Z Using cached typing_inspection-0.4.1-py3-none-any.whl (14 kB)
2025-07-05T12:16:46.908576586Z Using cached anyio-4.9.0-py3-none-any.whl (100 kB)
2025-07-05T12:16:46.909800214Z Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
2025-07-05T12:16:46.91091198Z Using cached certifi-2025.6.15-py3-none-any.whl (157 kB)
2025-07-05T12:16:47.060693835Z Installing collected packages: strenum, websockets, typing_extensions, sniffio, six, qrcode, PyMySQL, pyjwt, psycopg2-binary, pip-upgrade, pillow, packaging, MarkupSafe, itsdangerous, idna, hyperframe, hpack, h11, greenlet, dnspython, colorama, click, certifi, blinker, bidict, annotated-types, WTForms, wsproto, Werkzeug, typing-inspection, SQLAlchemy, realtime, python-dateutil, pydantic-core, Mako, Jinja2, httpcore, h2, gunicorn, email_validator, deprecation, anyio, simple-websocket, pydantic, httpx, Flask, alembic, python-engineio, Flask-WTF, Flask-SQLAlchemy, Flask-Login, supafunc, storage3, python-socketio, postgrest, gotrue, Flask-Migrate, supabase, Flask-SocketIO
2025-07-05T12:16:50.847187537Z 
2025-07-05T12:16:50.855407058Z Successfully installed Flask-3.1.1 Flask-Login-0.6.3 Flask-Migrate-4.1.0 Flask-SQLAlchemy-3.1.1 Flask-SocketIO-5.5.1 Flask-WTF-1.2.2 Jinja2-3.1.6 Mako-1.3.10 MarkupSafe-3.0.2 PyMySQL-1.1.1 SQLAlchemy-2.0.41 WTForms-3.2.1 Werkzeug-3.1.3 alembic-1.16.2 annotated-types-0.7.0 anyio-4.9.0 bidict-0.23.1 blinker-1.9.0 certifi-2025.6.15 click-8.2.1 colorama-0.4.6 deprecation-2.1.0 dnspython-2.7.0 email_validator-2.2.0 gotrue-2.12.3 greenlet-3.2.3 gunicorn-23.0.0 h11-0.16.0 h2-4.2.0 hpack-4.1.0 httpcore-1.0.9 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 itsdangerous-2.2.0 packaging-25.0 pillow-11.2.1 pip-upgrade-0.0.6 postgrest-1.1.1 psycopg2-binary-2.9.10 pydantic-2.11.7 pydantic-core-2.33.2 pyjwt-2.10.1 python-dateutil-2.9.0.post0 python-engineio-4.12.2 python-socketio-5.13.0 qrcode-8.2 realtime-2.5.3 simple-websocket-1.1.0 six-1.17.0 sniffio-1.3.1 storage3-0.12.0 strenum-0.4.15 supabase-2.16.0 supafunc-0.10.1 typing-inspection-0.4.1 typing_extensions-4.14.0 websockets-15.0.1 wsproto-1.2.0
2025-07-05T12:16:53.065476428Z ==> Uploading build...
2025-07-05T12:17:01.878678986Z ==> Uploaded in 7.2s. Compression took 1.6s
2025-07-05T12:17:01.92512555Z ==> Build successful 🎉
2025-07-05T12:17:07.374576831Z ==> Deploying...
2025-07-05T12:17:29.093510283Z ==> Running '   gunicorn wsgi:app'
2025-07-05T12:17:39.842793691Z [2025-07-05 12:17:39 +0000] [105] [INFO] Starting gunicorn 23.0.0
2025-07-05T12:17:39.843247241Z [2025-07-05 12:17:39 +0000] [105] [INFO] Listening at: http://0.0.0.0:10000 (105)
2025-07-05T12:17:39.843286362Z [2025-07-05 12:17:39 +0000] [105] [INFO] Using worker: sync
2025-07-05T12:17:39.847750983Z [2025-07-05 12:17:39 +0000] [106] [INFO] Booting worker with pid: 106
2025-07-05T12:17:45.222706784Z 127.0.0.1 - - [05/Jul/2025:12:17:45 +0000] "HEAD / HTTP/1.1" 200 0 "-" "Go-http-client/1.1"
2025-07-05T12:17:48.205068046Z ==> Your service is live 🎉
2025-07-05T12:17:48.376665964Z ==> 
2025-07-05T12:17:48.548158463Z ==> ///////////////////////////////////////////////////////////
2025-07-05T12:17:48.719686902Z ==> 
2025-07-05T12:17:48.889731481Z ==> Available at your primary URL https://unicornbrand.onrender.com
2025-07-05T12:17:49.059441169Z ==> 
2025-07-05T12:17:49.230441989Z ==> ///////////////////////////////////////////////////////////
2025-07-05T12:17:52.047108138Z 127.0.0.1 - - [05/Jul/2025:12:17:52 +0000] "GET / HTTP/1.1" 200 25144 "-" "Go-http-client/2.0"
2025-07-05T12:18:22.034005376Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET / HTTP/1.1" 200 27439 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.232883315Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/images/placeholder-shoe.jpg HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.238183304Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/js/libs/gsap.min.js HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.239285889Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/js/libs/ScrollTrigger.min.js HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.28860151Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/js/libs/SplitType.min.js HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.296090408Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/css/style.css HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.307788952Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.314458462Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/js/main.js HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.453396641Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/assets/images/garniture2.jpg HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/static/css/style.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.456781947Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /static/assets/images/garniture.jpg HTTP/1.1" 200 0 "https://unicornbrand.onrender.com/static/css/style.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.712355833Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /api/cart/count HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.724740022Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "POST /api/cart/sync HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:22.726386779Z 127.0.0.1 - - [05/Jul/2025:12:18:22 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXVZq HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:23.024692607Z 127.0.0.1 - - [05/Jul/2025:12:18:23 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQXVem&sid=hQihr958tSBrvZwVAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:23.034719643Z 127.0.0.1 - - [05/Jul/2025:12:18:23 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXVeq&sid=hQihr958tSBrvZwVAAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:23.112615588Z 127.0.0.1 - - [05/Jul/2025:12:18:23 +0000] "GET /static/assets/musics/Ordinary%20Girl%20-%20Ahv.mp3 HTTP/1.1" 206 9899674 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:53.952740468Z [2025-07-05 12:18:53 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:106)
2025-07-05T12:18:53.958321394Z [2025-07-05 12:18:53 +0000] [106] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=hQihr958tSBrvZwVAAAA
2025-07-05T12:18:53.958335214Z Traceback (most recent call last):
2025-07-05T12:18:53.958340094Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:18:53.958345385Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:18:53.958349565Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958353965Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:18:53.958358605Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:18:53.958363945Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:18:53.958368605Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:18:53.958372875Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958377495Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:18:53.958381725Z     return super().__call__(environ, start_response)
2025-07-05T12:18:53.958385935Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958393746Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:18:53.958398646Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:18:53.958403526Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958408116Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:18:53.958412666Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:18:53.958417116Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958421396Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:18:53.958426136Z     packets = socket.handle_get_request(
2025-07-05T12:18:53.958431596Z         environ, start_response)
2025-07-05T12:18:53.958436337Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:18:53.958454777Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:18:53.958457727Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:18:53.958460587Z                                                   start_response)
2025-07-05T12:18:53.958463267Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958465837Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:18:53.958468587Z     return ws(environ, start_response)
2025-07-05T12:18:53.958473877Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:18:53.958476408Z     ret = self.app(self)
2025-07-05T12:18:53.958478168Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:18:53.958481538Z     pkt = websocket_wait()
2025-07-05T12:18:53.958484638Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:18:53.958487278Z     data = ws.wait()
2025-07-05T12:18:53.958490348Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:18:53.958493108Z     return self.ws.receive()
2025-07-05T12:18:53.958496118Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:18:53.958498858Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:18:53.958501468Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:18:53.958503838Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:18:53.958506158Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:18:53.958508468Z     signaled = self._cond.wait(timeout)
2025-07-05T12:18:53.958510948Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:18:53.958513478Z     waiter.acquire()
2025-07-05T12:18:53.958516138Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:18:53.958518918Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:18:53.958521389Z     sys.exit(1)
2025-07-05T12:18:53.958523149Z     ~~~~~~~~^^^
2025-07-05T12:18:53.958524869Z SystemExit: 1
2025-07-05T12:18:53.958534839Z 127.0.0.1 - - [05/Jul/2025:12:18:53 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=hQihr958tSBrvZwVAAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:18:53.958748844Z [2025-07-05 12:18:53 +0000] [106] [INFO] Worker exiting (pid: 106)
2025-07-05T12:18:55.018254745Z [2025-07-05 12:18:55 +0000] [105] [ERROR] Worker (pid:106) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:18:55.032930265Z [2025-07-05 12:18:55 +0000] [110] [INFO] Booting worker with pid: 110
2025-07-05T12:18:55.111510095Z Invalid session hQihr958tSBrvZwVAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:18:55.111527785Z ERROR:engineio.server:Invalid session hQihr958tSBrvZwVAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:18:55.112287482Z 127.0.0.1 - - [05/Jul/2025:12:18:55 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXVnd&sid=hQihr958tSBrvZwVAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:55.419505181Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:18:55.419521952Z Traceback (most recent call last):
2025-07-05T12:18:55.419536332Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:55.419540052Z     self.dialect.do_execute(
2025-07-05T12:18:55.419543092Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419546732Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:55.419549562Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419552272Z     )
2025-07-05T12:18:55.419554873Z     ^
2025-07-05T12:18:55.419557673Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:55.419560393Z     cursor.execute(statement, parameters)
2025-07-05T12:18:55.419562922Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419566093Z psycopg2.OperationalError: SSL error: decryption failed or bad record mac
2025-07-05T12:18:55.419568233Z 
2025-07-05T12:18:55.419570373Z 
2025-07-05T12:18:55.419572893Z The above exception was the direct cause of the following exception:
2025-07-05T12:18:55.419575263Z 
2025-07-05T12:18:55.419577553Z Traceback (most recent call last):
2025-07-05T12:18:55.419580423Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:18:55.419583433Z     response = self.full_dispatch_request()
2025-07-05T12:18:55.419586043Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:18:55.419588673Z     rv = self.handle_user_exception(e)
2025-07-05T12:18:55.419591683Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:18:55.419594553Z     rv = self.dispatch_request()
2025-07-05T12:18:55.419597463Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:18:55.419599803Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:18:55.419602403Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:18:55.419605194Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:18:55.419607764Z     elif not current_user.is_authenticated:
2025-07-05T12:18:55.419610434Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419612834Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:18:55.419615774Z     obj = instance._get_current_object()
2025-07-05T12:18:55.419618194Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:18:55.419620854Z     return get_name(local())
2025-07-05T12:18:55.419623714Z                     ~~~~~^^
2025-07-05T12:18:55.419629014Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:18:55.419631794Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:18:55.419634354Z                                       ~~~~~~~~~^^
2025-07-05T12:18:55.419637024Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:18:55.419639594Z     current_app.login_manager._load_user()
2025-07-05T12:18:55.419642204Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:18:55.419644744Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:18:55.419652465Z     user = self._user_callback(user_id)
2025-07-05T12:18:55.419655185Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:18:55.419657755Z     return User.query.get(int(user_id))
2025-07-05T12:18:55.419660515Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:18:55.419663515Z   File "<string>", line 2, in get
2025-07-05T12:18:55.419666205Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:18:55.419668545Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:18:55.419670855Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:18:55.419673125Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:18:55.419675385Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419677715Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:18:55.419679955Z     return self.session._get_impl(
2025-07-05T12:18:55.419682205Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419684795Z         mapper,
2025-07-05T12:18:55.419687315Z         ^^^^^^^
2025-07-05T12:18:55.419690556Z     ...<6 lines>...
2025-07-05T12:18:55.419693216Z         execution_options=self._execution_options,
2025-07-05T12:18:55.419695705Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419698196Z     )
2025-07-05T12:18:55.419700626Z     ^
2025-07-05T12:18:55.419703386Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:18:55.419706006Z     return db_load_fn(
2025-07-05T12:18:55.419708596Z         self,
2025-07-05T12:18:55.419711136Z     ...<5 lines>...
2025-07-05T12:18:55.419713816Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.419716356Z     )
2025-07-05T12:18:55.419719186Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:18:55.419721836Z     session.execute(
2025-07-05T12:18:55.419724096Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419726206Z         q,
2025-07-05T12:18:55.419728346Z         ^^
2025-07-05T12:18:55.419730386Z     ...<2 lines>...
2025-07-05T12:18:55.419732436Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.419741407Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419744117Z     )
2025-07-05T12:18:55.419746257Z     ^
2025-07-05T12:18:55.419748477Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:18:55.419750597Z     return self._execute_internal(
2025-07-05T12:18:55.419752717Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419754727Z         statement,
2025-07-05T12:18:55.419756817Z         ^^^^^^^^^^
2025-07-05T12:18:55.419758787Z     ...<4 lines>...
2025-07-05T12:18:55.419760977Z         _add_event=_add_event,
2025-07-05T12:18:55.419762967Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419765037Z     )
2025-07-05T12:18:55.419767047Z     ^
2025-07-05T12:18:55.419771087Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:18:55.419773707Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:18:55.419776137Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419785718Z         self,
2025-07-05T12:18:55.419788228Z         ^^^^^
2025-07-05T12:18:55.419790498Z     ...<4 lines>...
2025-07-05T12:18:55.419792608Z         conn,
2025-07-05T12:18:55.419794708Z         ^^^^^
2025-07-05T12:18:55.419796718Z     )
2025-07-05T12:18:55.419827879Z     ^
2025-07-05T12:18:55.419835689Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:18:55.419838489Z     result = conn.execute(
2025-07-05T12:18:55.419841169Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:18:55.419843609Z     )
2025-07-05T12:18:55.419845849Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:18:55.419847989Z     return meth(
2025-07-05T12:18:55.419850179Z         self,
2025-07-05T12:18:55.419852329Z         distilled_parameters,
2025-07-05T12:18:55.419854559Z         execution_options or NO_OPTIONS,
2025-07-05T12:18:55.419856669Z     )
2025-07-05T12:18:55.419859059Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:18:55.419861569Z     return connection._execute_clauseelement(
2025-07-05T12:18:55.419864009Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.41986672Z         self, distilled_params, execution_options
2025-07-05T12:18:55.419869089Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.4198715Z     )
2025-07-05T12:18:55.4198742Z     ^
2025-07-05T12:18:55.41987646Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:18:55.41987875Z     ret = self._execute_context(
2025-07-05T12:18:55.41988097Z         dialect,
2025-07-05T12:18:55.41988313Z     ...<8 lines>...
2025-07-05T12:18:55.41988527Z         cache_hit=cache_hit,
2025-07-05T12:18:55.41988739Z     )
2025-07-05T12:18:55.41988962Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:18:55.41989178Z     return self._exec_single_context(
2025-07-05T12:18:55.41989381Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.41989606Z         dialect, context, statement, parameters
2025-07-05T12:18:55.41989843Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.41990053Z     )
2025-07-05T12:18:55.41990266Z     ^
2025-07-05T12:18:55.41990502Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:18:55.41990742Z     self._handle_dbapi_exception(
2025-07-05T12:18:55.4199095Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419911661Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:18:55.419913801Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.41991591Z     )
2025-07-05T12:18:55.41991795Z     ^
2025-07-05T12:18:55.419920041Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:18:55.419922271Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:18:55.419924451Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:55.419926761Z     self.dialect.do_execute(
2025-07-05T12:18:55.419928881Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.419935801Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:55.419938281Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419940521Z     )
2025-07-05T12:18:55.419942701Z     ^
2025-07-05T12:18:55.419944941Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:55.419947191Z     cursor.execute(statement, parameters)
2025-07-05T12:18:55.419949461Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.419952051Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL error: decryption failed or bad record mac
2025-07-05T12:18:55.419954081Z 
2025-07-05T12:18:55.419958151Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:18:55.419961222Z FROM users 
2025-07-05T12:18:55.419963462Z WHERE users.id = %(pk_1)s]
2025-07-05T12:18:55.419965692Z [parameters: {'pk_1': 1}]
2025-07-05T12:18:55.419967932Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:18:55.608069088Z [2025-07-05 12:18:55 +0000] [110] [ERROR] Error handling request /cart/view
2025-07-05T12:18:55.608086108Z Traceback (most recent call last):
2025-07-05T12:18:55.608089758Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:55.608093088Z     self.dialect.do_execute(
2025-07-05T12:18:55.608095488Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608098799Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:55.608101399Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608103719Z     )
2025-07-05T12:18:55.608106359Z     ^
2025-07-05T12:18:55.608109319Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:55.608112009Z     cursor.execute(statement, parameters)
2025-07-05T12:18:55.608114479Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608116849Z psycopg2.OperationalError: SSL error: decryption failed or bad record mac
2025-07-05T12:18:55.608119059Z 
2025-07-05T12:18:55.608121809Z 
2025-07-05T12:18:55.608124959Z The above exception was the direct cause of the following exception:
2025-07-05T12:18:55.608127169Z 
2025-07-05T12:18:55.608129609Z Traceback (most recent call last):
2025-07-05T12:18:55.608132639Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:18:55.6081351Z     response = self.full_dispatch_request()
2025-07-05T12:18:55.6081378Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:18:55.60814046Z     rv = self.handle_user_exception(e)
2025-07-05T12:18:55.60814319Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:18:55.60814584Z     rv = self.dispatch_request()
2025-07-05T12:18:55.60814848Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:18:55.608151Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:18:55.60815358Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:18:55.60816533Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:18:55.60816833Z     elif not current_user.is_authenticated:
2025-07-05T12:18:55.60817086Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.60817325Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:18:55.60817575Z     obj = instance._get_current_object()
2025-07-05T12:18:55.60817796Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:18:55.608180521Z     return get_name(local())
2025-07-05T12:18:55.608183521Z                     ~~~~~^^
2025-07-05T12:18:55.60818593Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:18:55.608188411Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:18:55.608190711Z                                       ~~~~~~~~~^^
2025-07-05T12:18:55.608193081Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:18:55.608195471Z     current_app.login_manager._load_user()
2025-07-05T12:18:55.608197771Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:18:55.608200271Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:18:55.608202791Z     user = self._user_callback(user_id)
2025-07-05T12:18:55.608205151Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:18:55.608207481Z     return User.query.get(int(user_id))
2025-07-05T12:18:55.608209801Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:18:55.608212281Z   File "<string>", line 2, in get
2025-07-05T12:18:55.608214671Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:18:55.608216921Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:18:55.608219581Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:18:55.608222271Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:18:55.608224751Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608227271Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:18:55.608229602Z     return self.session._get_impl(
2025-07-05T12:18:55.608231832Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608234302Z         mapper,
2025-07-05T12:18:55.608236612Z         ^^^^^^^
2025-07-05T12:18:55.608239462Z     ...<6 lines>...
2025-07-05T12:18:55.608241902Z         execution_options=self._execution_options,
2025-07-05T12:18:55.608244452Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608247052Z     )
2025-07-05T12:18:55.608249532Z     ^
2025-07-05T12:18:55.608252192Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:18:55.608254752Z     return db_load_fn(
2025-07-05T12:18:55.608257222Z         self,
2025-07-05T12:18:55.608259772Z     ...<5 lines>...
2025-07-05T12:18:55.608262472Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.608264922Z     )
2025-07-05T12:18:55.608267883Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:18:55.608276343Z     session.execute(
2025-07-05T12:18:55.608279353Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608282083Z         q,
2025-07-05T12:18:55.608284763Z         ^^
2025-07-05T12:18:55.608287223Z     ...<2 lines>...
2025-07-05T12:18:55.608301403Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.608304663Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608307243Z     )
2025-07-05T12:18:55.608309933Z     ^
2025-07-05T12:18:55.608312324Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:18:55.608314993Z     return self._execute_internal(
2025-07-05T12:18:55.608317424Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608319804Z         statement,
2025-07-05T12:18:55.608322474Z         ^^^^^^^^^^
2025-07-05T12:18:55.608324734Z     ...<4 lines>...
2025-07-05T12:18:55.608327164Z         _add_event=_add_event,
2025-07-05T12:18:55.608329794Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608332104Z     )
2025-07-05T12:18:55.608334594Z     ^
2025-07-05T12:18:55.608337224Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:18:55.608340364Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:18:55.608343104Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608345804Z         self,
2025-07-05T12:18:55.608348414Z         ^^^^^
2025-07-05T12:18:55.608351124Z     ...<4 lines>...
2025-07-05T12:18:55.608354024Z         conn,
2025-07-05T12:18:55.608356534Z         ^^^^^
2025-07-05T12:18:55.608358965Z     )
2025-07-05T12:18:55.608361625Z     ^
2025-07-05T12:18:55.608367465Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:18:55.608370185Z     result = conn.execute(
2025-07-05T12:18:55.608372805Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:18:55.608375335Z     )
2025-07-05T12:18:55.608377825Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:18:55.608379635Z 127.0.0.1 - - [05/Jul/2025:12:18:55 +0000] "GET /cart/view HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:18:55.608380295Z     return meth(
2025-07-05T12:18:55.608383805Z         self,
2025-07-05T12:18:55.608386425Z         distilled_parameters,
2025-07-05T12:18:55.608389135Z         execution_options or NO_OPTIONS,
2025-07-05T12:18:55.608391835Z     )
2025-07-05T12:18:55.608394535Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:18:55.608403746Z     return connection._execute_clauseelement(
2025-07-05T12:18:55.608406295Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608409376Z         self, distilled_params, execution_options
2025-07-05T12:18:55.608411566Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608413676Z     )
2025-07-05T12:18:55.608416256Z     ^
2025-07-05T12:18:55.608419496Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:18:55.608436816Z     ret = self._execute_context(
2025-07-05T12:18:55.608440146Z         dialect,
2025-07-05T12:18:55.608443536Z     ...<8 lines>...
2025-07-05T12:18:55.608446527Z         cache_hit=cache_hit,
2025-07-05T12:18:55.608449276Z     )
2025-07-05T12:18:55.608463187Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:18:55.608465197Z     return self._exec_single_context(
2025-07-05T12:18:55.608467357Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608469067Z         dialect, context, statement, parameters
2025-07-05T12:18:55.608470697Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608472417Z     )
2025-07-05T12:18:55.608474117Z     ^
2025-07-05T12:18:55.608475877Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:18:55.608477527Z     self._handle_dbapi_exception(
2025-07-05T12:18:55.608479167Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608480847Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:18:55.608482487Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608484127Z     )
2025-07-05T12:18:55.608485747Z     ^
2025-07-05T12:18:55.608487437Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:18:55.608489617Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:18:55.608491288Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:55.608493017Z     self.dialect.do_execute(
2025-07-05T12:18:55.608494688Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608496377Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:55.608498038Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608499668Z     )
2025-07-05T12:18:55.608501328Z     ^
2025-07-05T12:18:55.608503038Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:55.608504688Z     cursor.execute(statement, parameters)
2025-07-05T12:18:55.608506318Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608508468Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL error: decryption failed or bad record mac
2025-07-05T12:18:55.608510058Z 
2025-07-05T12:18:55.608513748Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:18:55.608516378Z FROM users 
2025-07-05T12:18:55.608519378Z WHERE users.id = %(pk_1)s]
2025-07-05T12:18:55.608522338Z [parameters: {'pk_1': 1}]
2025-07-05T12:18:55.608525288Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:18:55.608527688Z 
2025-07-05T12:18:55.608530218Z During handling of the above exception, another exception occurred:
2025-07-05T12:18:55.608532869Z 
2025-07-05T12:18:55.608535518Z Traceback (most recent call last):
2025-07-05T12:18:55.608538098Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:18:55.608540558Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:18:55.608546209Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608548909Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:18:55.608556599Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:18:55.608559449Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:18:55.608562119Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:18:55.608567059Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608569689Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:18:55.608572089Z     return super().__call__(environ, start_response)
2025-07-05T12:18:55.608574729Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.60857721Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 74, in __call__
2025-07-05T12:18:55.60857981Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:18:55.608582139Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608584639Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1514, in wsgi_app
2025-07-05T12:18:55.60858751Z     response = self.handle_exception(e)
2025-07-05T12:18:55.60859012Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 860, in handle_exception
2025-07-05T12:18:55.60859245Z     server_error = self.ensure_sync(handler)(server_error)
2025-07-05T12:18:55.60859713Z   File "/opt/render/project/src/app.py", line 65, in internal_server_error
2025-07-05T12:18:55.60859972Z     return render_template('500.html'), 500
2025-07-05T12:18:55.60860197Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-07-05T12:18:55.60860472Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 150, in render_template
2025-07-05T12:18:55.60860752Z     return _render(app, template, context)
2025-07-05T12:18:55.60861018Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 127, in _render
2025-07-05T12:18:55.60861286Z     app.update_template_context(context)
2025-07-05T12:18:55.60861552Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:18:55.60862093Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 530, in update_template_context
2025-07-05T12:18:55.608623391Z     context.update(self.ensure_sync(func)())
2025-07-05T12:18:55.608625911Z                    ~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:18:55.608628191Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 405, in _user_context_processor
2025-07-05T12:18:55.608630541Z     return dict(current_user=_get_user())
2025-07-05T12:18:55.608633471Z                              ~~~~~~~~~^^
2025-07-05T12:18:55.608636501Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:18:55.608639061Z     current_app.login_manager._load_user()
2025-07-05T12:18:55.608641641Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:18:55.608643901Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:18:55.608646151Z     user = self._user_callback(user_id)
2025-07-05T12:18:55.608648581Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:18:55.608650961Z     return User.query.get(int(user_id))
2025-07-05T12:18:55.608653241Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:18:55.608655621Z   File "<string>", line 2, in get
2025-07-05T12:18:55.608657941Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:18:55.608665752Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:18:55.608668261Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:18:55.608670521Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:18:55.608672921Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608675402Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:18:55.608678082Z     return self.session._get_impl(
2025-07-05T12:18:55.608680442Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608682672Z         mapper,
2025-07-05T12:18:55.608685022Z         ^^^^^^^
2025-07-05T12:18:55.608687662Z     ...<6 lines>...
2025-07-05T12:18:55.608690342Z         execution_options=self._execution_options,
2025-07-05T12:18:55.608692952Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608695652Z     )
2025-07-05T12:18:55.608698212Z     ^
2025-07-05T12:18:55.608700692Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:18:55.608703312Z     return db_load_fn(
2025-07-05T12:18:55.608705762Z         self,
2025-07-05T12:18:55.608708252Z     ...<5 lines>...
2025-07-05T12:18:55.608711033Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.608713742Z     )
2025-07-05T12:18:55.608716193Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:18:55.608718923Z     session.execute(
2025-07-05T12:18:55.608721393Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608723893Z         q,
2025-07-05T12:18:55.608726473Z         ^^
2025-07-05T12:18:55.608728843Z     ...<2 lines>...
2025-07-05T12:18:55.608731273Z         bind_arguments=bind_arguments,
2025-07-05T12:18:55.608733813Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608736393Z     )
2025-07-05T12:18:55.608738793Z     ^
2025-07-05T12:18:55.608741163Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:18:55.608758034Z     return self._execute_internal(
2025-07-05T12:18:55.608761274Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608763584Z         statement,
2025-07-05T12:18:55.608766004Z         ^^^^^^^^^^
2025-07-05T12:18:55.608771114Z     ...<4 lines>...
2025-07-05T12:18:55.608774114Z         _add_event=_add_event,
2025-07-05T12:18:55.608776694Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608778484Z     )
2025-07-05T12:18:55.608780094Z     ^
2025-07-05T12:18:55.608781804Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:18:55.608783524Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:18:55.608785294Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608786944Z         self,
2025-07-05T12:18:55.608788604Z         ^^^^^
2025-07-05T12:18:55.608790324Z     ...<4 lines>...
2025-07-05T12:18:55.608791934Z         conn,
2025-07-05T12:18:55.608793684Z         ^^^^^
2025-07-05T12:18:55.608796404Z     )
2025-07-05T12:18:55.608816965Z     ^
2025-07-05T12:18:55.608826425Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:18:55.608829365Z     result = conn.execute(
2025-07-05T12:18:55.608851836Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:18:55.608855236Z     )
2025-07-05T12:18:55.608857406Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:18:55.608859096Z     return meth(
2025-07-05T12:18:55.608860726Z         self,
2025-07-05T12:18:55.608862366Z         distilled_parameters,
2025-07-05T12:18:55.608864146Z         execution_options or NO_OPTIONS,
2025-07-05T12:18:55.608865776Z     )
2025-07-05T12:18:55.608867446Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:18:55.608869326Z     return connection._execute_clauseelement(
2025-07-05T12:18:55.608870966Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:55.608872686Z         self, distilled_params, execution_options
2025-07-05T12:18:55.608874366Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:55.608876086Z     )
2025-07-05T12:18:55.608877726Z     ^
2025-07-05T12:18:55.608879426Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:18:55.608881926Z     ret = self._execute_context(
2025-07-05T12:18:55.608883636Z         dialect,
2025-07-05T12:18:55.608885476Z     ...<8 lines>...
2025-07-05T12:18:55.608887106Z         cache_hit=cache_hit,
2025-07-05T12:18:55.608888986Z     )
2025-07-05T12:18:55.608890737Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1809, in _execute_context
2025-07-05T12:18:55.608892497Z     conn = self._revalidate_connection()
2025-07-05T12:18:55.608894266Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 675, in _revalidate_connection
2025-07-05T12:18:55.608895947Z     self._invalid_transaction()
2025-07-05T12:18:55.608897627Z     ~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:18:55.608899857Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 665, in _invalid_transaction
2025-07-05T12:18:55.608902547Z     raise exc.PendingRollbackError(
2025-07-05T12:18:55.608905377Z     ...<4 lines>...
2025-07-05T12:18:55.608907947Z     )
2025-07-05T12:18:55.608911387Z sqlalchemy.exc.PendingRollbackError: Can't reconnect until invalid transaction is rolled back.  Please rollback() fully before proceeding (Background on this error at: https://sqlalche.me/e/20/8s2b)
2025-07-05T12:18:58.441604902Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:18:58.441626452Z Traceback (most recent call last):
2025-07-05T12:18:58.441633242Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:58.441637783Z     self.dialect.do_execute(
2025-07-05T12:18:58.441640143Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441643063Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:58.441645343Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441647503Z     )
2025-07-05T12:18:58.441649653Z     ^
2025-07-05T12:18:58.441652643Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:58.441655453Z     cursor.execute(statement, parameters)
2025-07-05T12:18:58.441657693Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441660663Z psycopg2.errors.UndefinedColumn: column cart_items.user_id does not exist
2025-07-05T12:18:58.441678114Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:18:58.441694064Z                                                ^
2025-07-05T12:18:58.441696414Z 
2025-07-05T12:18:58.441698414Z 
2025-07-05T12:18:58.441700604Z The above exception was the direct cause of the following exception:
2025-07-05T12:18:58.441702604Z 
2025-07-05T12:18:58.441704804Z Traceback (most recent call last):
2025-07-05T12:18:58.441707514Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:18:58.441709774Z     response = self.full_dispatch_request()
2025-07-05T12:18:58.441712014Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:18:58.441714184Z     rv = self.handle_user_exception(e)
2025-07-05T12:18:58.441716435Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:18:58.441718895Z     rv = self.dispatch_request()
2025-07-05T12:18:58.441721084Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:18:58.441723315Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:18:58.441725555Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:18:58.441727865Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 290, in decorated_view
2025-07-05T12:18:58.441730415Z     return current_app.ensure_sync(func)(*args, **kwargs)
2025-07-05T12:18:58.441732985Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441735325Z   File "/opt/render/project/src/routes/cart.py", line 58, in view_cart
2025-07-05T12:18:58.441737545Z     cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
2025-07-05T12:18:58.441739675Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2704, in all
2025-07-05T12:18:58.441741865Z     return self._iter().all()  # type: ignore
2025-07-05T12:18:58.441744475Z            ~~~~~~~~~~^^
2025-07-05T12:18:58.441746645Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2857, in _iter
2025-07-05T12:18:58.441748745Z     result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
2025-07-05T12:18:58.441750855Z                                                   ~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441752985Z         statement,
2025-07-05T12:18:58.441755165Z         ^^^^^^^^^^
2025-07-05T12:18:58.441757415Z         params,
2025-07-05T12:18:58.441759665Z         ^^^^^^^
2025-07-05T12:18:58.441761856Z         execution_options={"_sa_orm_load_options": self.load_options},
2025-07-05T12:18:58.441764085Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441766205Z     )
2025-07-05T12:18:58.441768336Z     ^
2025-07-05T12:18:58.441770556Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:18:58.441772996Z     return self._execute_internal(
2025-07-05T12:18:58.441775246Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441777536Z         statement,
2025-07-05T12:18:58.441779706Z         ^^^^^^^^^^
2025-07-05T12:18:58.441782006Z     ...<4 lines>...
2025-07-05T12:18:58.441784066Z         _add_event=_add_event,
2025-07-05T12:18:58.441786176Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441788276Z     )
2025-07-05T12:18:58.441790556Z     ^
2025-07-05T12:18:58.441815927Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:18:58.441823637Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:18:58.441826147Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441828197Z         self,
2025-07-05T12:18:58.441830347Z         ^^^^^
2025-07-05T12:18:58.441832447Z     ...<4 lines>...
2025-07-05T12:18:58.441834537Z         conn,
2025-07-05T12:18:58.441836727Z         ^^^^^
2025-07-05T12:18:58.441838767Z     )
2025-07-05T12:18:58.441840967Z     ^
2025-07-05T12:18:58.441843277Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:18:58.441845447Z     result = conn.execute(
2025-07-05T12:18:58.441847577Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:18:58.441849698Z     )
2025-07-05T12:18:58.441851958Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:18:58.441854187Z     return meth(
2025-07-05T12:18:58.441856307Z         self,
2025-07-05T12:18:58.441858458Z         distilled_parameters,
2025-07-05T12:18:58.441860698Z         execution_options or NO_OPTIONS,
2025-07-05T12:18:58.441862958Z     )
2025-07-05T12:18:58.441865388Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:18:58.441867908Z     return connection._execute_clauseelement(
2025-07-05T12:18:58.441870558Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441872988Z         self, distilled_params, execution_options
2025-07-05T12:18:58.441888258Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441891218Z     )
2025-07-05T12:18:58.441893368Z     ^
2025-07-05T12:18:58.441895719Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:18:58.441897899Z     ret = self._execute_context(
2025-07-05T12:18:58.441900059Z         dialect,
2025-07-05T12:18:58.441902199Z     ...<8 lines>...
2025-07-05T12:18:58.441904379Z         cache_hit=cache_hit,
2025-07-05T12:18:58.441906479Z     )
2025-07-05T12:18:58.441908739Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:18:58.441911109Z     return self._exec_single_context(
2025-07-05T12:18:58.441913209Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441915359Z         dialect, context, statement, parameters
2025-07-05T12:18:58.441917639Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441919839Z     )
2025-07-05T12:18:58.441921919Z     ^
2025-07-05T12:18:58.441924069Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:18:58.441926159Z     self._handle_dbapi_exception(
2025-07-05T12:18:58.441928269Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.441930399Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:18:58.441932519Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.441934639Z     )
2025-07-05T12:18:58.441936819Z     ^
2025-07-05T12:18:58.441939Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:18:58.441941189Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:18:58.44194891Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:18:58.44195133Z     self.dialect.do_execute(
2025-07-05T12:18:58.44195354Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:18:58.44195562Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:18:58.44195774Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.44195985Z     )
2025-07-05T12:18:58.44196192Z     ^
2025-07-05T12:18:58.44196417Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:18:58.44196637Z     cursor.execute(statement, parameters)
2025-07-05T12:18:58.44196856Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:18:58.44197086Z sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column cart_items.user_id does not exist
2025-07-05T12:18:58.44197306Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:18:58.44197526Z                                                ^
2025-07-05T12:18:58.44197727Z 
2025-07-05T12:18:58.44198099Z [SQL: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS cart_items_user_id, cart_items.product_id AS cart_items_product_id, cart_items.quantity AS cart_items_quantity, cart_items.size AS cart_items_size, cart_items.color AS cart_items_color, cart_items.created_at AS cart_items_created_at, cart_items.updated_at AS cart_items_updated_at 
2025-07-05T12:18:58.441983281Z FROM cart_items 
2025-07-05T12:18:58.441985561Z WHERE cart_items.user_id = %(user_id_1)s]
2025-07-05T12:18:58.441987861Z [parameters: {'user_id_1': 1}]
2025-07-05T12:18:58.44199035Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-07-05T12:18:58.614660119Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /cart/view HTTP/1.1" 500 20217 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.807996423Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/css/style.css HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.809334563Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/js/libs/SplitType.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.810457309Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.811460741Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/js/libs/ScrollTrigger.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.812468024Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/js/main.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:58.813545478Z 127.0.0.1 - - [05/Jul/2025:12:18:58 +0000] "GET /static/js/libs/gsap.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:59.027614349Z 127.0.0.1 - - [05/Jul/2025:12:18:59 +0000] "POST /api/cart/sync HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:59.029059382Z 127.0.0.1 - - [05/Jul/2025:12:18:59 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXeRY HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:18:59.037646465Z 127.0.0.1 - - [05/Jul/2025:12:18:59 +0000] "GET /api/cart/count HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:24.029436243Z 127.0.0.1 - - [05/Jul/2025:12:19:24 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXeTd&sid=PXi6GIoj7Ss3rv8BAAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:24.031004858Z 127.0.0.1 - - [05/Jul/2025:12:19:24 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQXeTc&sid=PXi6GIoj7Ss3rv8BAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:54.16636048Z [2025-07-05 12:19:54 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:110)
2025-07-05T12:19:54.170984565Z [2025-07-05 12:19:54 +0000] [110] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=PXi6GIoj7Ss3rv8BAAAA
2025-07-05T12:19:54.170998115Z Traceback (most recent call last):
2025-07-05T12:19:54.171003725Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:19:54.171008675Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:19:54.171013115Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171017105Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:19:54.171021265Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:19:54.171026275Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:19:54.171030546Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:19:54.171034906Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171039346Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:19:54.171043236Z     return super().__call__(environ, start_response)
2025-07-05T12:19:54.171046826Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171050416Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:19:54.171055066Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:19:54.171059116Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171062926Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:19:54.171066926Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:19:54.171071036Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171075256Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:19:54.171079327Z     packets = socket.handle_get_request(
2025-07-05T12:19:54.171093667Z         environ, start_response)
2025-07-05T12:19:54.171096347Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:19:54.171098787Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:19:54.171101507Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:19:54.171104037Z                                                   start_response)
2025-07-05T12:19:54.171106517Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171109277Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:19:54.171111807Z     return ws(environ, start_response)
2025-07-05T12:19:54.171115037Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:19:54.171118408Z     ret = self.app(self)
2025-07-05T12:19:54.171120997Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:19:54.171123618Z     pkt = websocket_wait()
2025-07-05T12:19:54.171126358Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:19:54.171128758Z     data = ws.wait()
2025-07-05T12:19:54.171131558Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:19:54.171133798Z     return self.ws.receive()
2025-07-05T12:19:54.171136068Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:19:54.171138568Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:19:54.171141088Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:19:54.171143308Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:19:54.171145528Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:19:54.171147708Z     signaled = self._cond.wait(timeout)
2025-07-05T12:19:54.171150028Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:19:54.171152198Z     waiter.acquire()
2025-07-05T12:19:54.171154368Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:19:54.171155688Z 127.0.0.1 - - [05/Jul/2025:12:19:54 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=PXi6GIoj7Ss3rv8BAAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:19:54.171156648Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:19:54.171167679Z     sys.exit(1)
2025-07-05T12:19:54.171170439Z     ~~~~~~~~^^^
2025-07-05T12:19:54.171172649Z SystemExit: 1
2025-07-05T12:19:54.171355313Z [2025-07-05 12:19:54 +0000] [110] [INFO] Worker exiting (pid: 110)
2025-07-05T12:19:55.215855476Z [2025-07-05 12:19:55 +0000] [105] [ERROR] Worker (pid:110) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:19:55.309484694Z [2025-07-05 12:19:55 +0000] [114] [INFO] Booting worker with pid: 114
2025-07-05T12:19:55.313615097Z Invalid session PXi6GIoj7Ss3rv8BAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:19:55.313631428Z ERROR:engineio.server:Invalid session PXi6GIoj7Ss3rv8BAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:19:55.314382504Z 127.0.0.1 - - [05/Jul/2025:12:19:55 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXkaD&sid=PXi6GIoj7Ss3rv8BAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:55.31505342Z 127.0.0.1 - - [05/Jul/2025:12:19:55 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQXkb3&sid=PXi6GIoj7Ss3rv8BAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:57.04989797Z 127.0.0.1 - - [05/Jul/2025:12:19:57 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXsc7 HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:57.163638521Z 127.0.0.1 - - [05/Jul/2025:12:19:57 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQXsdy&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:19:57.195739934Z 127.0.0.1 - - [05/Jul/2025:12:19:57 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXsd_&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:22.050015308Z 127.0.0.1 - - [05/Jul/2025:12:20:22 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXsgG&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:52.282288695Z [2025-07-05 12:20:52 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:114)
2025-07-05T12:20:52.28825208Z [2025-07-05 12:20:52 +0000] [114] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=_NgRcEeRodb3535lAAAA
2025-07-05T12:20:52.28827184Z Traceback (most recent call last):
2025-07-05T12:20:52.28827595Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:20:52.28828009Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:20:52.28828373Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288287241Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:20:52.28829077Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:20:52.288295841Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:20:52.288299471Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:20:52.288303041Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288306601Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:20:52.288310751Z     return super().__call__(environ, start_response)
2025-07-05T12:20:52.288314451Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288318161Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:20:52.288322091Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:20:52.288325671Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288329181Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:20:52.288332771Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:20:52.288336242Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288339782Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:20:52.288352432Z     packets = socket.handle_get_request(
2025-07-05T12:20:52.288355752Z         environ, start_response)
2025-07-05T12:20:52.288357922Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:20:52.288360262Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:20:52.288362712Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:20:52.288365072Z                                                   start_response)
2025-07-05T12:20:52.288367362Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288369582Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:20:52.288371752Z     return ws(environ, start_response)
2025-07-05T12:20:52.288374602Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:20:52.288377612Z     ret = self.app(self)
2025-07-05T12:20:52.288379932Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:20:52.288382203Z     pkt = websocket_wait()
2025-07-05T12:20:52.288384643Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:20:52.288386873Z     data = ws.wait()
2025-07-05T12:20:52.288389193Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:20:52.288391523Z     return self.ws.receive()
2025-07-05T12:20:52.288394043Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:20:52.288396193Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:20:52.288398383Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:20:52.288400563Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:20:52.288402823Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:20:52.288405133Z     signaled = self._cond.wait(timeout)
2025-07-05T12:20:52.288407553Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:20:52.288409783Z     waiter.acquire()
2025-07-05T12:20:52.288412003Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:20:52.288414123Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:20:52.288416423Z     sys.exit(1)
2025-07-05T12:20:52.288418613Z     ~~~~~~~~^^^
2025-07-05T12:20:52.288420844Z SystemExit: 1
2025-07-05T12:20:52.288445554Z 127.0.0.1 - - [05/Jul/2025:12:20:52 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:20:52.288670039Z [2025-07-05 12:20:52 +0000] [114] [INFO] Worker exiting (pid: 114)
2025-07-05T12:20:53.313975809Z [2025-07-05 12:20:53 +0000] [105] [ERROR] Worker (pid:114) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:20:53.317530809Z [2025-07-05 12:20:53 +0000] [118] [INFO] Booting worker with pid: 118
2025-07-05T12:20:53.408769884Z Invalid session _NgRcEeRodb3535lAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:20:53.408786684Z ERROR:engineio.server:Invalid session _NgRcEeRodb3535lAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:20:53.409609683Z 127.0.0.1 - - [05/Jul/2025:12:20:53 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQXykb&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:53.410464242Z 127.0.0.1 - - [05/Jul/2025:12:20:53 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQXyka&sid=_NgRcEeRodb3535lAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:55.101856864Z 127.0.0.1 - - [05/Jul/2025:12:20:55 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQY4mK HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:55.198687794Z 127.0.0.1 - - [05/Jul/2025:12:20:55 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQY4p1&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:20:55.269150731Z 127.0.0.1 - - [05/Jul/2025:12:20:55 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQY4p2&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:20.101954167Z 127.0.0.1 - - [05/Jul/2025:12:21:20 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQY4rZ&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:50.421362699Z [2025-07-05 12:21:50 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:118)
2025-07-05T12:21:50.426224099Z [2025-07-05 12:21:50 +0000] [118] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=AjRiXt6D82hhHMC7AAAA
2025-07-05T12:21:50.426241619Z Traceback (most recent call last):
2025-07-05T12:21:50.426246179Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:21:50.42625153Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:21:50.426255779Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.42625981Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:21:50.42626383Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:21:50.42626825Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:21:50.4262723Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:21:50.42627615Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.42628015Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:21:50.42628429Z     return super().__call__(environ, start_response)
2025-07-05T12:21:50.42628798Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.42629203Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:21:50.426296511Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:21:50.42630098Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.426304831Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:21:50.426308731Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:21:50.426326401Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.426329351Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:21:50.426331841Z     packets = socket.handle_get_request(
2025-07-05T12:21:50.426335161Z         environ, start_response)
2025-07-05T12:21:50.426338151Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:21:50.426340792Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:21:50.426343521Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:21:50.426346001Z                                                   start_response)
2025-07-05T12:21:50.426348602Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:21:50.426351202Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:21:50.426353662Z     return ws(environ, start_response)
2025-07-05T12:21:50.426356962Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:21:50.426360372Z     ret = self.app(self)
2025-07-05T12:21:50.426363292Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:21:50.426365782Z     pkt = websocket_wait()
2025-07-05T12:21:50.426368762Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:21:50.426374782Z     data = ws.wait()
2025-07-05T12:21:50.426377492Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:21:50.426380012Z     return self.ws.receive()
2025-07-05T12:21:50.426382732Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:21:50.426385362Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:21:50.426388293Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:21:50.426391053Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:21:50.426393673Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:21:50.426396183Z     signaled = self._cond.wait(timeout)
2025-07-05T12:21:50.426398793Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:21:50.426401183Z     waiter.acquire()
2025-07-05T12:21:50.426403993Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:21:50.426406993Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:21:50.426409613Z     sys.exit(1)
2025-07-05T12:21:50.426412383Z     ~~~~~~~~^^^
2025-07-05T12:21:50.426414953Z SystemExit: 1
2025-07-05T12:21:50.426440234Z 127.0.0.1 - - [05/Jul/2025:12:21:50 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:21:50.426701589Z [2025-07-05 12:21:50 +0000] [118] [INFO] Worker exiting (pid: 118)
2025-07-05T12:21:51.511145531Z [2025-07-05 12:21:51 +0000] [105] [ERROR] Worker (pid:118) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:21:51.514747332Z [2025-07-05 12:21:51 +0000] [122] [INFO] Booting worker with pid: 122
2025-07-05T12:21:51.519155082Z Invalid session AjRiXt6D82hhHMC7AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:21:51.519169432Z ERROR:engineio.server:Invalid session AjRiXt6D82hhHMC7AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:21:51.520016321Z 127.0.0.1 - - [05/Jul/2025:12:21:51 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYAwl&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:51.520775658Z 127.0.0.1 - - [05/Jul/2025:12:21:51 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQYAwk&sid=AjRiXt6D82hhHMC7AAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:53.028494673Z 127.0.0.1 - - [05/Jul/2025:12:21:53 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYIwQ HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:53.120705269Z 127.0.0.1 - - [05/Jul/2025:12:21:53 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQYIy2&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:21:53.121218551Z 127.0.0.1 - - [05/Jul/2025:12:21:53 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYIy3&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:22:18.028452076Z 127.0.0.1 - - [05/Jul/2025:12:22:18 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYIzU&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:22:52.63239092Z ==> Detected service running on port 10000
2025-07-05T12:22:53.00681994Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-07-05T12:22:48.624276585Z [2025-07-05 12:22:48 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:122)
2025-07-05T12:22:48.630615678Z [2025-07-05 12:22:48 +0000] [122] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=3BXgzyWH-dL5Drc0AAAA
2025-07-05T12:22:48.630633258Z Traceback (most recent call last):
2025-07-05T12:22:48.630638228Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:22:48.630643498Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:22:48.630647719Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.630651728Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:22:48.630655889Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:22:48.630660709Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:22:48.630665019Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:22:48.630669379Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.630673759Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:22:48.630676549Z     return super().__call__(environ, start_response)
2025-07-05T12:22:48.630680209Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.630684709Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:22:48.630689819Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:22:48.630694489Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.63069866Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:22:48.63071653Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:22:48.63071874Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.63072051Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:22:48.63072224Z     packets = socket.handle_get_request(
2025-07-05T12:22:48.63072454Z         environ, start_response)
2025-07-05T12:22:48.63072625Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:22:48.63072818Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:22:48.63072983Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:22:48.63073153Z                                                   start_response)
2025-07-05T12:22:48.63073321Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:22:48.63073497Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:22:48.63073663Z     return ws(environ, start_response)
2025-07-05T12:22:48.630738921Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:22:48.630741041Z     ret = self.app(self)
2025-07-05T12:22:48.63074309Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:22:48.630747361Z     pkt = websocket_wait()
2025-07-05T12:22:48.630749491Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:22:48.630751161Z     data = ws.wait()
2025-07-05T12:22:48.630752921Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:22:48.630754691Z     return self.ws.receive()
2025-07-05T12:22:48.630756351Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:22:48.630757991Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:22:48.630759971Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:22:48.630761621Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:22:48.630763261Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:22:48.630764911Z     signaled = self._cond.wait(timeout)
2025-07-05T12:22:48.630766541Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:22:48.630768201Z     waiter.acquire()
2025-07-05T12:22:48.630770771Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:22:48.630773661Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:22:48.630776791Z     sys.exit(1)
2025-07-05T12:22:48.630779921Z     ~~~~~~~~^^^
2025-07-05T12:22:48.630782631Z SystemExit: 1
2025-07-05T12:22:48.630879474Z 127.0.0.1 - - [05/Jul/2025:12:22:48 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:22:48.63113681Z [2025-07-05 12:22:48 +0000] [122] [INFO] Worker exiting (pid: 122)
2025-07-05T12:22:49.716203835Z [2025-07-05 12:22:49 +0000] [105] [ERROR] Worker (pid:122) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:22:49.720327098Z [2025-07-05 12:22:49 +0000] [126] [INFO] Booting worker with pid: 126
2025-07-05T12:22:49.809425645Z Invalid session 3BXgzyWH-dL5Drc0AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:22:49.809457495Z ERROR:engineio.server:Invalid session 3BXgzyWH-dL5Drc0AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:22:49.810177342Z 127.0.0.1 - - [05/Jul/2025:12:22:49 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQYP4H&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:22:49.810768895Z 127.0.0.1 - - [05/Jul/2025:12:22:49 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYP4H.0&sid=3BXgzyWH-dL5Drc0AAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:22:50.110008814Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:22:50.110026634Z Traceback (most recent call last):
2025-07-05T12:22:50.110030484Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:22:50.110033584Z     self.dialect.do_execute(
2025-07-05T12:22:50.110035994Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110038474Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:22:50.110040684Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110043104Z     )
2025-07-05T12:22:50.110045555Z     ^
2025-07-05T12:22:50.110048544Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:22:50.110051635Z     cursor.execute(statement, parameters)
2025-07-05T12:22:50.110054695Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110056445Z psycopg2.OperationalError: SSL SYSCALL error: EOF detected
2025-07-05T12:22:50.110058005Z 
2025-07-05T12:22:50.110059565Z 
2025-07-05T12:22:50.110061965Z The above exception was the direct cause of the following exception:
2025-07-05T12:22:50.110063535Z 
2025-07-05T12:22:50.110065295Z Traceback (most recent call last):
2025-07-05T12:22:50.110067125Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:22:50.110068765Z     response = self.full_dispatch_request()
2025-07-05T12:22:50.110070505Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:22:50.110072175Z     rv = self.handle_user_exception(e)
2025-07-05T12:22:50.110073905Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:22:50.110075675Z     rv = self.dispatch_request()
2025-07-05T12:22:50.110077375Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:22:50.110079055Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:22:50.110080805Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:22:50.110082465Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:22:50.110084125Z     elif not current_user.is_authenticated:
2025-07-05T12:22:50.110085935Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110087575Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:22:50.110089285Z     obj = instance._get_current_object()
2025-07-05T12:22:50.110090925Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:22:50.110102066Z     return get_name(local())
2025-07-05T12:22:50.110103926Z                     ~~~~~^^
2025-07-05T12:22:50.110105526Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:22:50.110107186Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:22:50.110108866Z                                       ~~~~~~~~~^^
2025-07-05T12:22:50.110110506Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:22:50.110112126Z     current_app.login_manager._load_user()
2025-07-05T12:22:50.110113936Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:22:50.110115636Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:22:50.110117266Z     user = self._user_callback(user_id)
2025-07-05T12:22:50.110118966Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:22:50.110120606Z     return User.query.get(int(user_id))
2025-07-05T12:22:50.110122276Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:22:50.110123866Z   File "<string>", line 2, in get
2025-07-05T12:22:50.110125546Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:22:50.110127156Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:22:50.110128856Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:22:50.110130536Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:22:50.110132166Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110133786Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:22:50.110135426Z     return self.session._get_impl(
2025-07-05T12:22:50.110137406Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110139066Z         mapper,
2025-07-05T12:22:50.110140777Z         ^^^^^^^
2025-07-05T12:22:50.110142657Z     ...<6 lines>...
2025-07-05T12:22:50.110144347Z         execution_options=self._execution_options,
2025-07-05T12:22:50.110146027Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110147677Z     )
2025-07-05T12:22:50.110149387Z     ^
2025-07-05T12:22:50.110151037Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:22:50.110152717Z     return db_load_fn(
2025-07-05T12:22:50.110154357Z         self,
2025-07-05T12:22:50.110156037Z     ...<5 lines>...
2025-07-05T12:22:50.110157657Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.110159287Z     )
2025-07-05T12:22:50.110160987Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:22:50.110162717Z     session.execute(
2025-07-05T12:22:50.110164357Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110166037Z         q,
2025-07-05T12:22:50.110167717Z         ^^
2025-07-05T12:22:50.110169397Z     ...<2 lines>...
2025-07-05T12:22:50.110171077Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.110172747Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110185178Z     )
2025-07-05T12:22:50.110187088Z     ^
2025-07-05T12:22:50.110188788Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:22:50.110194298Z     return self._execute_internal(
2025-07-05T12:22:50.110196018Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110197648Z         statement,
2025-07-05T12:22:50.110199278Z         ^^^^^^^^^^
2025-07-05T12:22:50.110200878Z     ...<4 lines>...
2025-07-05T12:22:50.110202548Z         _add_event=_add_event,
2025-07-05T12:22:50.110204158Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110205778Z     )
2025-07-05T12:22:50.110207388Z     ^
2025-07-05T12:22:50.110209468Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:22:50.110211158Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:22:50.110212848Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110214478Z         self,
2025-07-05T12:22:50.110216138Z         ^^^^^
2025-07-05T12:22:50.110217748Z     ...<4 lines>...
2025-07-05T12:22:50.110219368Z         conn,
2025-07-05T12:22:50.110220988Z         ^^^^^
2025-07-05T12:22:50.110222588Z     )
2025-07-05T12:22:50.110224208Z     ^
2025-07-05T12:22:50.110225959Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:22:50.110227639Z     result = conn.execute(
2025-07-05T12:22:50.110229288Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:22:50.110231089Z     )
2025-07-05T12:22:50.110232749Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:22:50.110234359Z     return meth(
2025-07-05T12:22:50.110236039Z         self,
2025-07-05T12:22:50.110237679Z         distilled_parameters,
2025-07-05T12:22:50.110239349Z         execution_options or NO_OPTIONS,
2025-07-05T12:22:50.110240979Z     )
2025-07-05T12:22:50.110242749Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:22:50.110244409Z     return connection._execute_clauseelement(
2025-07-05T12:22:50.110246039Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.110247759Z         self, distilled_params, execution_options
2025-07-05T12:22:50.110249399Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110251049Z     )
2025-07-05T12:22:50.110252769Z     ^
2025-07-05T12:22:50.110254419Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:22:50.110256049Z     ret = self._execute_context(
2025-07-05T12:22:50.110257669Z         dialect,
2025-07-05T12:22:50.110259309Z     ...<8 lines>...
2025-07-05T12:22:50.110260939Z         cache_hit=cache_hit,
2025-07-05T12:22:50.110262599Z     )
2025-07-05T12:22:50.110264209Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:22:50.110265869Z     return self._exec_single_context(
2025-07-05T12:22:50.11026754Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.11026924Z         dialect, context, statement, parameters
2025-07-05T12:22:50.110270849Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.1102725Z     )
2025-07-05T12:22:50.11027415Z     ^
2025-07-05T12:22:50.11027587Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:22:50.11027752Z     self._handle_dbapi_exception(
2025-07-05T12:22:50.11028176Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.11028349Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:22:50.11028509Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.11028674Z     )
2025-07-05T12:22:50.11028842Z     ^
2025-07-05T12:22:50.11029007Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:22:50.1102918Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:22:50.11029345Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:22:50.1102951Z     self.dialect.do_execute(
2025-07-05T12:22:50.1102968Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.11029849Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:22:50.11030014Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.1103018Z     )
2025-07-05T12:22:50.11030343Z     ^
2025-07-05T12:22:50.11030508Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:22:50.11030673Z     cursor.execute(statement, parameters)
2025-07-05T12:22:50.11030834Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.110310201Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
2025-07-05T12:22:50.11031173Z 
2025-07-05T12:22:50.110315481Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:22:50.110317181Z FROM users 
2025-07-05T12:22:50.110318891Z WHERE users.id = %(pk_1)s]
2025-07-05T12:22:50.110320581Z [parameters: {'pk_1': 1}]
2025-07-05T12:22:50.110322291Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:22:50.209123316Z [2025-07-05 12:22:50 +0000] [126] [ERROR] Error handling request /cart/view
2025-07-05T12:22:50.209157266Z Traceback (most recent call last):
2025-07-05T12:22:50.209161636Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:22:50.209165347Z     self.dialect.do_execute(
2025-07-05T12:22:50.209167937Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209171787Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:22:50.209174107Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209176697Z     )
2025-07-05T12:22:50.209179447Z     ^
2025-07-05T12:22:50.209182837Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:22:50.209185077Z     cursor.execute(statement, parameters)
2025-07-05T12:22:50.209187587Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209190337Z psycopg2.OperationalError: SSL SYSCALL error: EOF detected
2025-07-05T12:22:50.209192917Z 
2025-07-05T12:22:50.209195237Z 
2025-07-05T12:22:50.209198277Z The above exception was the direct cause of the following exception:
2025-07-05T12:22:50.209200877Z 
2025-07-05T12:22:50.209203737Z Traceback (most recent call last):
2025-07-05T12:22:50.209207217Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:22:50.209223748Z     response = self.full_dispatch_request()
2025-07-05T12:22:50.209227168Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:22:50.209229128Z     rv = self.handle_user_exception(e)
2025-07-05T12:22:50.209230988Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:22:50.209232728Z     rv = self.dispatch_request()
2025-07-05T12:22:50.209234518Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:22:50.209236268Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:22:50.209238148Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:22:50.209239988Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:22:50.209241678Z     elif not current_user.is_authenticated:
2025-07-05T12:22:50.209243408Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209245018Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:22:50.209246669Z     obj = instance._get_current_object()
2025-07-05T12:22:50.209248438Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:22:50.209250069Z     return get_name(local())
2025-07-05T12:22:50.209251698Z                     ~~~~~^^
2025-07-05T12:22:50.209253329Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:22:50.209255059Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:22:50.209256689Z                                       ~~~~~~~~~^^
2025-07-05T12:22:50.209258299Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:22:50.209260229Z     current_app.login_manager._load_user()
2025-07-05T12:22:50.209261879Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:22:50.209263549Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:22:50.209265179Z     user = self._user_callback(user_id)
2025-07-05T12:22:50.209266899Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:22:50.209268539Z     return User.query.get(int(user_id))
2025-07-05T12:22:50.209270199Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:22:50.209272079Z   File "<string>", line 2, in get
2025-07-05T12:22:50.209273839Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:22:50.209275509Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:22:50.209277209Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:22:50.209278839Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:22:50.209280459Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209282079Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:22:50.209283729Z     return self.session._get_impl(
2025-07-05T12:22:50.209285369Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209287089Z         mapper,
2025-07-05T12:22:50.209288789Z         ^^^^^^^
2025-07-05T12:22:50.209295139Z     ...<6 lines>...
2025-07-05T12:22:50.209298259Z         execution_options=self._execution_options,
2025-07-05T12:22:50.20930098Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.20930363Z     )
2025-07-05T12:22:50.20930647Z     ^
2025-07-05T12:22:50.2093092Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:22:50.20931181Z     return db_load_fn(
2025-07-05T12:22:50.2093144Z         self,
2025-07-05T12:22:50.20931691Z     ...<5 lines>...
2025-07-05T12:22:50.20931983Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.20932184Z     )
2025-07-05T12:22:50.20932355Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:22:50.20932525Z     session.execute(
2025-07-05T12:22:50.20932691Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.20932855Z         q,
2025-07-05T12:22:50.20933019Z         ^^
2025-07-05T12:22:50.20933184Z     ...<2 lines>...
2025-07-05T12:22:50.20933351Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.20933814Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.20933998Z     )
2025-07-05T12:22:50.209341611Z     ^
2025-07-05T12:22:50.209343391Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:22:50.209344801Z 127.0.0.1 - - [05/Jul/2025:12:22:50 +0000] "GET /cart/view HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:22:50.209345071Z     return self._execute_internal(
2025-07-05T12:22:50.209346781Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209358941Z         statement,
2025-07-05T12:22:50.209361701Z         ^^^^^^^^^^
2025-07-05T12:22:50.209364021Z     ...<4 lines>...
2025-07-05T12:22:50.209367041Z         _add_event=_add_event,
2025-07-05T12:22:50.209369751Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209372021Z     )
2025-07-05T12:22:50.209374481Z     ^
2025-07-05T12:22:50.209377981Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:22:50.209381221Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:22:50.209383812Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209386341Z         self,
2025-07-05T12:22:50.209388842Z         ^^^^^
2025-07-05T12:22:50.209391342Z     ...<4 lines>...
2025-07-05T12:22:50.209393652Z         conn,
2025-07-05T12:22:50.209400272Z         ^^^^^
2025-07-05T12:22:50.209403202Z     )
2025-07-05T12:22:50.209405932Z     ^
2025-07-05T12:22:50.209409012Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:22:50.209411722Z     result = conn.execute(
2025-07-05T12:22:50.209414312Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:22:50.209416752Z     )
2025-07-05T12:22:50.209419302Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:22:50.209421822Z     return meth(
2025-07-05T12:22:50.209424202Z         self,
2025-07-05T12:22:50.209426402Z         distilled_parameters,
2025-07-05T12:22:50.209429402Z         execution_options or NO_OPTIONS,
2025-07-05T12:22:50.209431622Z     )
2025-07-05T12:22:50.209433853Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:22:50.209444883Z     return connection._execute_clauseelement(
2025-07-05T12:22:50.209447443Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209450323Z         self, distilled_params, execution_options
2025-07-05T12:22:50.209452463Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209454753Z     )
2025-07-05T12:22:50.209456923Z     ^
2025-07-05T12:22:50.209459663Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:22:50.209461863Z     ret = self._execute_context(
2025-07-05T12:22:50.209464183Z         dialect,
2025-07-05T12:22:50.209466543Z     ...<8 lines>...
2025-07-05T12:22:50.209468893Z         cache_hit=cache_hit,
2025-07-05T12:22:50.209471123Z     )
2025-07-05T12:22:50.209473654Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:22:50.209476254Z     return self._exec_single_context(
2025-07-05T12:22:50.209479164Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209481914Z         dialect, context, statement, parameters
2025-07-05T12:22:50.209484544Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209486984Z     )
2025-07-05T12:22:50.209489464Z     ^
2025-07-05T12:22:50.209491924Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:22:50.209494274Z     self._handle_dbapi_exception(
2025-07-05T12:22:50.209496754Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209499174Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:22:50.209501374Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209503794Z     )
2025-07-05T12:22:50.209506474Z     ^
2025-07-05T12:22:50.209509314Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:22:50.209511844Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:22:50.209514084Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:22:50.209516504Z     self.dialect.do_execute(
2025-07-05T12:22:50.209518875Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209521355Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:22:50.209523735Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209526325Z     )
2025-07-05T12:22:50.209528595Z     ^
2025-07-05T12:22:50.209531105Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:22:50.209533425Z     cursor.execute(statement, parameters)
2025-07-05T12:22:50.209535805Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209538135Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
2025-07-05T12:22:50.209540385Z 
2025-07-05T12:22:50.209543705Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:22:50.209546105Z FROM users 
2025-07-05T12:22:50.209548445Z WHERE users.id = %(pk_1)s]
2025-07-05T12:22:50.209550775Z [parameters: {'pk_1': 1}]
2025-07-05T12:22:50.209560296Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:22:50.209562825Z 
2025-07-05T12:22:50.209565856Z During handling of the above exception, another exception occurred:
2025-07-05T12:22:50.209568046Z 
2025-07-05T12:22:50.209570296Z Traceback (most recent call last):
2025-07-05T12:22:50.209572876Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:22:50.209575706Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:22:50.209578226Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209594866Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:22:50.209598396Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:22:50.209601496Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:22:50.209603866Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:22:50.209606557Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209609186Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:22:50.209611577Z     return super().__call__(environ, start_response)
2025-07-05T12:22:50.209614077Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209616627Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 74, in __call__
2025-07-05T12:22:50.209619017Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:22:50.209621547Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209624147Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1514, in wsgi_app
2025-07-05T12:22:50.209626667Z     response = self.handle_exception(e)
2025-07-05T12:22:50.209629227Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 860, in handle_exception
2025-07-05T12:22:50.209631747Z     server_error = self.ensure_sync(handler)(server_error)
2025-07-05T12:22:50.209634227Z   File "/opt/render/project/src/app.py", line 65, in internal_server_error
2025-07-05T12:22:50.209636867Z     return render_template('500.html'), 500
2025-07-05T12:22:50.209639437Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-07-05T12:22:50.209642437Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 150, in render_template
2025-07-05T12:22:50.209645177Z     return _render(app, template, context)
2025-07-05T12:22:50.209647807Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 127, in _render
2025-07-05T12:22:50.209663398Z     app.update_template_context(context)
2025-07-05T12:22:50.209665918Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:22:50.209668288Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 530, in update_template_context
2025-07-05T12:22:50.209670418Z     context.update(self.ensure_sync(func)())
2025-07-05T12:22:50.209672588Z                    ~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:22:50.209674978Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 405, in _user_context_processor
2025-07-05T12:22:50.209677368Z     return dict(current_user=_get_user())
2025-07-05T12:22:50.209679828Z                              ~~~~~~~~~^^
2025-07-05T12:22:50.209682278Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:22:50.209690398Z     current_app.login_manager._load_user()
2025-07-05T12:22:50.209693208Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:22:50.209695639Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:22:50.209698068Z     user = self._user_callback(user_id)
2025-07-05T12:22:50.209700859Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:22:50.209703539Z     return User.query.get(int(user_id))
2025-07-05T12:22:50.209706279Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:22:50.209709019Z   File "<string>", line 2, in get
2025-07-05T12:22:50.209714899Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:22:50.209717849Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:22:50.209720589Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:22:50.209723139Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:22:50.209726129Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209728809Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:22:50.209731679Z     return self.session._get_impl(
2025-07-05T12:22:50.209734409Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209737409Z         mapper,
2025-07-05T12:22:50.20974032Z         ^^^^^^^
2025-07-05T12:22:50.20974308Z     ...<6 lines>...
2025-07-05T12:22:50.20974586Z         execution_options=self._execution_options,
2025-07-05T12:22:50.20974879Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.20975146Z     )
2025-07-05T12:22:50.20975399Z     ^
2025-07-05T12:22:50.20975697Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:22:50.20975955Z     return db_load_fn(
2025-07-05T12:22:50.20976197Z         self,
2025-07-05T12:22:50.20976475Z     ...<5 lines>...
2025-07-05T12:22:50.20976764Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.20977021Z     )
2025-07-05T12:22:50.20977307Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:22:50.20977625Z     session.execute(
2025-07-05T12:22:50.20977886Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.20978139Z         q,
2025-07-05T12:22:50.20978395Z         ^^
2025-07-05T12:22:50.209786261Z     ...<2 lines>...
2025-07-05T12:22:50.209788861Z         bind_arguments=bind_arguments,
2025-07-05T12:22:50.209791661Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209794211Z     )
2025-07-05T12:22:50.209796591Z     ^
2025-07-05T12:22:50.209879763Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:22:50.209891393Z     return self._execute_internal(
2025-07-05T12:22:50.209894433Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209913213Z         statement,
2025-07-05T12:22:50.209916744Z         ^^^^^^^^^^
2025-07-05T12:22:50.209919213Z     ...<4 lines>...
2025-07-05T12:22:50.209921884Z         _add_event=_add_event,
2025-07-05T12:22:50.209924314Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.209927144Z     )
2025-07-05T12:22:50.209930114Z     ^
2025-07-05T12:22:50.209932984Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:22:50.209943084Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:22:50.209946334Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.209948934Z         self,
2025-07-05T12:22:50.209951934Z         ^^^^^
2025-07-05T12:22:50.209954784Z     ...<4 lines>...
2025-07-05T12:22:50.209957384Z         conn,
2025-07-05T12:22:50.209959694Z         ^^^^^
2025-07-05T12:22:50.209962574Z     )
2025-07-05T12:22:50.209965474Z     ^
2025-07-05T12:22:50.209968545Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:22:50.209971575Z     result = conn.execute(
2025-07-05T12:22:50.209974625Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:22:50.209977335Z     )
2025-07-05T12:22:50.209980325Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:22:50.209983025Z     return meth(
2025-07-05T12:22:50.209985755Z         self,
2025-07-05T12:22:50.209988415Z         distilled_parameters,
2025-07-05T12:22:50.209990975Z         execution_options or NO_OPTIONS,
2025-07-05T12:22:50.209993845Z     )
2025-07-05T12:22:50.209996635Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:22:50.209999305Z     return connection._execute_clauseelement(
2025-07-05T12:22:50.210002295Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:22:50.210005095Z         self, distilled_params, execution_options
2025-07-05T12:22:50.210007795Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:22:50.210010666Z     )
2025-07-05T12:22:50.210013116Z     ^
2025-07-05T12:22:50.210015606Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:22:50.210018336Z     ret = self._execute_context(
2025-07-05T12:22:50.210020636Z         dialect,
2025-07-05T12:22:50.210023466Z     ...<8 lines>...
2025-07-05T12:22:50.210025876Z         cache_hit=cache_hit,
2025-07-05T12:22:50.210028406Z     )
2025-07-05T12:22:50.210030946Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1809, in _execute_context
2025-07-05T12:22:50.210033796Z     conn = self._revalidate_connection()
2025-07-05T12:22:50.210037016Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 675, in _revalidate_connection
2025-07-05T12:22:50.210039776Z     self._invalid_transaction()
2025-07-05T12:22:50.210042356Z     ~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:22:50.210045236Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 665, in _invalid_transaction
2025-07-05T12:22:50.210048207Z     raise exc.PendingRollbackError(
2025-07-05T12:22:50.210050927Z     ...<4 lines>...
2025-07-05T12:22:50.210053756Z     )
2025-07-05T12:22:50.210057197Z sqlalchemy.exc.PendingRollbackError: Can't reconnect until invalid transaction is rolled back.  Please rollback() fully before proceeding (Background on this error at: https://sqlalche.me/e/20/8s2b)
2025-07-05T12:22:50.217199148Z 127.0.0.1 - - [05/Jul/2025:12:22:50 +0000] "GET /static/css/style.css HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.414866302Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:23:42.414925343Z Traceback (most recent call last):
2025-07-05T12:23:42.414929964Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:23:42.414933324Z     self.dialect.do_execute(
2025-07-05T12:23:42.414936114Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.414939574Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:23:42.414942334Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.414944824Z     )
2025-07-05T12:23:42.414947284Z     ^
2025-07-05T12:23:42.414950334Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:23:42.414953034Z     cursor.execute(statement, parameters)
2025-07-05T12:23:42.414955594Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.414958814Z psycopg2.errors.UndefinedColumn: column cart_items.user_id does not exist
2025-07-05T12:23:42.414961364Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:23:42.414963654Z                                                ^
2025-07-05T12:23:42.414965744Z 
2025-07-05T12:23:42.414967864Z 
2025-07-05T12:23:42.414970424Z The above exception was the direct cause of the following exception:
2025-07-05T12:23:42.414972555Z 
2025-07-05T12:23:42.414975025Z Traceback (most recent call last):
2025-07-05T12:23:42.414980405Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:23:42.414983475Z     response = self.full_dispatch_request()
2025-07-05T12:23:42.414986385Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:23:42.414989455Z     rv = self.handle_user_exception(e)
2025-07-05T12:23:42.414991805Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:23:42.414993485Z     rv = self.dispatch_request()
2025-07-05T12:23:42.414995235Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:23:42.414996935Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:23:42.414998615Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:23:42.415000345Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 290, in decorated_view
2025-07-05T12:23:42.415002045Z     return current_app.ensure_sync(func)(*args, **kwargs)
2025-07-05T12:23:42.415003765Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415005465Z   File "/opt/render/project/src/routes/cart.py", line 58, in view_cart
2025-07-05T12:23:42.415007155Z     cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
2025-07-05T12:23:42.415008865Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2704, in all
2025-07-05T12:23:42.415010505Z     return self._iter().all()  # type: ignore
2025-07-05T12:23:42.415012576Z            ~~~~~~~~~~^^
2025-07-05T12:23:42.415014245Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2857, in _iter
2025-07-05T12:23:42.415015905Z     result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
2025-07-05T12:23:42.415017726Z                                                   ~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415019356Z         statement,
2025-07-05T12:23:42.415025116Z         ^^^^^^^^^^
2025-07-05T12:23:42.415027076Z         params,
2025-07-05T12:23:42.415028776Z         ^^^^^^^
2025-07-05T12:23:42.415030496Z         execution_options={"_sa_orm_load_options": self.load_options},
2025-07-05T12:23:42.415032166Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415033796Z     )
2025-07-05T12:23:42.415035466Z     ^
2025-07-05T12:23:42.415037096Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:23:42.415038766Z     return self._execute_internal(
2025-07-05T12:23:42.415040446Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415042346Z         statement,
2025-07-05T12:23:42.415044076Z         ^^^^^^^^^^
2025-07-05T12:23:42.415045756Z     ...<4 lines>...
2025-07-05T12:23:42.415047756Z         _add_event=_add_event,
2025-07-05T12:23:42.415049406Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415051056Z     )
2025-07-05T12:23:42.415052676Z     ^
2025-07-05T12:23:42.415054326Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:23:42.415055977Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:23:42.415057626Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415059297Z         self,
2025-07-05T12:23:42.415060957Z         ^^^^^
2025-07-05T12:23:42.415062597Z     ...<4 lines>...
2025-07-05T12:23:42.415064247Z         conn,
2025-07-05T12:23:42.415065937Z         ^^^^^
2025-07-05T12:23:42.415067537Z     )
2025-07-05T12:23:42.415069137Z     ^
2025-07-05T12:23:42.415071167Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:23:42.415072847Z     result = conn.execute(
2025-07-05T12:23:42.415074537Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:23:42.415076197Z     )
2025-07-05T12:23:42.415077907Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:23:42.415079557Z     return meth(
2025-07-05T12:23:42.415081247Z         self,
2025-07-05T12:23:42.415082997Z         distilled_parameters,
2025-07-05T12:23:42.415084677Z         execution_options or NO_OPTIONS,
2025-07-05T12:23:42.415086347Z     )
2025-07-05T12:23:42.415087977Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:23:42.415089657Z     return connection._execute_clauseelement(
2025-07-05T12:23:42.415091307Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415092997Z         self, distilled_params, execution_options
2025-07-05T12:23:42.415107088Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415109728Z     )
2025-07-05T12:23:42.415111748Z     ^
2025-07-05T12:23:42.415113568Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:23:42.415126018Z     ret = self._execute_context(
2025-07-05T12:23:42.415127808Z         dialect,
2025-07-05T12:23:42.415129518Z     ...<8 lines>...
2025-07-05T12:23:42.415131228Z         cache_hit=cache_hit,
2025-07-05T12:23:42.415132868Z     )
2025-07-05T12:23:42.415134598Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:23:42.415136468Z     return self._exec_single_context(
2025-07-05T12:23:42.415141508Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415143239Z         dialect, context, statement, parameters
2025-07-05T12:23:42.415144979Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415146599Z     )
2025-07-05T12:23:42.415148248Z     ^
2025-07-05T12:23:42.415149939Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:23:42.415151599Z     self._handle_dbapi_exception(
2025-07-05T12:23:42.415153309Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415155009Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:23:42.415156949Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415158579Z     )
2025-07-05T12:23:42.415160239Z     ^
2025-07-05T12:23:42.415161959Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:23:42.415163639Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:23:42.415165319Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:23:42.415166989Z     self.dialect.do_execute(
2025-07-05T12:23:42.415168659Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:23:42.415170349Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:23:42.415171999Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415173629Z     )
2025-07-05T12:23:42.415175269Z     ^
2025-07-05T12:23:42.415176959Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:23:42.415178679Z     cursor.execute(statement, parameters)
2025-07-05T12:23:42.415180329Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:23:42.415182069Z sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column cart_items.user_id does not exist
2025-07-05T12:23:42.415183729Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:23:42.415185369Z                                                ^
2025-07-05T12:23:42.415186919Z 
2025-07-05T12:23:42.41519036Z [SQL: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS cart_items_user_id, cart_items.product_id AS cart_items_product_id, cart_items.quantity AS cart_items_quantity, cart_items.size AS cart_items_size, cart_items.color AS cart_items_color, cart_items.created_at AS cart_items_created_at, cart_items.updated_at AS cart_items_updated_at 
2025-07-05T12:23:42.415192229Z FROM cart_items 
2025-07-05T12:23:42.415193889Z WHERE cart_items.user_id = %(user_id_1)s]
2025-07-05T12:23:42.41519556Z [parameters: {'user_id_1': 1}]
2025-07-05T12:23:42.41519724Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-07-05T12:23:42.525004542Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /cart/view HTTP/1.1" 500 20217 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.648549985Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/js/libs/gsap.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.658860877Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/js/libs/ScrollTrigger.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.660018853Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/css/style.css HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.66254424Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/js/libs/SplitType.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.744205419Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/js/main.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.748474415Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.883356372Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /api/cart/count HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.894937803Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "POST /api/cart/sync HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.896372005Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYjkk HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:42.952316985Z 127.0.0.1 - - [05/Jul/2025:12:23:42 +0000] "GET /static/assets/musics/Ordinary%20Girl%20-%20Ahv.mp3 HTTP/1.1" 206 1048576 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:43.002536566Z 127.0.0.1 - - [05/Jul/2025:12:23:43 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQYjms&sid=lBCF76ebJ-ZuvnjoAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:43.00714952Z 127.0.0.1 - - [05/Jul/2025:12:23:43 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYjmv&sid=lBCF76ebJ-ZuvnjoAAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:23:43.167948521Z 127.0.0.1 - - [05/Jul/2025:12:23:43 +0000] "GET /static/assets/musics/Ordinary%20Girl%20-%20Ahv.mp3 HTTP/1.1" 206 9899674 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:24:13.868323645Z [2025-07-05 12:24:13 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:126)
2025-07-05T12:24:13.872583491Z [2025-07-05 12:24:13 +0000] [126] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=lBCF76ebJ-ZuvnjoAAAA
2025-07-05T12:24:13.872599781Z Traceback (most recent call last):
2025-07-05T12:24:13.872605861Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:24:13.872611851Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:24:13.872616972Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872637412Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:24:13.872639802Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:24:13.872642632Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:24:13.872644692Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:24:13.872647762Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872649832Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:24:13.872651972Z     return super().__call__(environ, start_response)
2025-07-05T12:24:13.872654092Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872656192Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:24:13.872661473Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:24:13.872663662Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872665702Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:24:13.872667943Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:24:13.872669953Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872672083Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:24:13.872674133Z     packets = socket.handle_get_request(
2025-07-05T12:24:13.872676883Z         environ, start_response)
2025-07-05T12:24:13.872678983Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:24:13.872681133Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:24:13.872683163Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:24:13.872685233Z                                                   start_response)
2025-07-05T12:24:13.872687323Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872689373Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:24:13.872691423Z     return ws(environ, start_response)
2025-07-05T12:24:13.872694583Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:24:13.872697323Z     ret = self.app(self)
2025-07-05T12:24:13.872699403Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:24:13.872701443Z     pkt = websocket_wait()
2025-07-05T12:24:13.872703514Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:24:13.872705554Z     data = ws.wait()
2025-07-05T12:24:13.872707743Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:24:13.872709783Z     return self.ws.receive()
2025-07-05T12:24:13.872711844Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:24:13.872713944Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:24:13.872716064Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:24:13.872718134Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:24:13.872724204Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:24:13.872726374Z     signaled = self._cond.wait(timeout)
2025-07-05T12:24:13.872728474Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:24:13.872730514Z     waiter.acquire()
2025-07-05T12:24:13.872732584Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:24:13.872734694Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:24:13.872738924Z     sys.exit(1)
2025-07-05T12:24:13.872741134Z     ~~~~~~~~^^^
2025-07-05T12:24:13.872743204Z SystemExit: 1
2025-07-05T12:24:13.872787375Z 127.0.0.1 - - [05/Jul/2025:12:24:13 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=lBCF76ebJ-ZuvnjoAAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:24:13.873059562Z [2025-07-05 12:24:13 +0000] [126] [INFO] Worker exiting (pid: 126)
2025-07-05T12:24:14.915306562Z [2025-07-05 12:24:14 +0000] [105] [ERROR] Worker (pid:126) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:24:14.919430315Z [2025-07-05 12:24:14 +0000] [130] [INFO] Booting worker with pid: 130
2025-07-05T12:24:15.009923473Z Invalid session lBCF76ebJ-ZuvnjoAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:24:15.009944844Z ERROR:engineio.server:Invalid session lBCF76ebJ-ZuvnjoAAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:24:15.010713821Z 127.0.0.1 - - [05/Jul/2025:12:24:15 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYjpr&sid=lBCF76ebJ-ZuvnjoAAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:24:15.022488416Z 127.0.0.1 - - [05/Jul/2025:12:24:15 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:24:17.030035195Z 127.0.0.1 - - [05/Jul/2025:12:24:17 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYs4Q HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:24:42.0302498Z 127.0.0.1 - - [05/Jul/2025:12:24:42 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQYs6I&sid=KYmqKW1Hnn4VZofBAAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:24:42.031760574Z 127.0.0.1 - - [05/Jul/2025:12:24:42 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQYs6H&sid=KYmqKW1Hnn4VZofBAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:12.058265288Z [2025-07-05 12:25:12 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:130)
2025-07-05T12:25:12.064712383Z [2025-07-05 12:25:12 +0000] [130] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=KYmqKW1Hnn4VZofBAAAA
2025-07-05T12:25:12.064730134Z Traceback (most recent call last):
2025-07-05T12:25:12.064735514Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:25:12.064740484Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:25:12.064745194Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064749794Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:25:12.064754314Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:25:12.064770755Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:25:12.064773615Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:25:12.064776364Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064778995Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:25:12.064781795Z     return super().__call__(environ, start_response)
2025-07-05T12:25:12.064784955Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064787215Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:25:12.064789595Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:25:12.064791325Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064793245Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:25:12.064794995Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:25:12.064796625Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064822976Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:25:12.064828046Z     packets = socket.handle_get_request(
2025-07-05T12:25:12.064830326Z         environ, start_response)
2025-07-05T12:25:12.064832036Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:25:12.064833776Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:25:12.064835846Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:25:12.064845416Z                                                   start_response)
2025-07-05T12:25:12.064847306Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064849026Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:25:12.064850636Z     return ws(environ, start_response)
2025-07-05T12:25:12.064853056Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:25:12.064855156Z     ret = self.app(self)
2025-07-05T12:25:12.064856916Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 225, in _websocket_handler
2025-07-05T12:25:12.064858536Z     p = websocket_wait()
2025-07-05T12:25:12.064860197Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:25:12.064861817Z     data = ws.wait()
2025-07-05T12:25:12.064863566Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:25:12.064865206Z     return self.ws.receive()
2025-07-05T12:25:12.064866986Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:25:12.064868677Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:25:12.064870327Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:25:12.064872037Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:25:12.064873697Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:25:12.064875377Z     signaled = self._cond.wait(timeout)
2025-07-05T12:25:12.064877027Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:25:12.064883287Z     waiter.acquire()
2025-07-05T12:25:12.064885077Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:25:12.064886707Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:25:12.064888427Z     sys.exit(1)
2025-07-05T12:25:12.064890097Z     ~~~~~~~~^^^
2025-07-05T12:25:12.064891737Z SystemExit: 1
2025-07-05T12:25:12.064977429Z 127.0.0.1 - - [05/Jul/2025:12:25:12 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=KYmqKW1Hnn4VZofBAAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:25:12.065192994Z [2025-07-05 12:25:12 +0000] [130] [INFO] Worker exiting (pid: 130)
2025-07-05T12:25:13.117264736Z [2025-07-05 12:25:13 +0000] [105] [ERROR] Worker (pid:130) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:25:13.118620636Z [2025-07-05 12:25:13 +0000] [137] [INFO] Booting worker with pid: 137
2025-07-05T12:25:13.512602209Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:25:13.512616639Z Traceback (most recent call last):
2025-07-05T12:25:13.512621349Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:13.512623969Z     self.dialect.do_execute(
2025-07-05T12:25:13.512626349Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.512628789Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:13.512631299Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.512633659Z     )
2025-07-05T12:25:13.512636019Z     ^
2025-07-05T12:25:13.512638449Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:13.51264096Z     cursor.execute(statement, parameters)
2025-07-05T12:25:13.5126435Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.512645989Z psycopg2.OperationalError: SSL SYSCALL error: EOF detected
2025-07-05T12:25:13.51264821Z 
2025-07-05T12:25:13.51265032Z 
2025-07-05T12:25:13.51265272Z The above exception was the direct cause of the following exception:
2025-07-05T12:25:13.51265497Z 
2025-07-05T12:25:13.51265728Z Traceback (most recent call last):
2025-07-05T12:25:13.51265968Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:25:13.51266219Z     response = self.full_dispatch_request()
2025-07-05T12:25:13.51266471Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:25:13.51266704Z     rv = self.handle_user_exception(e)
2025-07-05T12:25:13.51266949Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:25:13.51267192Z     rv = self.dispatch_request()
2025-07-05T12:25:13.51267424Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:25:13.51267643Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:25:13.51267871Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:25:13.51268113Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:25:13.51268357Z     elif not current_user.is_authenticated:
2025-07-05T12:25:13.51268587Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.51268817Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:25:13.512703011Z     obj = instance._get_current_object()
2025-07-05T12:25:13.512705651Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:25:13.512708031Z     return get_name(local())
2025-07-05T12:25:13.512710321Z                     ~~~~~^^
2025-07-05T12:25:13.512712581Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:25:13.512714891Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:25:13.512717261Z                                       ~~~~~~~~~^^
2025-07-05T12:25:13.512719611Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:25:13.512721941Z     current_app.login_manager._load_user()
2025-07-05T12:25:13.512724381Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:25:13.512726801Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:25:13.512729131Z     user = self._user_callback(user_id)
2025-07-05T12:25:13.512731582Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:25:13.512734191Z     return User.query.get(int(user_id))
2025-07-05T12:25:13.512736592Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:25:13.512738992Z   File "<string>", line 2, in get
2025-07-05T12:25:13.512741432Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:25:13.512744022Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:25:13.512746482Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:25:13.512748792Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:25:13.512768052Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.512771132Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:25:13.512773503Z     return self.session._get_impl(
2025-07-05T12:25:13.512776323Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.512778763Z         mapper,
2025-07-05T12:25:13.512781143Z         ^^^^^^^
2025-07-05T12:25:13.512783483Z     ...<6 lines>...
2025-07-05T12:25:13.512785953Z         execution_options=self._execution_options,
2025-07-05T12:25:13.512788493Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.512791073Z     )
2025-07-05T12:25:13.512793463Z     ^
2025-07-05T12:25:13.512795763Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:25:13.512798063Z     return db_load_fn(
2025-07-05T12:25:13.513187472Z         self,
2025-07-05T12:25:13.513191082Z     ...<5 lines>...
2025-07-05T12:25:13.513193832Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.513196302Z     )
2025-07-05T12:25:13.513199172Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:25:13.513201362Z     session.execute(
2025-07-05T12:25:13.513203712Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513206162Z         q,
2025-07-05T12:25:13.513208242Z         ^^
2025-07-05T12:25:13.513210452Z     ...<2 lines>...
2025-07-05T12:25:13.513212862Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.513215282Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513225703Z     )
2025-07-05T12:25:13.513237063Z     ^
2025-07-05T12:25:13.513239943Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:25:13.513242883Z     return self._execute_internal(
2025-07-05T12:25:13.513245303Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513247823Z         statement,
2025-07-05T12:25:13.513250133Z         ^^^^^^^^^^
2025-07-05T12:25:13.513252603Z     ...<4 lines>...
2025-07-05T12:25:13.513255173Z         _add_event=_add_event,
2025-07-05T12:25:13.513257913Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513260834Z     )
2025-07-05T12:25:13.513263363Z     ^
2025-07-05T12:25:13.513266183Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:25:13.513268824Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:25:13.513271414Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513273934Z         self,
2025-07-05T12:25:13.513276364Z         ^^^^^
2025-07-05T12:25:13.513278924Z     ...<4 lines>...
2025-07-05T12:25:13.513281744Z         conn,
2025-07-05T12:25:13.513284634Z         ^^^^^
2025-07-05T12:25:13.513287434Z     )
2025-07-05T12:25:13.513290164Z     ^
2025-07-05T12:25:13.513293284Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:25:13.513296004Z     result = conn.execute(
2025-07-05T12:25:13.513298724Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:25:13.513301644Z     )
2025-07-05T12:25:13.513304604Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:25:13.513307195Z     return meth(
2025-07-05T12:25:13.513309944Z         self,
2025-07-05T12:25:13.513312625Z         distilled_parameters,
2025-07-05T12:25:13.513315205Z         execution_options or NO_OPTIONS,
2025-07-05T12:25:13.513317635Z     )
2025-07-05T12:25:13.513320115Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:25:13.513322785Z     return connection._execute_clauseelement(
2025-07-05T12:25:13.513325265Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513328385Z         self, distilled_params, execution_options
2025-07-05T12:25:13.513331345Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513333705Z     )
2025-07-05T12:25:13.513336565Z     ^
2025-07-05T12:25:13.513339455Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:25:13.513341935Z     ret = self._execute_context(
2025-07-05T12:25:13.513344595Z         dialect,
2025-07-05T12:25:13.513347376Z     ...<8 lines>...
2025-07-05T12:25:13.513350016Z         cache_hit=cache_hit,
2025-07-05T12:25:13.513352936Z     )
2025-07-05T12:25:13.513355736Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:25:13.513358746Z     return self._exec_single_context(
2025-07-05T12:25:13.513361576Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513364156Z         dialect, context, statement, parameters
2025-07-05T12:25:13.513366876Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513369556Z     )
2025-07-05T12:25:13.513372216Z     ^
2025-07-05T12:25:13.513374976Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:25:13.513382796Z     self._handle_dbapi_exception(
2025-07-05T12:25:13.513385516Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513388186Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:25:13.513390846Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513393537Z     )
2025-07-05T12:25:13.513396266Z     ^
2025-07-05T12:25:13.513399086Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:25:13.513401997Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:25:13.513404727Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:13.513407577Z     self.dialect.do_execute(
2025-07-05T12:25:13.513410447Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.513413247Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:13.513416057Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513419027Z     )
2025-07-05T12:25:13.513421567Z     ^
2025-07-05T12:25:13.513424317Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:13.513427027Z     cursor.execute(statement, parameters)
2025-07-05T12:25:13.513429637Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.513432217Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
2025-07-05T12:25:13.513434557Z 
2025-07-05T12:25:13.513437478Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:25:13.513440147Z FROM users 
2025-07-05T12:25:13.513442798Z WHERE users.id = %(pk_1)s]
2025-07-05T12:25:13.513445448Z [parameters: {'pk_1': 1}]
2025-07-05T12:25:13.513447828Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:25:13.61523351Z [2025-07-05 12:25:13 +0000] [137] [ERROR] Error handling request /cart/view
2025-07-05T12:25:13.61524816Z Traceback (most recent call last):
2025-07-05T12:25:13.61525244Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:13.61525577Z     self.dialect.do_execute(
2025-07-05T12:25:13.61526182Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.61526508Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:13.615281851Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615284551Z     )
2025-07-05T12:25:13.615287181Z     ^
2025-07-05T12:25:13.615290431Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:13.615293141Z     cursor.execute(statement, parameters)
2025-07-05T12:25:13.615295681Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615298391Z psycopg2.OperationalError: SSL SYSCALL error: EOF detected
2025-07-05T12:25:13.615300671Z 
2025-07-05T12:25:13.615303011Z 
2025-07-05T12:25:13.615305512Z The above exception was the direct cause of the following exception:
2025-07-05T12:25:13.615318772Z 
2025-07-05T12:25:13.615321452Z Traceback (most recent call last):
2025-07-05T12:25:13.615324332Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:25:13.615326792Z     response = self.full_dispatch_request()
2025-07-05T12:25:13.615329312Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:25:13.615331612Z     rv = self.handle_user_exception(e)
2025-07-05T12:25:13.615333992Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:25:13.615336382Z     rv = self.dispatch_request()
2025-07-05T12:25:13.615339302Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:25:13.615341802Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:25:13.615344242Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:25:13.615346882Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 284, in decorated_view
2025-07-05T12:25:13.615349553Z     elif not current_user.is_authenticated:
2025-07-05T12:25:13.615352182Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615354853Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 318, in __get__
2025-07-05T12:25:13.615357473Z     obj = instance._get_current_object()
2025-07-05T12:25:13.615360273Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/werkzeug/local.py", line 526, in _get_current_object
2025-07-05T12:25:13.615362913Z     return get_name(local())
2025-07-05T12:25:13.615365623Z                     ~~~~~^^
2025-07-05T12:25:13.615368383Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 25, in <lambda>
2025-07-05T12:25:13.615371213Z     current_user = LocalProxy(lambda: _get_user())
2025-07-05T12:25:13.615373573Z                                       ~~~~~~~~~^^
2025-07-05T12:25:13.615376483Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:25:13.615379503Z     current_app.login_manager._load_user()
2025-07-05T12:25:13.615382173Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:25:13.615384983Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:25:13.615387463Z     user = self._user_callback(user_id)
2025-07-05T12:25:13.615390193Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:25:13.615393174Z     return User.query.get(int(user_id))
2025-07-05T12:25:13.615395074Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:25:13.615396683Z   File "<string>", line 2, in get
2025-07-05T12:25:13.615398454Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:25:13.615400114Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:25:13.615401904Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:25:13.615403534Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:25:13.615405254Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615406964Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:25:13.615412894Z     return self.session._get_impl(
2025-07-05T12:25:13.615414594Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615416254Z         mapper,
2025-07-05T12:25:13.615417984Z         ^^^^^^^
2025-07-05T12:25:13.615420244Z     ...<6 lines>...
2025-07-05T12:25:13.615423894Z         execution_options=self._execution_options,
2025-07-05T12:25:13.615425714Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615427374Z     )
2025-07-05T12:25:13.615429034Z     ^
2025-07-05T12:25:13.615430804Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:25:13.615432514Z     return db_load_fn(
2025-07-05T12:25:13.615434244Z         self,
2025-07-05T12:25:13.615435974Z     ...<5 lines>...
2025-07-05T12:25:13.615437615Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.615439284Z     )
2025-07-05T12:25:13.615441035Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:25:13.615442695Z     session.execute(
2025-07-05T12:25:13.615444355Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615446005Z         q,
2025-07-05T12:25:13.615447675Z         ^^
2025-07-05T12:25:13.615449315Z     ...<2 lines>...
2025-07-05T12:25:13.615450965Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.615461465Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615463305Z     )
2025-07-05T12:25:13.615464945Z     ^
2025-07-05T12:25:13.615466655Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:25:13.615468345Z     return self._execute_internal(
2025-07-05T12:25:13.615469965Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615471605Z         statement,
2025-07-05T12:25:13.615473275Z         ^^^^^^^^^^
2025-07-05T12:25:13.615474885Z     ...<4 lines>...
2025-07-05T12:25:13.615476605Z         _add_event=_add_event,
2025-07-05T12:25:13.615478265Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615479905Z     )
2025-07-05T12:25:13.615481556Z     ^
2025-07-05T12:25:13.615483305Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:25:13.615485036Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:25:13.615486696Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615488365Z         self,
2025-07-05T12:25:13.615490066Z         ^^^^^
2025-07-05T12:25:13.615491716Z     ...<4 lines>...
2025-07-05T12:25:13.615493386Z         conn,
2025-07-05T12:25:13.615495136Z         ^^^^^
2025-07-05T12:25:13.615496756Z     )
2025-07-05T12:25:13.615498386Z     ^
2025-07-05T12:25:13.615500026Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:25:13.615501696Z     result = conn.execute(
2025-07-05T12:25:13.615503336Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:25:13.615504986Z     )
2025-07-05T12:25:13.615506666Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:25:13.615508416Z     return meth(
2025-07-05T12:25:13.615510096Z         self,
2025-07-05T12:25:13.615511726Z         distilled_parameters,
2025-07-05T12:25:13.615513546Z         execution_options or NO_OPTIONS,
2025-07-05T12:25:13.615515186Z     )
2025-07-05T12:25:13.615516906Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:25:13.615521716Z     return connection._execute_clauseelement(
2025-07-05T12:25:13.615523436Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615525186Z         self, distilled_params, execution_options
2025-07-05T12:25:13.615526926Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615528557Z     )
2025-07-05T12:25:13.615530186Z     ^
2025-07-05T12:25:13.615531846Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:25:13.615533547Z     ret = self._execute_context(
2025-07-05T12:25:13.615535187Z         dialect,
2025-07-05T12:25:13.615536847Z     ...<8 lines>...
2025-07-05T12:25:13.615538527Z         cache_hit=cache_hit,
2025-07-05T12:25:13.615540137Z     )
2025-07-05T12:25:13.615541787Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:25:13.615543447Z     return self._exec_single_context(
2025-07-05T12:25:13.615545147Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615546747Z         dialect, context, statement, parameters
2025-07-05T12:25:13.615548367Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615549987Z     )
2025-07-05T12:25:13.615551607Z     ^
2025-07-05T12:25:13.615553277Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:25:13.615554917Z     self._handle_dbapi_exception(
2025-07-05T12:25:13.615556517Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615558117Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:25:13.615559757Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615561397Z     )
2025-07-05T12:25:13.615563007Z     ^
2025-07-05T12:25:13.615564717Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:25:13.615566387Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:25:13.615568097Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:13.615569767Z     self.dialect.do_execute(
2025-07-05T12:25:13.615571398Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615573898Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:13.615576838Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615579528Z     )
2025-07-05T12:25:13.615582128Z     ^
2025-07-05T12:25:13.615583518Z 127.0.0.1 - - [05/Jul/2025:12:25:13 +0000] "GET /cart/view HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:25:13.615584738Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:13.615588238Z     cursor.execute(statement, parameters)
2025-07-05T12:25:13.615590598Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615596868Z sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
2025-07-05T12:25:13.615600788Z 
2025-07-05T12:25:13.615605078Z [SQL: SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password_hash AS users_password_hash, users.first_name AS users_first_name, users.last_name AS users_last_name, users.phone AS users_phone, users.address AS users_address, users.avatar AS users_avatar, users.is_admin AS users_is_admin, users.created_at AS users_created_at 
2025-07-05T12:25:13.615611678Z FROM users 
2025-07-05T12:25:13.615614288Z WHERE users.id = %(pk_1)s]
2025-07-05T12:25:13.615616859Z [parameters: {'pk_1': 1}]
2025-07-05T12:25:13.615619379Z (Background on this error at: https://sqlalche.me/e/20/e3q8)
2025-07-05T12:25:13.615621548Z 
2025-07-05T12:25:13.615623979Z During handling of the above exception, another exception occurred:
2025-07-05T12:25:13.615626039Z 
2025-07-05T12:25:13.615628349Z Traceback (most recent call last):
2025-07-05T12:25:13.615630959Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:25:13.615633419Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:25:13.615635669Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615660609Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:25:13.615663669Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:25:13.61566612Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:25:13.61566879Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:25:13.61567143Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.61567395Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:25:13.61567634Z     return super().__call__(environ, start_response)
2025-07-05T12:25:13.61567847Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.61568089Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 74, in __call__
2025-07-05T12:25:13.61568333Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:25:13.61568584Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.61568807Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1514, in wsgi_app
2025-07-05T12:25:13.61569049Z     response = self.handle_exception(e)
2025-07-05T12:25:13.6156929Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 860, in handle_exception
2025-07-05T12:25:13.61569529Z     server_error = self.ensure_sync(handler)(server_error)
2025-07-05T12:25:13.61569764Z   File "/opt/render/project/src/app.py", line 65, in internal_server_error
2025-07-05T12:25:13.61570023Z     return render_template('500.html'), 500
2025-07-05T12:25:13.61570265Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-07-05T12:25:13.61570527Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 150, in render_template
2025-07-05T12:25:13.61570779Z     return _render(app, template, context)
2025-07-05T12:25:13.615710261Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/templating.py", line 127, in _render
2025-07-05T12:25:13.615712791Z     app.update_template_context(context)
2025-07-05T12:25:13.615715291Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:25:13.615718121Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 530, in update_template_context
2025-07-05T12:25:13.615720611Z     context.update(self.ensure_sync(func)())
2025-07-05T12:25:13.615723161Z                    ~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:25:13.615725621Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 405, in _user_context_processor
2025-07-05T12:25:13.615728031Z     return dict(current_user=_get_user())
2025-07-05T12:25:13.615740071Z                              ~~~~~~~~~^^
2025-07-05T12:25:13.615742721Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 370, in _get_user
2025-07-05T12:25:13.615745191Z     current_app.login_manager._load_user()
2025-07-05T12:25:13.615747651Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:25:13.615750042Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/login_manager.py", line 364, in _load_user
2025-07-05T12:25:13.615752551Z     user = self._user_callback(user_id)
2025-07-05T12:25:13.615755032Z   File "/opt/render/project/src/models/user.py", line 42, in load_user
2025-07-05T12:25:13.615757542Z     return User.query.get(int(user_id))
2025-07-05T12:25:13.615760112Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
2025-07-05T12:25:13.615762662Z   File "<string>", line 2, in get
2025-07-05T12:25:13.615765132Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 386, in warned
2025-07-05T12:25:13.615767592Z     return fn(*args, **kwargs)  # type: ignore[no-any-return]
2025-07-05T12:25:13.615770092Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1126, in get
2025-07-05T12:25:13.615772652Z     return self._get_impl(ident, loading.load_on_pk_identity)
2025-07-05T12:25:13.615775172Z            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615777792Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 1135, in _get_impl
2025-07-05T12:25:13.615780312Z     return self.session._get_impl(
2025-07-05T12:25:13.615782782Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615785312Z         mapper,
2025-07-05T12:25:13.615787702Z         ^^^^^^^
2025-07-05T12:25:13.615790062Z     ...<6 lines>...
2025-07-05T12:25:13.615792583Z         execution_options=self._execution_options,
2025-07-05T12:25:13.615795083Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615797612Z     )
2025-07-05T12:25:13.615830303Z     ^
2025-07-05T12:25:13.615833203Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3873, in _get_impl
2025-07-05T12:25:13.615835733Z     return db_load_fn(
2025-07-05T12:25:13.615838253Z         self,
2025-07-05T12:25:13.615840804Z     ...<5 lines>...
2025-07-05T12:25:13.615843213Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.615845554Z     )
2025-07-05T12:25:13.615848084Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/loading.py", line 694, in load_on_pk_identity
2025-07-05T12:25:13.615850454Z     session.execute(
2025-07-05T12:25:13.615853014Z     ~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615855524Z         q,
2025-07-05T12:25:13.615857894Z         ^^
2025-07-05T12:25:13.615860434Z     ...<2 lines>...
2025-07-05T12:25:13.615862974Z         bind_arguments=bind_arguments,
2025-07-05T12:25:13.615865434Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615867734Z     )
2025-07-05T12:25:13.615870174Z     ^
2025-07-05T12:25:13.615872824Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:25:13.615875294Z     return self._execute_internal(
2025-07-05T12:25:13.615877724Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615890695Z         statement,
2025-07-05T12:25:13.615893245Z         ^^^^^^^^^^
2025-07-05T12:25:13.615895805Z     ...<4 lines>...
2025-07-05T12:25:13.615898555Z         _add_event=_add_event,
2025-07-05T12:25:13.615905745Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615908265Z     )
2025-07-05T12:25:13.615910685Z     ^
2025-07-05T12:25:13.615913255Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:25:13.615915725Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:25:13.615918455Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615920825Z         self,
2025-07-05T12:25:13.615923275Z         ^^^^^
2025-07-05T12:25:13.615925655Z     ...<4 lines>...
2025-07-05T12:25:13.615928086Z         conn,
2025-07-05T12:25:13.615930486Z         ^^^^^
2025-07-05T12:25:13.615933016Z     )
2025-07-05T12:25:13.615935556Z     ^
2025-07-05T12:25:13.615940046Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:25:13.615942486Z     result = conn.execute(
2025-07-05T12:25:13.615944876Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:25:13.615947316Z     )
2025-07-05T12:25:13.615949836Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:25:13.615952186Z     return meth(
2025-07-05T12:25:13.615954846Z         self,
2025-07-05T12:25:13.615957146Z         distilled_parameters,
2025-07-05T12:25:13.615959616Z         execution_options or NO_OPTIONS,
2025-07-05T12:25:13.615962036Z     )
2025-07-05T12:25:13.615964506Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:25:13.615967136Z     return connection._execute_clauseelement(
2025-07-05T12:25:13.615969647Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:13.615972027Z         self, distilled_params, execution_options
2025-07-05T12:25:13.615974487Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:13.615976947Z     )
2025-07-05T12:25:13.615979327Z     ^
2025-07-05T12:25:13.615981857Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:25:13.615984337Z     ret = self._execute_context(
2025-07-05T12:25:13.615986817Z         dialect,
2025-07-05T12:25:13.615989277Z     ...<8 lines>...
2025-07-05T12:25:13.615991777Z         cache_hit=cache_hit,
2025-07-05T12:25:13.615994207Z     )
2025-07-05T12:25:13.615996707Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1809, in _execute_context
2025-07-05T12:25:13.615999097Z     conn = self._revalidate_connection()
2025-07-05T12:25:13.616001577Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 675, in _revalidate_connection
2025-07-05T12:25:13.616004027Z     self._invalid_transaction()
2025-07-05T12:25:13.616006477Z     ~~~~~~~~~~~~~~~~~~~~~~~~~^^
2025-07-05T12:25:13.616009007Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 665, in _invalid_transaction
2025-07-05T12:25:13.616011517Z     raise exc.PendingRollbackError(
2025-07-05T12:25:13.616014028Z     ...<4 lines>...
2025-07-05T12:25:13.616016537Z     )
2025-07-05T12:25:13.616022658Z sqlalchemy.exc.PendingRollbackError: Can't reconnect until invalid transaction is rolled back.  Please rollback() fully before proceeding (Background on this error at: https://sqlalche.me/e/20/8s2b)
2025-07-05T12:25:18.310237208Z ERROR:app:Exception on /cart/view [GET]
2025-07-05T12:25:18.3102814Z Traceback (most recent call last):
2025-07-05T12:25:18.31028581Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:18.31028994Z     self.dialect.do_execute(
2025-07-05T12:25:18.31029271Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.31029586Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:18.31029857Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.31030135Z     )
2025-07-05T12:25:18.31030391Z     ^
2025-07-05T12:25:18.31030742Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:18.31030986Z     cursor.execute(statement, parameters)
2025-07-05T12:25:18.31031246Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.31031586Z psycopg2.errors.UndefinedColumn: column cart_items.user_id does not exist
2025-07-05T12:25:18.31031871Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:25:18.31032171Z                                                ^
2025-07-05T12:25:18.310323941Z 
2025-07-05T12:25:18.310325881Z 
2025-07-05T12:25:18.310328061Z The above exception was the direct cause of the following exception:
2025-07-05T12:25:18.310330131Z 
2025-07-05T12:25:18.310332311Z Traceback (most recent call last):
2025-07-05T12:25:18.310335021Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1511, in wsgi_app
2025-07-05T12:25:18.310337561Z     response = self.full_dispatch_request()
2025-07-05T12:25:18.310340361Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 919, in full_dispatch_request
2025-07-05T12:25:18.310342981Z     rv = self.handle_user_exception(e)
2025-07-05T12:25:18.310345821Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 917, in full_dispatch_request
2025-07-05T12:25:18.310348381Z     rv = self.dispatch_request()
2025-07-05T12:25:18.310350861Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 902, in dispatch_request
2025-07-05T12:25:18.310353381Z     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
2025-07-05T12:25:18.310355931Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
2025-07-05T12:25:18.310358431Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_login/utils.py", line 290, in decorated_view
2025-07-05T12:25:18.310360901Z     return current_app.ensure_sync(func)(*args, **kwargs)
2025-07-05T12:25:18.310363331Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310365622Z   File "/opt/render/project/src/routes/cart.py", line 58, in view_cart
2025-07-05T12:25:18.310368031Z     cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
2025-07-05T12:25:18.310370262Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2704, in all
2025-07-05T12:25:18.310372522Z     return self._iter().all()  # type: ignore
2025-07-05T12:25:18.310375482Z            ~~~~~~~~~~^^
2025-07-05T12:25:18.310377812Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/query.py", line 2857, in _iter
2025-07-05T12:25:18.310380112Z     result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
2025-07-05T12:25:18.310382312Z                                                   ~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310384532Z         statement,
2025-07-05T12:25:18.310386912Z         ^^^^^^^^^^
2025-07-05T12:25:18.310392542Z         params,
2025-07-05T12:25:18.310394862Z         ^^^^^^^
2025-07-05T12:25:18.310397152Z         execution_options={"_sa_orm_load_options": self.load_options},
2025-07-05T12:25:18.310399372Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310401602Z     )
2025-07-05T12:25:18.310403802Z     ^
2025-07-05T12:25:18.310406132Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-07-05T12:25:18.310408482Z     return self._execute_internal(
2025-07-05T12:25:18.310410723Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310413083Z         statement,
2025-07-05T12:25:18.310415303Z         ^^^^^^^^^^
2025-07-05T12:25:18.310417692Z     ...<4 lines>...
2025-07-05T12:25:18.310419943Z         _add_event=_add_event,
2025-07-05T12:25:18.310422153Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310424333Z     )
2025-07-05T12:25:18.310426523Z     ^
2025-07-05T12:25:18.310428853Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2251, in _execute_internal
2025-07-05T12:25:18.310431053Z     result: Result[Any] = compile_state_cls.orm_execute_statement(
2025-07-05T12:25:18.310433283Z                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310435513Z         self,
2025-07-05T12:25:18.310437683Z         ^^^^^
2025-07-05T12:25:18.310439833Z     ...<4 lines>...
2025-07-05T12:25:18.310442023Z         conn,
2025-07-05T12:25:18.310444263Z         ^^^^^
2025-07-05T12:25:18.310446453Z     )
2025-07-05T12:25:18.310448583Z     ^
2025-07-05T12:25:18.310450823Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/context.py", line 306, in orm_execute_statement
2025-07-05T12:25:18.310453053Z     result = conn.execute(
2025-07-05T12:25:18.310455304Z         statement, params or {}, execution_options=execution_options
2025-07-05T12:25:18.310457504Z     )
2025-07-05T12:25:18.310459784Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1415, in execute
2025-07-05T12:25:18.310462024Z     return meth(
2025-07-05T12:25:18.310464234Z         self,
2025-07-05T12:25:18.310466454Z         distilled_parameters,
2025-07-05T12:25:18.310468704Z         execution_options or NO_OPTIONS,
2025-07-05T12:25:18.310470874Z     )
2025-07-05T12:25:18.310473054Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 523, in _execute_on_connection
2025-07-05T12:25:18.310475384Z     return connection._execute_clauseelement(
2025-07-05T12:25:18.310477584Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310480054Z         self, distilled_params, execution_options
2025-07-05T12:25:18.310505054Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310507705Z     )
2025-07-05T12:25:18.310509955Z     ^
2025-07-05T12:25:18.310512185Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1637, in _execute_clauseelement
2025-07-05T12:25:18.310514475Z     ret = self._execute_context(
2025-07-05T12:25:18.310516695Z         dialect,
2025-07-05T12:25:18.310518895Z     ...<8 lines>...
2025-07-05T12:25:18.310521125Z         cache_hit=cache_hit,
2025-07-05T12:25:18.310523385Z     )
2025-07-05T12:25:18.310525685Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
2025-07-05T12:25:18.310527975Z     return self._exec_single_context(
2025-07-05T12:25:18.310533985Z            ~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310536255Z         dialect, context, statement, parameters
2025-07-05T12:25:18.310538435Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310540665Z     )
2025-07-05T12:25:18.310542905Z     ^
2025-07-05T12:25:18.310545275Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1982, in _exec_single_context
2025-07-05T12:25:18.3107524Z     self._handle_dbapi_exception(
2025-07-05T12:25:18.31075668Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.31075943Z         e, str_statement, effective_parameters, cursor, context
2025-07-05T12:25:18.3107618Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.31076437Z     )
2025-07-05T12:25:18.310766971Z     ^
2025-07-05T12:25:18.310769871Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2351, in _handle_dbapi_exception
2025-07-05T12:25:18.310772371Z     raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
2025-07-05T12:25:18.310774761Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1963, in _exec_single_context
2025-07-05T12:25:18.310777351Z     self.dialect.do_execute(
2025-07-05T12:25:18.310779781Z     ~~~~~~~~~~~~~~~~~~~~~~~^
2025-07-05T12:25:18.310782421Z         cursor, str_statement, effective_parameters, context
2025-07-05T12:25:18.310785071Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310787621Z     )
2025-07-05T12:25:18.310790301Z     ^
2025-07-05T12:25:18.310792821Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 943, in do_execute
2025-07-05T12:25:18.310795191Z     cursor.execute(statement, parameters)
2025-07-05T12:25:18.310797631Z     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:18.310836642Z sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column cart_items.user_id does not exist
2025-07-05T12:25:18.310839282Z LINE 1: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS...
2025-07-05T12:25:18.310841732Z                                                ^
2025-07-05T12:25:18.310843892Z 
2025-07-05T12:25:18.310848172Z [SQL: SELECT cart_items.id AS cart_items_id, cart_items.user_id AS cart_items_user_id, cart_items.product_id AS cart_items_product_id, cart_items.quantity AS cart_items_quantity, cart_items.size AS cart_items_size, cart_items.color AS cart_items_color, cart_items.created_at AS cart_items_created_at, cart_items.updated_at AS cart_items_updated_at 
2025-07-05T12:25:18.310851032Z FROM cart_items 
2025-07-05T12:25:18.310853652Z WHERE cart_items.user_id = %(user_id_1)s]
2025-07-05T12:25:18.310856182Z [parameters: {'user_id_1': 1}]
2025-07-05T12:25:18.310858853Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-07-05T12:25:18.511337397Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /cart/view HTTP/1.1" 500 20217 "https://unicornbrand.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.647270648Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/js/libs/SplitType.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.647287399Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/css/style.css HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.651489443Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/js/main.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.651988675Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.653504169Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/js/libs/ScrollTrigger.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.679447993Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/js/libs/gsap.min.js HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.915960209Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /static/assets/musics/Ordinary%20Girl%20-%20Ahv.mp3 HTTP/1.1" 206 9899674 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:18.926578658Z 127.0.0.1 - - [05/Jul/2025:12:25:18 +0000] "GET /api/cart/count HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:19.017900335Z 127.0.0.1 - - [05/Jul/2025:12:25:19 +0000] "POST /api/cart/sync HTTP/1.1" 404 20202 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:19.019339777Z 127.0.0.1 - - [05/Jul/2025:12:25:19 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZ5A9 HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:19.217626022Z 127.0.0.1 - - [05/Jul/2025:12:25:19 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQZ5Fn&sid=eWTIcu6J7mBwzWU-AAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:19.235760121Z 127.0.0.1 - - [05/Jul/2025:12:25:19 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZ5Fp&sid=eWTIcu6J7mBwzWU-AAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:50.2223254Z [2025-07-05 12:25:50 +0000] [105] [CRITICAL] WORKER TIMEOUT (pid:137)
2025-07-05T12:25:50.226119635Z [2025-07-05 12:25:50 +0000] [137] [ERROR] Error handling request /socket.io/?EIO=4&transport=websocket&sid=eWTIcu6J7mBwzWU-AAAA
2025-07-05T12:25:50.226136295Z Traceback (most recent call last):
2025-07-05T12:25:50.226141715Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 134, in handle
2025-07-05T12:25:50.226146395Z     self.handle_request(listener, req, client, addr)
2025-07-05T12:25:50.226150106Z     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226153806Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/sync.py", line 177, in handle_request
2025-07-05T12:25:50.226157566Z     respiter = self.wsgi(environ, resp.start_response)
2025-07-05T12:25:50.226162056Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask/app.py", line 1536, in __call__
2025-07-05T12:25:50.226178016Z     return self.wsgi_app(environ, start_response)
2025-07-05T12:25:50.226180496Z            ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226182756Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/flask_socketio/__init__.py", line 42, in __call__
2025-07-05T12:25:50.226185056Z     return super().__call__(environ, start_response)
2025-07-05T12:25:50.226187727Z            ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226190416Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/middleware.py", line 63, in __call__
2025-07-05T12:25:50.226193296Z     return self.engineio_app.handle_request(environ, start_response)
2025-07-05T12:25:50.226195637Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226197867Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/socketio/server.py", line 434, in handle_request
2025-07-05T12:25:50.226200267Z     return self.eio.handle_request(environ, start_response)
2025-07-05T12:25:50.226202427Z            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226204697Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/server.py", line 286, in handle_request
2025-07-05T12:25:50.226206987Z     packets = socket.handle_get_request(
2025-07-05T12:25:50.226210037Z         environ, start_response)
2025-07-05T12:25:50.226212347Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 92, in handle_get_request
2025-07-05T12:25:50.226214777Z     return getattr(self, '_upgrade_' + transport)(environ,
2025-07-05T12:25:50.226217097Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
2025-07-05T12:25:50.226219447Z                                                   start_response)
2025-07-05T12:25:50.226225257Z                                                   ^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226227857Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 151, in _upgrade_websocket
2025-07-05T12:25:50.226230577Z     return ws(environ, start_response)
2025-07-05T12:25:50.226233368Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 15, in __call__
2025-07-05T12:25:50.226236057Z     ret = self.app(self)
2025-07-05T12:25:50.226238608Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 183, in _websocket_handler
2025-07-05T12:25:50.226240958Z     pkt = websocket_wait()
2025-07-05T12:25:50.226243358Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/socket.py", line 156, in websocket_wait
2025-07-05T12:25:50.226248838Z     data = ws.wait()
2025-07-05T12:25:50.226251278Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/engineio/async_drivers/_websocket_wsgi.py", line 32, in wait
2025-07-05T12:25:50.226253558Z     return self.ws.receive()
2025-07-05T12:25:50.226255808Z            ~~~~~~~~~~~~~~~^^
2025-07-05T12:25:50.226258048Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/simple_websocket/ws.py", line 96, in receive
2025-07-05T12:25:50.226260388Z     if not self.event.wait(timeout=timeout):
2025-07-05T12:25:50.226262588Z            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
2025-07-05T12:25:50.226264908Z   File "/usr/local/lib/python3.13/threading.py", line 659, in wait
2025-07-05T12:25:50.226267088Z     signaled = self._cond.wait(timeout)
2025-07-05T12:25:50.226269348Z   File "/usr/local/lib/python3.13/threading.py", line 359, in wait
2025-07-05T12:25:50.226271688Z     waiter.acquire()
2025-07-05T12:25:50.226273938Z     ~~~~~~~~~~~~~~^^
2025-07-05T12:25:50.226282069Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 204, in handle_abort
2025-07-05T12:25:50.226284439Z     sys.exit(1)
2025-07-05T12:25:50.226286889Z     ~~~~~~~~^^^
2025-07-05T12:25:50.226289059Z SystemExit: 1
2025-07-05T12:25:50.226302769Z 127.0.0.1 - - [05/Jul/2025:12:25:50 +0000] "GET /socket.io/?EIO=4&transport=websocket&sid=eWTIcu6J7mBwzWU-AAAA HTTP/1.1" 500 0 "-" "-"
2025-07-05T12:25:50.226511334Z [2025-07-05 12:25:50 +0000] [137] [INFO] Worker exiting (pid: 137)
2025-07-05T12:25:51.31518987Z [2025-07-05 12:25:51 +0000] [105] [ERROR] Worker (pid:137) was sent SIGKILL! Perhaps out of memory?
2025-07-05T12:25:51.318944855Z [2025-07-05 12:25:51 +0000] [141] [INFO] Booting worker with pid: 141
2025-07-05T12:25:51.410346753Z Invalid session eWTIcu6J7mBwzWU-AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:25:51.410370523Z ERROR:engineio.server:Invalid session eWTIcu6J7mBwzWU-AAAA (further occurrences of this error will be logged with level INFO)
2025-07-05T12:25:51.411190612Z 127.0.0.1 - - [05/Jul/2025:12:25:51 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZ5Jl&sid=eWTIcu6J7mBwzWU-AAAA HTTP/1.1" 400 38 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:51.422827054Z 127.0.0.1 - - [05/Jul/2025:12:25:51 +0000] "GET /static/assets/images/unicorn.png HTTP/1.1" 304 0 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:53.038491547Z 127.0.0.1 - - [05/Jul/2025:12:25:53 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZDWb HTTP/1.1" 200 118 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:53.149844535Z 127.0.0.1 - - [05/Jul/2025:12:25:53 +0000] "POST /socket.io/?EIO=4&transport=polling&t=PVQZDYP&sid=uqvq_nAU6a40DlOtAAAA HTTP/1.1" 200 2 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:25:53.16563293Z 127.0.0.1 - - [05/Jul/2025:12:25:53 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZDYR&sid=uqvq_nAU6a40DlOtAAAA HTTP/1.1" 200 32 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
2025-07-05T12:26:18.038573859Z 127.0.0.1 - - [05/Jul/2025:12:26:18 +0000] "GET /socket.io/?EIO=4&transport=polling&t=PVQZDaL&sid=uqvq_nAU6a40DlOtAAAA HTTP/1.1" 200 1 "https://unicornbrand.onrender.com/cart/view" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"