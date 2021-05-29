import time
class saveEmail():
    def InsertFile(self, string):
        f = open("registro_email.txt", "a+")
        f.write(string)
        f.close()
    def historyEmail(self,datos):
        datos=datos
        cadena=""
        cadena=cadena+"El código del envio es: "+datos+"Fecha y hora: "+time.ctime(time.time()) + "\n"
        self.InsertFile(cadena)