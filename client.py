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

    def recieve(self):
        return self.client.recv(2048).decode()

def _recieve():
    while True:
        global cinit, allwaysC
        data = cinit[1].recieve()
        if allwaysC == True:
            with open("TSC/plugins/server_files/messages.txt", "a") as file:
                file.write(data + "\n")
        else:
            return data

def _recieve_messages():
    global allwaysC, cinit
    import threading
    thread = threading.Thread(target=_recieve)
    thread.start()
    return True

def send(message):
    global cinit
    return cinit[1].send(message)

def get_cinit():
    global cinit
    return cinit

allwaysC = False
cinit = []


def init(ip):
    global cinit
    import socket
    n = Network(ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cinit = (s, n)
    open("TSC/plugins/server_files/messages.txt", "w").close()
    _recieve_messages()

def get_message_latest():
    with open("TSC/plugins/server_files/messages.txt", "r") as file:
        return file.read().split("\n")[-1]

def get_messages_all():
    with open("TSC/plugins/server_files/messages.txt",  "r") as file:
        return file.read().split("\n")

def clear_messages():
    try:
        with open("TSC/plugins/server_files/messages.txt", "w") as file:
            pass
        return True
    except:
        return False