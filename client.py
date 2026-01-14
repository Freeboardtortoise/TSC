import socket
import json
import time

def initialise_plugins():
    global plugin
    import TSC.pluginsManager as pm
    plugin = pm.ClientPluginManager()

class Network:
    def __init__(self, ip_addr, port,timeout):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip_addr
        self.port = port
        self.client.settimeout(timeout)
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except Exception as e:
            raise RuntimeError("failed to connect to server") from e
            

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
        except:
            print("error")
            return False

    def recieve(self):
        return self.client.recv(2048).decode()
currentConnectionID = 0

class Connection:
    def __init__(self, ip, port, timeout=3):
        global currentConnectionID   
        self.allwaysC = False
        self.cinit = []
        self.connectionID = currentConnectionID + 1

        self.ip  = ip
        self.port = port
        currentConnectionID += 1
        import socket
        try:
            n = Network(ip, port, timeout)
            time.sleep(0.1)  # allow server thread to process connection
        except RuntimeError as e:
            raise RuntimeError("failed to connect to server") from e

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cinit = (s, n)
        plugin.on_connection(ip, port)

    def send(self,message):
        data = plugin.on_message_send(self.ip, self.port, message)
        return pluginsManager.on_message_recieve(self.ip, self.port, self.cinit[1].send(data))

    def get_cinit(self):
        return self.cinit
