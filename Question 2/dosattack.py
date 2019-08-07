from scapy.all import *

src = ["127.0.0.1", "80"]
dst = ["127.0.0.2", "12000"]
i = 1

while True:
    IP1 = IP(source_IP = src[0], destination = dst[0])
    TCP1 = TCP(srcport = src[1], dstport = dst[1])
    pkt = IP1 / TCP1
    send(pkt, inter = 0.001)
    print("packet sent ", i)
    i += 1

