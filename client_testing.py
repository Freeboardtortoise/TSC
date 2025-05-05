import client
client.init("127.0.0.1")
client.allwaysC = True
client.recieve_threaded()

while True:
    print(client.get_messages_all())