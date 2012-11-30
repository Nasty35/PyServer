# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
import ServerMessage
import Packets

#Clase HandlePackets
class HandlePackets():
    def Parse(self, packet, log, sock):
        if packet.__eq__1:
            log.Write("Id ".__add__(packet).__add__("programada, ejecutando..."))
            Packets.Init().Parse(ServerMessage.ServerMessage(packet), log, sock)
        else:
            log.Write("Id no programada.")