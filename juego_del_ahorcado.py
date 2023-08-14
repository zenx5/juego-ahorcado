# Juego del ahorcado.

print(" Bienvenido al juego del ahorcado ")
palabra=input("La primera persona escribe la palabra: ")

p_lista=list(palabra)
largo=len(p_lista)
for i in range(largo):
    p_lista[i] = p_lista[i].lower()
piso=[]
intentos=10
for i in range(largo):
    piso.append("_")
marcador=True

while marcador:
    print(piso)
    letra=input("Diga una letra: ")

    if letra not in p_lista:
        print("La letra no esta")
        intentos-=1
        if intentos==0:
            print("Juego perdido")
            break
        else:
            print(f"Le quedan {intentos} intentos")
            continue
    else:
        for i in range(largo):
            if p_lista[i]==letra:
                piso[i]=letra
        
        
        if "_" in piso:
            continue
        else:
            print("Juego ganado ")
            break



        

