import services


def main():

    """
    Cuando salida.py se ejecuta, llama a la función salida_lote de services.py
    """
    salida_lote = services.salida_lote()
    print(salida_lote.text)
  
if __name__ == "__main__":
    main()  
