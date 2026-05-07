import re

def extraer_menciones(texto):
    patron = r'@[a-zA-Z0-9_]+' 
    
    return re.findall(patron, texto)

if __name__ == "__main__":
    prueba = "Hola @jose_dev_pro y @andrea56, miren esto @python"
    resultado = extraer_menciones(texto=prueba)


    print(f"Texto original: '{prueba}'")
    print(f"Menciones extraidas: {resultado}")