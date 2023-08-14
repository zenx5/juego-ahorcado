# Juego del ahorcado.

def check_letter(list_letter, letter):
    list_index = []
    if letter in list_letter:
        for index in range( len(list_letter) ):
            if( list_letter[index]==letter ):
                list_index.append(index)
    return list_index

def get_word():
    return input("La primera persona escribe la palabra: ")

def start_game(p_lista, intentos):
    marcador=True
    piso=[]

    for i in range( len(p_lista) ):
        p_lista[i] = p_lista[i].lower()
        piso.append("_")

    while marcador:
        print(piso)
        letra=input("Diga una letra: ")
        indexes = check_letter(p_lista, letra)
        if len(indexes)==0:
            intentos-=1
        else:
            for index in indexes:
                piso[index] = letra
        print(f"intentos: ${intentos}")

        if intentos==0:
            marcador = False
        else:
            print(f"Le quedan {intentos} intentos")

        if "_" not in piso:
            marcador = True
            break

    return marcador


def main(intentos):
    print(" Bienvenido al juego del ahorcado ")
    word = get_word()
    p_lista=list(word)

    if( start_game(p_lista, intentos) ):
        print(f"Juego ganado, la palabra es {word}")
    else:
        print("Juego perdido")


main(3)


