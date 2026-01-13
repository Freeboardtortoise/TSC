import _thread

class Server:
    def __init__(self, ip, port):
        self.connections = []
        self.sinit = []
        IDs_used = [1]
        import socket
        print("Made with TSC")
        print("Darion Knighton-Fitt")
        server = ip
        port = port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <-- allows rebinding quickly
        try:
            s.bind((server, port))
            print("server started")
        except socket.error as e:
            print("ERROR, try again")
            print(e)

        s.listen()
        print("waiting for connection")
        self.sinit = [s, IDs_used]
        self.connections = self.connections


    def get_clients(self):
        import TSC.client_function as client_function
        import _thread

        s = self.sinit[0]
        IDs_used = self.sinit[1]
        current_ID = 1
        import random
        while current_ID in IDs_used:
            current_ID = random.randint(10000000, 999999999)

        self.sinit[1] = self.sinit[1] + [current_ID]
        conn, addr = s.accept()
        print("\n new connection:" + str(addr))
        _thread.start_new_thread(
            client_function.client_threaded, (conn, addr, self.sinit[1]))
        self.connections = self.connections + [[conn, addr, current_ID]]


    def get_initc():
        global initc
        return initc


    def get_connections(self):
        return self.connections


    def do_not_use(self):
        while True:
            self.get_clients()


    def get_clients_threaded(self):
        _thread.start_new_thread(self.do_not_use, ())

def recieve(conn):
    try:
        data = conn.recv(2048)
        data = data.decode("utf-8")

        if not data:
            return None
        else:
            return data
    except:
        return None
def send(conn, reply):
    try:
        conn.sendall(str.encode(reply))
        return True
    except:
        return False