import socket

HOST = "127.0.0.1"
PORT = 8088

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("please input packet you want to send")
    d = input()
    s.send(d.encode())
    data = s.recv(1024)
    s.close()

print(f"recv from server data: {data.decode()}")

