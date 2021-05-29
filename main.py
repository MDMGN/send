from validar import validarCampos
from sendinblue import sendinblue

print("==================Patito Feliz===================\n==============(Agencia de Marketing)=============")
print("Bienvenido al sistema de envios de email para nuestros Asesores.")
validar=validarCampos()
while True:
    print("\nIngresa tus datos:")
    nombre=validar.validarName()
    email=validar.validarEmail()
    telefono=validar.validarPhone()
    publicity=validar.validarPublicity()
    publicidad = sendinblue(nombre,email,telefono,publicity)
    publicidad.confirmSend()
    publicidad.confirmExit()