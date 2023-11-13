import socket

HOST = "127.0.0.1"
PORT = 8088

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("please input packet you want to send")
    d = input()
    s.sendto(d.encode(), (HOST, PORT))
    data, addr = s.recvfrom(1024)

print(f"recv from server{str(addr)} data: {data.decode()}")
