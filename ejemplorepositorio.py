opcion=int(input(" digite la opcion que desee inicio (1) nosotros(2)comprar(3)reservas(4)productos(5)"))
if opcion==1:
    print("empresa dedicada a la venta y servicio de belleza")
    print("El concepto de belleza se ha estudiado principalmente por la disciplina filosófica de la estética, pero también ha sido abordado por otras disciplinas como la historia, la sociología y la psicología social Comúnmente, la belleza se define como la característica de una cosa o persona que, a través de una experiencia sensorial, procura una sensación de placer o un sentimiento de satisfacción Por otro lado, la Estética es la rama de la Filosofía que tiene por objeto el estudio de la esencia y la percepción de la belleza La búsqueda de la belleza y de la estética ha sido una constante en la sociedad desde hace siglos. Esta búsqueda de la belleza en la persona individual ha derivado hoy en día en tratamientos médicos para resolver problemas estéticos y resaltar la belleza de cada persona, así como para prevenir la aparición de dichos problemas. Es así como surge lo que hoy en día se conoce como medicina estética.")

if opcion==2:
    print("servicios de aseo ")
    print("venta de productos de aseo ")
    print("atencion al cliente virtual ")
    print("excelente servicio de ventas")
if(opcion==3):
    iden=int(input("digite su cedula"))
    print("registrado correctamente")
    ingresar=int(input("ingrese nombre de usuario(numero de documento)"))
    if ingresar=iden:
        print("bienvenido")
        print("Escoge la variadad de productos que desees y se guradaran en el carrito")
    else:
        print("nombre de usaurio incorrecto vuelve a intentarlo")
if(opcion==4):
    iden=int(input("digite su cedula"))
    print("registrado correctamente")
    ingresar=int(input("ingrese nombre de usuario(numero de documento)"))
    if ingresar=iden:
        print("bienvenido")
        print("realiza tu reserva")
        dia=int("digita el dia de la reserva")
        hora=int("digita la hora de la reserva")
        servicio=str(input("digita el tipo de reserva "))
if(opcion==5):
    iden=int(input("digite su cedula"))
    print("registrado correctamente")
    ingresar=int(input("ingrese nombre de usuario(numero de documento)"))
    if ingresar=iden:
        print("productos de aseo") 
        print("productos para el rostro")
        print("productos para el pelo ")
        print("productos de belleza")
