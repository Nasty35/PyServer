import SocketServer
import threading

class Server(threading.Thread):
    def __init__(self, port):
        self.port = port
        threading.Thread.__init__(self)
    def run(self):
        try:
            server = SocketServer.ThreadingTCPServer(('localhost', self.port), ServerHandler)
            print 'Sockets iniciados en el puerto '.__add__(str(self.port))
            server.serve_forever()
        except SocketServer.socket.error, e:
            print e
class ServerHandler(SocketServer.BaseRequestHandler):
    def setup(self):
        # Connect
        self.client = self.client_address
        print 'Nuevo cliente conectado: '.__add__(self.client)
        self.request.send('Hola')
    def handle(self):
        # Handling
        while True:
            data = self.request.recv(1024)
            print 'Recibido: '.__add__(data)
            #if data.strip().__eq__('close') : return
            respuesta = ""
            self.request.send(respuesta)
    def finish(self):
        # Disconnect
        print 'El cliente '.__add__(self.client).__add__('se desconecto')