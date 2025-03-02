import socket
from concurrent.futures import ThreadPoolExecutor
def scan(p):
    with socket.socket() as s:
        if not s.connect_ex(("127.0.0.1", p)): print(p, "open")
with ThreadPoolExecutor(100) as e: e.map(scan, range(1, 1024))
