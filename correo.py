import re

def validar_correo_institucional(correo):
    patron = r'^[a-z]{2,}\.[a-z]{2,}@elpoli\.edu\.co$'
    if re.match(patron, correo):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f"juanjose.perez@elpoli.edu.co -> {validar_correo_institucional('juanjose.perez@elpoli.edu.co')}")
    print(f"j.perez@elpoli.edu.co -> {validar_correo_institucional('j.perez@elpoli.edu.co')}")      
    print(f"juanjose.perez@gmail.com -> {validar_correo_institucional('juanjose.perez@gmail.com')}")        
    print(f"juanjose.Perez@elpoli.edu.co -> {validar_correo_institucional('juanjose.Perez@elpoli.edu.co')}")