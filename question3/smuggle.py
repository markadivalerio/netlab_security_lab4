#! /usr/bin/env python3
import socket

host = "www.baiwanzhan.com"
port = 80


def main():
    #connect
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    #make requests
    reqs = ["GET /service/site/search.aspx?query=%E6%B3%95",
        "%E8%BD%AE HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)]
    requests = [info.encode() for info in reqs]
    responses = []
    for req in requests:
        client.send(req)
        resp = client.recv(4096)
        responses.append(repr(resp))

if __name__ == "__main__":
    main()
