# Proyecto escrito por Daniel (Nasty35)
# Prohibido distribuir sin dar agradecimientos
# Uso exclusivo para el uso educativo y experimental

#Importando librerias
from datetime import datetime

#Clase Logging
class Logging:
    def Write(self, text):
        text = '[' + str(datetime.today()) + '] - ' + text
        print text
        try:
            out = open("log.txt", "a")
            out.write(text.__add__("\n"))
            out.close()
        except IOError, e:
            print e
    def WriteError(self, error_text):
        error_text = '[ERROR #'.__add__(str(datetime.today())).__add__('] - ').__add__(error_text)
        print error_text
        try:
            out = open("log.txt", "a")
            out.write(error_text.__add__("\n"))
            out.close()
        except IOError, e:
            print e