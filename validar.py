class validarCampos():
    def validarName(self):
        try:
            name=str(input("Nombre: "))
            validarWord=name.isalpha()
            while not validarWord:
                print("Nombre incorrecto!. Introduzca un nombre valido.")
                name=str(input("Nombre: "))
                validarWord=name.isalpha()
            return name
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()
    def validarEmail(self):
        try:
            email=str(input("Email: "))
            validarArroba=email.count('@')
            validarPunto=email.count('.')
            validarSpace=email.count(" ")
            while validarArroba != 1 or validarPunto == 0 or validarSpace!=0:
                print("Email incorrecto!. Introduzca un email valido.")
                email=str(input("Email: "))
                validarArroba=email.count('@')
                validarPunto=email.count('.')
                validarSpace=email.count(" ")
            return email
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()
    def validarPhone(self):
        try:
            correcto=False
            phone=str(input("Teléfono (9 digitos): "))
            while not correcto:
                if len(phone)==9 and phone.isnumeric():
                    correcto=True
                else:
                    print("Teléfono incorrecto. Introduzca un teléfono valido.")
                    phone=str(input("Teléfono (9 digitos): "))
            return phone
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()
    def validarPublicity(self):
        try:
            publicity=str(input("Nombre de la publicidad: "))
            correcto=False
            while not correcto:
                validarSpace=publicity.isspace()
                if validarSpace==True or len(publicity)==0:
                    print("El nombre de la publicidad no es valida!. Introduzca uno valido.")
                    publicity=str(input("Nombre de la publicidad: "))
                else:
                    correcto=True
            return publicity
        except KeyboardInterrupt:
            print("Error keyboardInterrupt.\nCerrando programa.....")
            exit()