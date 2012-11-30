# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias

#Clase ServerMessage
class ServerMessage:
    a = ""
    b = ""
    def __init__(self, header):
        self.a = str(header)
        self.b = "Header: ".__add__(str(header))
    def writeInt(self, c):
        self.a = self.a.__add__(str(c))
        self.b = self.b.__add__(", Int: ").__add__(str(c))
    def writeUTF(self, c):
        self.a = self.a.__add__(c)
        self.b = self.b.__add__(", String: ").__add__(c)
    def writeBool(self, c):
        if(c == True):
            self.a = self.a.__add__("1")
            self.b = self.b.__add__(", Bool: true")
        elif(c == False):
            self.a = self.a.__add__("0")
            self.b = self.b.__add__(", Bool: false")
    def sendMessage(self, log, sock):
        log.Write("Packet enviado => ".__add__(self.b))
        sock.sendData(self.a)