# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
import HandlePackets
import socket
import threading

#Clase Listen
class Listen(threading.Thread):
    def __init__(self, port, log):
        self.port = port
        self.log = log
        threading.Thread.__init__(self)
    def run(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', self.port))
            server.listen(10)
            self.log.Write("Sockets correctamente iniciados en el puerto: ".__add__(str(self.port)))
            self.log.Write("Servidor iniciando correctamente, esperando conexiones!")
            while True:
                connection = Connection(server.accept(), self.log)
                connection.start()
            server.close()
            server = None
            connection.join()
            self.join()
        except socket.error, e:
            self.log.WriteError("Hubo un error con los sockets: ".__add__(e))
#Clase Connection
class Connection(threading.Thread):
    def __init__(self, (sock, addr), log):
        self.sock = sock
        self.addr = addr
        self.log = log
        threading.Thread.__init__(self)
    def sendData(self, data):
        try:
            self.sock.send(data)
        except socket.error, e:
            self.log.WriteError("Hubo un error al intentar enviar ".__add__(": ").__add__(e))
    def run(self):
        self.log.Write("Nuevo cliente conectado")
        try:
            data = self.sock.recv(512)
            self.log.Write("Packet recibido => ".__add__(str(data)))
            HandlePackets.HandlePackets().Parse(int(data), self.log, self)
        except socket.error, e:
            self.log.WriteError("Hubo un error con la conexion: ".__add__(e))