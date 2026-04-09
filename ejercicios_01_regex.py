import re

# =============================================================================
# EJERCICIOS — EXPRESIONES REGULARES
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Validar correo electrónico
#    usuario@dominio.com → True
#    usuario@.com        → False
# -----------------------------------------------------------------------------
def validar_email(email):
    patron = r"^[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

# -----------------------------------------------------------------------------
# 2. Validar número de teléfono colombiano
#    Debe empezar con 3 y tener 10 dígitos
#    3001234567 → True  |  1234567890 → False
# -----------------------------------------------------------------------------
def validar_telefono(numero):
    patron = r"^3\d{9}$"
    return bool(re.match(patron, numero))

# -----------------------------------------------------------------------------
# 3. Extraer todos los números de un texto
#    "Tengo 3 gatos y 12 perros" → ["3", "12"]
# -----------------------------------------------------------------------------
def extraer_numeros(texto):
    return re.findall(r"\d+", texto)

# -----------------------------------------------------------------------------
# 4. Validar contraseña segura
#    Mínimo 8 caracteres, al menos una mayúscula, una minúscula y un dígito
#    "Abcdef1!" → True  |  "password" → False
# -----------------------------------------------------------------------------
def validar_contrasena(password):
    tiene_mayuscula = bool(re.search(r"[A-Z]", password))
    tiene_minuscula = bool(re.search(r"[a-z]", password))
    tiene_digito    = bool(re.search(r"\d", password))
    longitud_ok     = len(password) >= 8
    return tiene_mayuscula and tiene_minuscula and tiene_digito and longitud_ok

# -----------------------------------------------------------------------------
# 5. Extraer URLs de un texto
#    "Visita https://google.com o http://python.org" → [lista de urls]
# -----------------------------------------------------------------------------
def extraer_urls(texto):
    return re.findall(r"https?://[^\s]+", texto)

# -----------------------------------------------------------------------------
# 6. Validar fecha en formato DD/MM/AAAA
#    "25/12/2024" → True  |  "2024-12-25" → False
# -----------------------------------------------------------------------------
def validar_fecha(fecha):
    patron = r"^\d{2}/\d{2}/\d{4}$"
    return bool(re.match(patron, fecha))

# -----------------------------------------------------------------------------
# 7. Contar palabras que empiezan con mayúscula
#    "Hola mundo, Cómo Estás" → ["Hola", "Cómo", "Estás"]
# -----------------------------------------------------------------------------
def palabras_con_mayuscula(texto):
    return re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]*", texto)

# -----------------------------------------------------------------------------
# 8. Reemplazar múltiples espacios por uno solo
#    "Hola    mundo   cómo   estás" → "Hola mundo cómo estás"
# -----------------------------------------------------------------------------
def limpiar_espacios(texto):
    return re.sub(r" +", " ", texto).strip()

# -----------------------------------------------------------------------------
# 9. Validar código postal colombiano (6 dígitos)
#    "050010" → True  |  "12345" → False
# -----------------------------------------------------------------------------
def validar_codigo_postal(codigo):
    patron = r"^\d{6}$"
    return bool(re.match(patron, codigo))

# -----------------------------------------------------------------------------
# 10. Extraer palabras en MAYÚSCULAS de un texto
#     "Hola MUNDO esto es PYTHON" → ["MUNDO", "PYTHON"]
# -----------------------------------------------------------------------------
def extraer_mayusculas(texto):
    return re.findall(r"\b[A-Z]{2,}\b", texto)


# =============================================================================
# PRUEBAS
# =============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("EJERCICIO 1 — Validar email")
    print("=" * 55)
    print(validar_email("usuario@correo.com"))    # True
    print(validar_email("usuario@.com"))           # False
    print(validar_email("sin_arroba.com"))         # False

    print("\n" + "=" * 55)
    print("EJERCICIO 2 — Validar teléfono colombiano")
    print("=" * 55)
    print(validar_telefono("3001234567"))   # True
    print(validar_telefono("1234567890"))   # False
    print(validar_telefono("300123456"))    # False (9 dígitos)

    print("\n" + "=" * 55)
    print("EJERCICIO 3 — Extraer números")
    print("=" * 55)
    print(extraer_numeros("Tengo 3 gatos y 12 perros"))      # ['3', '12']
    print(extraer_numeros("En 2024 nací con 3 kilos"))        # ['2024', '3']

    print("\n" + "=" * 55)
    print("EJERCICIO 4 — Validar contraseña segura")
    print("=" * 55)
    print(validar_contrasena("Abcdef1!"))   # True
    print(validar_contrasena("password"))   # False
    print(validar_contrasena("ABC1234"))    # False (sin minúscula, muy corta)

    print("\n" + "=" * 55)
    print("EJERCICIO 5 — Extraer URLs")
    print("=" * 55)
    print(extraer_urls("Visita https://google.com o http://python.org"))
    # ['https://google.com', 'http://python.org']

    print("\n" + "=" * 55)
    print("EJERCICIO 6 — Validar fecha DD/MM/AAAA")
    print("=" * 55)
    print(validar_fecha("25/12/2024"))   # True
    print(validar_fecha("2024-12-25"))   # False
    print(validar_fecha("1/1/2024"))     # False

    print("\n" + "=" * 55)
    print("EJERCICIO 7 — Palabras con mayúscula")
    print("=" * 55)
    print(palabras_con_mayuscula("Hola mundo, Cómo Estás"))
    # ['Hola', 'Cómo', 'Estás']

    print("\n" + "=" * 55)
    print("EJERCICIO 8 — Limpiar espacios")
    print("=" * 55)
    print(limpiar_espacios("Hola    mundo   cómo   estás"))
    # "Hola mundo cómo estás"

    print("\n" + "=" * 55)
    print("EJERCICIO 9 — Validar código postal")
    print("=" * 55)
    print(validar_codigo_postal("050010"))   # True
    print(validar_codigo_postal("12345"))    # False
    print(validar_codigo_postal("1234567"))  # False

    print("\n" + "=" * 55)
    print("EJERCICIO 10 — Extraer palabras en MAYÚSCULAS")
    print("=" * 55)
    print(extraer_mayusculas("Hola MUNDO esto es PYTHON"))
    # ['MUNDO', 'PYTHON']
