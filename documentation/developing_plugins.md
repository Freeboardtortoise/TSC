# Developing plugins

## making the plugin

### steps
1. create the file... _place the file in TSC/plugins/filename.py_
2. add in the plugin metadata:
```python
#plugin metadata
name = "name of your plugin"
pmv = "version of pmv that this plugin is made for"
```
3. import libraries
```python

import TSC.pluginsManager as pmv```
3. create the base classes
```python
class ServerPlugin(pmv.ServerPlugin):
  def __init__(self):
    print("hello from your plugin")
class ClientPlugin(pmv.ClientPlugin):
  def __init__(self):
    print("hello from the server plugin")
```
4. impliment your plugin
use the following functions within the classes to develop your plugin
client side plugin functions
``` __init__(self)``
``` on_connection(self, ip, port)```
``` on_message_send(self, ip, port, message)``` then return ```{"handled": weather or not it has been handlea, "message": the handled messaged}```
``` on_message_recieve(self, ip, port, message)``` then return ```{"handled": weather or not it has been handlea, "message": the handled messaged}```
server side plugin functions
``` on_server_start(self, ip, port, sinit, connections)```

## Applying to make it an oficial plugin

make an isue with the tag "new plugin" in the https://github.com/Freeboardtortoise/TSC-plugins.git with your file atached and a discription and documentation if needed must provide the sourse code or your plugin wil be disrregarded in order to keep this library free and open seorce so people can find the isues and fix them also so that I can review the plugin to make sure that it is not malwhare or potentialy harmfull.
