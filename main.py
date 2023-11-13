import os
import socket

HOST = "127.0.0.1"
PORT = 8088


def tcpServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"server start at {HOST}:{PORT} type tcp")
    while True:
        conn, addr = s.accept()
        print(f"connect by {addr}")
        while True:
            data = conn.recv(1024)
            if len(data) == 0:
                conn.close()
                print(f"server close...")
                break
            print(f"recv from client: {data.decode()}")
            echodata = data.decode()
            conn.sendall(echodata.encode())


def udpServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print(f"server start at {HOST}:{PORT} type udp")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"connect by {addr}")
        print(f"recv from client:{data.decode()}")
        echodata = data.decode()
        s.sendto(echodata.encode(), addr)


def icmpServer():
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
        print(f"server start at {HOST}:{PORT} type icmp")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"connect by {addr}")
            print(f"recv from client:{data[28:].decode('utf-8')}")
            s.sendto(data, (HOST, PORT))


def main():
    while True:
        print("please enter what type you want to echo")
        print('''
              1. tcp echo server
              2. udp echo server
              3. icmp echo server
              ''')
        chose = int(input())
        if chose == 1:
            tcpServer()
        elif chose == 2:
            udpServer()
        elif chose == 3:
            icmpServer()
        else:
            print("have some wrong!")
            break


if __name__ == '__main__':
    main()
