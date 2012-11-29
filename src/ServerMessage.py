# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
import Logging
import Sockets

#Clase ServerMessage
class ServerMessage:
    a = ""
    b = ""
    def __init__(self, header):
        self.a = str(header)
        self.b = "Header: " + str(header)
    def writeInt(self, c):
        self.a = self.a + str(c)
        self.b = self.b + ", Int: " + str(c)
    def writeUTF(self, c):
        self.a = self.a + c
        self.b = self.b + ", String: " + c
    def writeBool(self, c):
        if(c == True):
            self.a = self.a + str(1)
            self.b = self.b + ", Bool: true"
        elif(c == False):
            self.a = self.a + str(0)
            self.b = self.b + ", Bool: false"
    def SendMessage(self, log, sock):
        log.Write("Packet enviado => " + self.b)
        sock.SendData(self.a)