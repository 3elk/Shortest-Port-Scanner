import socket
from concurrent.futures import ThreadPoolExecutor
def scan(p):
    with socket.socket() as s:
        if not s.connect_ex(("IP ADDRESS", p)): print(p, "is open") # change where it says "IP ADDRESS"
with ThreadPoolExecutor(100) as e: e.map(scan, range(START-PORT, END-PORT)) # change the "START-PORT" and "END-PORT" values
