#!/usr/bin/env python3
import socket


class ResponseConstructor():

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 53
        self.buffer = 512
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((self.host, self.port))

        print("UDP server up and listening")

        # Listen for incoming queries
        while True:
            self.bytesAddressPair = self.UDPServerSocket.recvfrom(self.buffer)
            self.dnsquery = self.bytesAddressPair[0]
            self.address = self.bytesAddressPair[1]


            self.TransactionId = self.dnsquery[0:2]
            self.TID = ''
            for byte in self.TransactionId:
                self.TID += hex(byte)[2:]
                print(self.TID)


if __name__ == "__main__":
    ResponseConstructor()
