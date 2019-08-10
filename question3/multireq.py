#! /usr/bin/env python
import socket
from scapy.all import *
from time import sleep
import requests

sport = random.randint(54800, 54899)
#addr = "www.baiwanzhan.com"
ip = IP(dst="www.google.com")
#ip = IP(dst="www.baiwanzhan.com")
addr = "106.119.182.141"
dport = 80

def handshake():
    syn_pkg = ip/TCP(sport=sport, dport=dport, flags='S', seq=1000)
    #syn_ack = sr1(syn_pkg)
    #seq = syn_ack[0][0][-1][TCP].seq
    #ack = syn_ack[0][0][-1][TCP].ack
    print('HERE 1')
    syn_ack = sr1(syn_pkg)
    print('HERE 2')
    seq = syn_ack[TCP].seq+1
    ack = syn_ack[TCP].ack
    ack_pkg = ip/TCP(dport=dport, flags='A', seq=ack, ack=seq)
    print('HERE 3')
    send(ack_pkg)
    print('HERE 4')
    return (ack, seq)

#def send_req(prev_ack, data):
#    req_pkg = IP(dst=addr)/TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / data

#getStr = "GET / HTTP/1.1\r\nHost: www.baiwanzhan.com\r\n\r\n"

search_a="%E6%B3%95"
search_b="%E8%BD%AE"
search = search_a + search_b
getStr = "GET /service/site/search.aspx?query=%E6%B3%95%E8%BD%AE HTTP/1.1\r\n"
getStr1 = "GET /service/site/search.aspx?query=he"
getStr2 = "llo HTTP/1.1\r\n"
getStr3 = "GET /service/site/search.aspx?query=hello HTTP/1.1\r\n"
partialStr1 = "GET /service/site/search.aspx?query=%E6%B3%95"
partialStr2 = "%E8%BD%AE HTTP/1.1\r\n"
#request = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
#reply = sr1(request)
#print(reply)

#req1 = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / partialStr1
#req2 = IP(dst='www.baiwanzhan.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / partialStr2

#reply1 = sr1(req1)
#reply1.show()
#reply2 = sr1(req2)
#reply2.show()

def try2():
    r = requests.get("http://www.baiwanzhan.com/service/site/search.aspx?query=hello")
    print(r.status_code)
    print(r.headers)
    print(r.content)

def main():
#    try2()
#    return

    ack, seq = handshake()
    print(ack)
    print(seq)
    req = ip / TCP(dport=dport, sport=sport, seq=ack, ack=seq, flags='PA') / getStr3
    res = sr(req) 
#    req1 = ip / TCP(dport=dport, sport=sport, seq=ack, ack=seq, flags='PA') / getStr1
#    res1 = sr1(req1)
#    seq1 = res1[TCP].seq+1
#    ack1 = res1[TCP].ack
#    req2 = ip / TCP(dport=dport, sport=sport, seq=ack1, ack=seq1, flags='PA') / getStr2
#    send(req2)
    
    #print('HERE 5')
    #res = send([req1,req2])
    #print('HERE 6')
    #print(ack)
    #print(seq)
    #print(res)


if __name__ == "__main__":
    main()
