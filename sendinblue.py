import requests
from db import *
from save_email import saveEmail
class sendinblue():
    apiKey="your api key"
    url="https://api.sendinblue.com/v3/smtp/email"
    emailCompany="michaelmdvrhack@gmail.com"
    nombreAsesor=""
    emailAsesor=""
    telefonoAsesor=""
    nombrePublicidad=""
    def __init__(self,nameasesor,emailasesor,phoneasesor,namepublicity):
        self.nombreAsesor=nameasesor
        self.emailAsesor=emailasesor
        self.telefonoAsesor=phoneasesor
        self.nombrePublicidad=namepublicity
    def sendEmail(self):
        for cliente in database:
            nombreCliente = database[cliente]["nombre"]
            emailCliente = database[cliente]["email"]
        payload = {
                    "sender": {
                        "name": "Fruit Shop",
                        "email": self.emailCompany
                    },
                    "to": [{"email":emailCliente}],
                    "params": {
                        "prospecto":nombreCliente,
                        "asesor": self.nombreAsesor,
                        "telefono": self.telefonoAsesor,
                        "email": self.emailAsesor
                    },
                    "subject": self.nombrePublicidad,
                    "templateId": 1
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "api-key": self.apiKey
        }
        response = requests.request("POST", self.url, json=payload, headers=headers)
        return response.text
    def confirmSend(self):
        try:
            while True:
                confirmar=str(input("Desea enviar el email con estos datos? (s/n): ")).lower()
                if confirmar=="s":
                    self.sendEmail()
                    self.saveEmail()
                    print("El email fue enviado con exito!")
                    break
                elif confirmar=="n":
                    break
                else:
                    print("La opción no es correcta.")
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()
    def confirmExit(self):
        try:
            while True:
                confirmar=str(input("Desea salir del sistema? (s/n): ")).lower()
                if confirmar=="s":
                    print("Gracias por utilizar nuestro servicio!.\n..Saliendo del programa.")
                    exit()
                elif confirmar=="n":
                    break
                else:
                    print("La opción no es correcta.")
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()
    def saveEmail(self):
        guardar=saveEmail()
        sendEmail=self.sendEmail()
        guardar.historyEmail(sendEmail)