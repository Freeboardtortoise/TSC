import os
import importlib.util

def import_all_from_folder(folder_path: str):
    """
    Import all .py files from the given folder (ignores __init__.py and files starting with '_').
    Returns a list of imported modules.
    """
    imported_modules = []

    if not os.path.isdir(folder_path):
        raise ValueError(f"{folder_path} is not a valid directory")

    for filename in os.listdir(folder_path):
        if not filename.endswith(".py") or filename.startswith("_"):
            continue

        module_name = filename[:-3]
        file_path = os.path.join(folder_path, filename)

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            imported_modules.append(module)

    return imported_modules

class ClientPlugin:
    def __init__(self):
        print("the plugin has not yet implimented this function yet")
    def on_connection(self, ip, port):
        print("the plugin has not yet implimented this function yet")
    def on_message_send(self, ip, port, message):
        print("the plugin has not yet implimented this function yet")
        return {"handled": False, "newMessage":None}
    def on_message_recieve(self, ip, port, message):
        print("the plugin has not yet implimented this function yet")
        return {"handled": False, "newMessage":None}



class ServerPlugin:
    def __init__(self):
        print("the plugin has not yet implimented this function yet")
    def on_server_start(self, ip, port, sinit, connections):
        print("the plugin has not yet implimented this yet")
    def on_connection(self, ip, port, sinit, connections):
        print("the plugin has not yet implimented this yet")
    def on_message_recieve(self, ip, port, sinit,connections, data):
        return {"handled": False, "message": data}
    def on_message_send(self, ip, port, sinit, connections, data):
        return {"handled": False,"message": data}
    

class ClientPluginManager:
    def __init__(self, pluginFolder="TSC/plugins/"):
        modules = import_all_from_folder(pluginFolder)
        self.plugins = []
        for module in modules:
            print(module)
            self.plugins.append(module.ClientPlugin())

    def on_connection(self, ip,port,id):
        for plugin in self.plugins:
            plugin.on_connection(ip, port)
    def on_message_send(self, ip, port, message):
        thing_to_return = None
        for plugin in self.plugins:
            thing = plugin.on_message_send(ip, port, message)
            if thing["handled"] == True:
                if thing_to_return is not None:
                    thing_to_return = thing["mesage"]

        return thing_to_return
    def on_message_recieve(self, ip, port, message):
        thing_to_return = None
        for plugin in self.plugins:
            thing = plugin.on_message_recieve(ip, port, message)
            if thing["handled"] == True:
                if thing_to_return is not None:
                    thing_to_return = thing["mesage"]

        return thing_to_return

class ServerPluginManager:
    def __init__(self, pluginFolder="TSC/plugins/"):
        modules = import_all_from_folder(pluginFolder)
        self.plugins = []
        for module in modules:
            print(module)
            self.plugins.append(module.ServerPlugin())
    
    def on_server_start(self, ip, port, sinit, connections):
        for plugin in self.plugins:
            plugin.on_server_start()

    def on_connection(self, ip,port,sinit, connections):
        for plugin in self.plugins:
            plugin.on_connection(ip, port)
    def on_message_send(self, ip, port,sinit,connections, message):
        thing_to_return = None
        for plugin in self.plugins:
            thing = plugin.on_message_send(ip, port, sinit, connections message)
            if thing["handled"] == True:
                if thing_to_return is not None:
                    thing_to_return = thing["mesage"]
            if thing_to_return is None:
                thing_to_return = thing

        return thing_to_return
    def on_message_recieve(self, ip, port, message):
        thing_to_return = None
        for plugin in self.plugins:
            thing = plugin.on_message_recieve(ip, port, message)
            if thing["handled"] == True:
                if thing_to_return is not None:
                    thing_to_return = thing["mesage"]

        return thing_to_return






