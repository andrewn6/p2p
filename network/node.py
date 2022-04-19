# The server class is a class that creates a server that listens for connections on a given port
from collections import defaultdict
from concurrent.futures import thread
import socket
import threading
import sys

class Server:
    def __init__(self, host, port=8080, v='P2P'):
        self.host = host
        self.port = port
        self.v = v
        self.peers = defaultdict(set)
        self.lock = threading.Lock()

    def start(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((self.HOST, self.PORT))
            self.s.listen(5)
            print('Server %s is listening port %s' % (self.v, self.port))

            while True:
                soc, addr = self.s.accept()
                print('%s:%s connected' % (addr[0], addr[1]))
                thread = threading.Thread(target=self.handler, args=(soc, addr))

                thread.start()
                
        except:
            pass
               