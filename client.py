import socket

class Network:
    def __init__(self, ip_addr):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip_addr
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            print("error connecting to server")
            quit()

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
        except:
            print("error")
            return False



cinit = []
def init(ip):
    global cinit
    import socket
    n = Network(ip)
    print("this program was made with tortoise server client")
    print("library made by Darion Knighton-Fitt")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cinit = (s, n)

def send(message):
    global cinit
    return cinit[1].send(message)

def get_cinit():
    global cinit
    return cinit