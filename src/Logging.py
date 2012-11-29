# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
from datetime import datetime

#Clase Logging
class Logging:
    def Write(self, text):
        print '[' + str(datetime.today()) + '] - ' + text
	def WriteError(self, error_text):
	    print '[ERROR #' + str(datetime.today()) + '] - ' + error_text