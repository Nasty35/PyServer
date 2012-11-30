# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
import Sockets
import Logging

log = Logging.Logging();
log.Write("Iniciando servidor...")
socket = Sockets.Listen(30000, log)
socket.start()