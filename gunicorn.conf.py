import multiprocessing

bind = "unix:/home/parallels/myproject/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120
keepalive = 5
errorlog = "/home/parallels/myproject/logs/gunicorn-error.log"
accesslog = "/home/parallels/myproject/logs/gunicorn-access.log"
loglevel = "info"
limit_request_line = 8190
limit_request_field_size = 8190

