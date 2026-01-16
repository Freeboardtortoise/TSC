import _thread
import socket

import TSC.pluginsManager as pm

def initialise_plugins():
    global plugins
    plugins = pm.ServerPluginManager()

class Server:
    def __init__(self, port):
        def get_local_ip():
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
            finally:
                s.close()
        ip = get_local_ip()
        self.connections = []
        self.sinit = []
        self.ip = ip
        self.port = port
        IDs_used = [1]
        import socket
        server = ip
        port = port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <-- allows rebinding quickly
        try:
            s.bind((server, port))
        except socket.error as e:
            print("ERROR, try again")
            print(e)

        s.listen()
        self.sinit = [s, IDs_used]
        self.connections = self.connections
        plugins.on_server_start(ip, port, self.sinit, self.connections)


    def get_clients(self, message_handeler):
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
        # Let plugins know someone connected
        plugins.on_connection(conn, addr, self.sinit, self.connections)
        _thread.start_new_thread(
            self.client_function_wrapper, (message_handeler,conn, addr, self.sinit[1]))
        self.connections = self.connections + [[conn, addr, current_ID]]

    def client_function_wrapper(self, message_handeler, conn, addr, sinit):
        plugins.on_connection(self.ip, self.port, self.sinit, self.connections)
        while True:
            data = recieve(conn)
            current = ''
            handledMessage = False
            reply = plugins.on_message_recieve(self.ip, self.port, self.sinit, self.connections, data)
            userReply = message_handeler(self.ip, self.port, reply)
            reply = plugins.on_message_send(self.ip, self.port, self.sinit, self.connections, reply)
            send(conn,reply)
    def get_initc():
        global initc
        return initc


    def get_connections(self):
        return self.connections


    def do_not_use(self, client_function):
        while True:
            self.get_clients(client_function)


    def get_clients_threaded(self, message_handeler):
        _thread.start_new_thread(self.do_not_use, (message_handeler,))

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
