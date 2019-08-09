import socket
from scapy.all import *

syn = IP(dst="www.baiwanzhan.com")/TCP(dport=80, flags='S')
print(syn)
syn_ack = sr1(syn)
print(syn_ack)
getStr = "GET / HTTP/1.1\r\nHost: www.baiwanzhan.com\r\n\r\n"
search_a="%E6%B3%95"
search_b="%E8%BD%AE"
search = search_a + search_b
request = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP.dport], seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
reply = sr1(request)
print(reply)
