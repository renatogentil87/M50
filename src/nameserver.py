#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'
PORT = 53

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    while True:
        data, addr = sock.recvfrom(512)
        response = dns_response(data)
        sock.sendto(response, addr)

def dns_response(data):
    TransactionID = data[0:2]
    TID = ''
    for byte in TransactionID:
        TID +=hex(byte)[2:]
    print(TID)

        
if __name__ == "__main__":
        main()