import socket
import struct

HOST = "127.0.0.1"
PORT = 8088


def create_icmp_request():
    packet_type = 8  # ICMP Echo Request
    code = 0
    checksum = 0
    packet_id = 12345
    sequence = 1
    header = struct.pack("bbHHhsssss", packet_type, code, checksum, packet_id, sequence, b"h", b"e", b"l", b"l", b"o")
    checksum = calculate_checksum(header)
    packet = struct.pack("bbHHhsssss", packet_type, code, checksum, packet_id, sequence, b"h", b"e", b"l", b"l", b"o")
    return packet


def calculate_checksum(data):
    checksum = 0
    count_to = (len(data) // 2) * 2

    for count in range(0, count_to, 2):
        this_val = data[count + 1] * 256 + data[count]
        checksum += this_val
        checksum &= 0xffffffff

    if count_to < len(data):
        checksum += data[len(data) - 1]
        checksum &= 0xffffffff

    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += (checksum >> 16)
    checksum = ~checksum & 0xffff

    return checksum


def icmp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
        s.setsockopt(socket.SOL_IP, socket.IP_TTL, 64)
        packet = create_icmp_request()
        s.sendto(packet, (HOST, PORT))
        data, addr = s.recvfrom(1024)
        print(f"recv from server data: {data[28:].decode('utf-8')}")


if __name__ == "__main__":
    icmp_client()
