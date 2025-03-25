from TSC import TSC_server
TSC_server.init('127.0.0.1')

running = True
TSC_server.get_clients_threaded()
while running:
    print()