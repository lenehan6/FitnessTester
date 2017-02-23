import threading
import socket
import sys

class Connection(threading.Thread):

    def __init__(self, ip, port, socket, jobs):
        self._jobs = jobs;
        self._buf = [];
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New thread started for "+ip+":"+str(port)

    def run(self):
        try:
            print >> sys.stderr, 'connection from', self.ip, ':', self.port;

            # Receive the data in small chunks and retransmit it
            while True:
                data = self.socket.recv(1028)
                self._jobs.append( data );

        finally:
            # Clean up the connection
            self.socket.close()




class Server(threading.Thread):
    def __init__(self, jobs):
        self._jobs = jobs;
        self.connections = [];
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.server_address = ('localhost', 3998)
        print >> sys.stderr, 'starting up on %s port %s' % self.server_address
        self.sock.bind(self.server_address)

    def run(self):
        try:
            # Listen for incoming connections
            self.sock.listen(1)

            while True:
                # Wait for a connection
                print >> sys.stderr, 'waiting for a connection'

                (clientsock, (ip, port)) = self.sock.accept()
                c = Connection(ip, port, clientsock, self._jobs);
                self.connections.append( c );
                c.start();
        finally:
            for c in self.connections:
                c.socket.close();

