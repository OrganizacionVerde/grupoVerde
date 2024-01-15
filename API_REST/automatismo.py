import entrada
from time import sleep


if __name__ == "__main__":

    contador = 0
    
    while True:
        entrada.main()
        sleep(3)
        contador +=1

        if contador == 1200:
            print(f"Terminado. Registros metidos: {contador}")
            break

