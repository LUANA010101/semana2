nombre = input ("ingrese su nombre") 
print (f"Bienvenido { nombre} menu de postres") 
opcion= 0
while opcion !=4:
     print("1 macarrones")
     print("2 profiteroles")
     print("3 crepas")
     print("4 salir")
     opcion= int(input("elige una opcion del 1 al 4 : \n"))
     if   opcion >=1 and opcion <= 4:        
          print (f"has elegido la opcion numero :, {opcion},  gracias")
     elif opcion == 4:
          print= ("haz salido del menu") 
     else:
          print("opcion invalida")    
                   
            


