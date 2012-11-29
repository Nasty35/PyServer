# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
import Logging
import socket
import threading
import ServerMessage

#Clase HandlePackets
class HandlePackets():
    def Parse(self, receiver, log, sock):
        Message = ServerMessage.ServerMessage(1)
        Message.writeUTF("lol")
        Message.SendMessage(log, sock)