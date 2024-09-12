import string
import random
longitud=0
while longitud <8:
    longitud= int(input("Ingrese el tamaño deseado de la contraseña (8 a más digitos): "))

mayc=string.ascii_uppercase+'Ñ'
minc=string.ascii_lowercase+'ñ'
nums=string.digits
cart=string.punctuation

password=""
i=1
while i<longitud:
    if i<=longitud:
        password=password+random.choice(mayc)
        i+=1
    if i<=longitud:
        password=password+random.choice(minc)
        i+=1
    if i<=longitud:
        password=password+random.choice(nums)
        i+=1
    if i<=longitud:
        password=password+random.choice(cart)
        i+=1

#print(password)
passwd2=list(password)  #Cambia la candena a lista para poder hacerla más aleatoria
#print(passwd2)
random.shuffle(passwd2) #Desordena la lista
print("La contraseña segura es : "+"".join(passwd2)) #Imprime la contraseña final.
    

