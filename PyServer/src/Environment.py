import Network
import Database

print 'Iniciando servidor...'
server = Network.Server(30000)
server.start()
db = Database.Database('localhost', 'root', 'root', 'python')
print 'Servidor iniciado!'