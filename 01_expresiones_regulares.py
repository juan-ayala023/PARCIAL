# ============================================================
#  EXPRESIONES REGULARES EN PYTHON - Guía de Estudio
#  Parcial Algoritmos y Programación 4
# ============================================================

import re

# ──────────────────────────────────────────────────────────
# 1. FUNCIONES PRINCIPALES DE re
# ──────────────────────────────────────────────────────────
# re.match(patron, texto)   → busca SOLO al inicio del string
# re.search(patron, texto)  → busca en CUALQUIER parte del string
# re.findall(patron, texto) → retorna LISTA con todas las coincidencias
# re.sub(patron, reemplazo, texto) → reemplaza coincidencias

# ──────────────────────────────────────────────────────────
# 2. METACARACTERES ESENCIALES
# ──────────────────────────────────────────────────────────
# ^       inicio del string
# $       fin del string
# .       cualquier carácter (excepto salto de línea)
# \d      dígito [0-9]
# \w      letra, dígito o guion bajo [a-zA-Z0-9_]
# \s      espacio en blanco
# [A-Z]   letras mayúsculas
# [a-z]   letras minúsculas
# [0-9]   dígitos
# {n}     exactamente n veces
# {n,m}   entre n y m veces
# +       1 o más veces
# *       0 o más veces
# ?       0 o 1 vez (también hace el guion opcional)
# |       OR
# ( )     grupo

# ──────────────────────────────────────────────────────────
# 3. EJERCICIO 1 DEL PARCIAL — validar_placa_vehiculo
# ──────────────────────────────────────────────────────────
# Formato válido: 3 letras MAYÚSCULAS + guion OPCIONAL + 3 dígitos
# ABC123  → True
# ABC-123 → True
# AB1234  → False  (solo 2 letras)
# abc123  → False  (letras minúsculas)

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.
    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123
    """
    patron = r"^[A-Z]{3}-?\d{3}$"
    #         ^            → inicio
    #         [A-Z]{3}     → exactamente 3 letras mayúsculas
    #         -?           → guion opcional (0 o 1 vez)
    #         \d{3}        → exactamente 3 dígitos
    #         $            → fin
    return bool(re.match(patron, placa))

# Pruebas
print("=== validar_placa_vehiculo ===")
print(validar_placa_vehiculo("ABC123"))   # True
print(validar_placa_vehiculo("ABC-123"))  # True
print(validar_placa_vehiculo("AB1234"))   # False
print(validar_placa_vehiculo("abc123"))   # False
print(validar_placa_vehiculo("ABCD12"))   # False
print(validar_placa_vehiculo("ABC12"))    # False

# ──────────────────────────────────────────────────────────
# 4. EJERCICIO 2 DEL PARCIAL — extraer_hashtags
# ──────────────────────────────────────────────────────────
# Un hashtag: # seguido de letras, números o guion bajo
# Usar re.findall para obtener TODOS los hashtags

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.
    """
    return re.findall(r"#\w+", texto)
    # #    → el símbolo hashtag literal
    # \w+  → una o más letras, dígitos o guion bajo

# Pruebas
print("\n=== extraer_hashtags ===")
print(extraer_hashtags("Hola #python es #genial y #100dias"))
# -> ["#python", "#genial", "#100dias"]
print(extraer_hashtags("Sin hashtags aquí"))
# -> []
print(extraer_hashtags("#hola mundo #chao_todos"))
# -> ["#hola", "#chao_todos"]

# ──────────────────────────────────────────────────────────
# 5. OTROS PATRONES COMUNES (posibles variantes en el parcial)
# ──────────────────────────────────────────────────────────

# Email
patron_email = r"^[\w.-]+@[\w.-]+\.\w{2,}$"
print("\n=== Emails ===")
print(bool(re.match(patron_email, "usuario@correo.com")))  # True
print(bool(re.match(patron_email, "mal_correo")))           # False

# Solo números
patron_numero = r"^\d+$"
print("\n=== Solo números ===")
print(bool(re.match(patron_numero, "12345")))   # True
print(bool(re.match(patron_numero, "123ab")))   # False

# Teléfono colombiano (10 dígitos)
patron_tel = r"^3\d{9}$"
print("\n=== Teléfono ===")
print(bool(re.match(patron_tel, "3001234567")))  # True
print(bool(re.match(patron_tel, "1234567890")))  # False

# Palabras que empiezan con mayúscula
patron_nombre = r"^[A-Z][a-z]+"
print("\n=== Nombre con mayúscula ===")
print(bool(re.match(patron_nombre, "Carlos")))   # True
print(bool(re.match(patron_nombre, "carlos")))   # False
