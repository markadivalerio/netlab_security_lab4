#! /usr/bin/env python
import socket
from scapy.all import *
from time import sleep

sport = random.randint(54800, 54899)
#addr = "www.baiwanzhan.com"
addr = "106.119.182.141"
dport = 80

def handshake():
    syn_pkg = IP(dst=addr)/TCP(sport=sport, dport=dport, flags='S', seq=1000)
    #syn_ack = sr1(syn_pkg)
    #seq = syn_ack[0][0][-1][TCP].seq
    #ack = syn_ack[0][0][-1][TCP].ack
    syn_ack = sr1(syn_pkg)
    seq = syn_ack[TCP].seq
    ack = syn_ack[TCP].ack
    ack_pkg = IP(dst=addr)/TCP(dport=dport, flags='A', seq=ack, ack=seq)
    send(ack_pkg)
    return (ack, seq)

#def send_req(prev_ack, data):
#    req_pkg = IP(dst=addr)/TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / data

#getStr = "GET / HTTP/1.1\r\nHost: www.baiwanzhan.com\r\n\r\n"
'''
search_a="%E6%B3%95"
search_b="%E8%BD%AE"
search = search_a + search_b
getStr = "GET /service/site/search.aspx?query=%E6%B3%95%E8%BD%AE HTTP/1.1\r\n"
partialStr1 = "GET /service/site/search.aspx?query=%E6%B3%95"
partialStr2 = "%E8%BD%AE HTTP/1.1\r\n"
request = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
reply = sr1(request)
print(reply)

req1 = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / partialStr1
#req2 = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / partialStr2

reply1 = sr1(req1)
reply1.show()
reply2 = sr1(req2)
reply2.show()
'''

def main():
    ack, seq = handshake()
    print(ack)
    print(seq)


if __name__ == "__main__":
    main()
