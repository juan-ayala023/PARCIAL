# =============================================================================
# REGEX AVANZADO — Grupos, alternancia, lookahead
# =============================================================================
import re

# =============================================================================
# 1. GRUPOS DE CAPTURA ()
# Permiten extraer partes específicas de un match
# =============================================================================

# Sin grupo: retorna el match completo
print("=== Sin grupo ===")
resultado = re.findall(r"\d{4}-\d{2}-\d{2}", "Fecha: 2024-12-25")
print(resultado)   # ['2024-12-25']

# Con grupos: retorna solo lo capturado dentro de ()
print("\n=== Con grupos — extraer año, mes, día por separado ===")
resultado = re.findall(r"(\d{4})-(\d{2})-(\d{2})", "Fecha: 2024-12-25")
print(resultado)   # [('2024', '12', '25')]

# Uso práctico: extraer nombre y dominio de un email
print("\n=== Extraer partes de un email ===")
patron = r"([\w.-]+)@([\w.-]+)"
match = re.search(patron, "usuario@correo.com")
if match:
    print(f"Usuario: {match.group(1)}")   # usuario
    print(f"Dominio: {match.group(2)}")   # correo.com
    print(f"Completo: {match.group(0)}")  # usuario@correo.com

# Ejercicio: extraer código de área y número de teléfono
print("\n=== Extraer código de área y número ===")
def extraer_telefono(texto):
    # formato: (57) 3001234567  o  57-3001234567
    patron = r"\(?(\d{2})\)?[-\s]?(\d{10})"
    match = re.search(patron, texto)
    if match:
        return {"codigo": match.group(1), "numero": match.group(2)}
    return None

print(extraer_telefono("Llama al (57) 3001234567"))
print(extraer_telefono("Contacto: 57-3009876543"))


# =============================================================================
# 2. ALTERNANCIA |
# Funciona como OR — coincide con uno u otro patrón
# =============================================================================
print("\n=== Alternancia | ===")

# Validar extensión de archivo
def validar_imagen(nombre):
    return bool(re.search(r"\.(jpg|jpeg|png|gif|webp)$", nombre, re.IGNORECASE))

print(validar_imagen("foto.jpg"))     # True
print(validar_imagen("foto.PNG"))     # True
print(validar_imagen("foto.pdf"))     # False
print(validar_imagen("foto.jpeg"))    # True

# Encontrar palabras clave en un texto
print("\n=== Buscar palabras clave ===")
def contiene_error(log):
    return bool(re.search(r"error|exception|fallo|crítico", log, re.IGNORECASE))

print(contiene_error("INFO: todo bien"))              # False
print(contiene_error("ERROR: conexión fallida"))      # True
print(contiene_error("NullPointerException en línea 42"))  # True


# =============================================================================
# 3. CUANTIFICADORES CODICIOSOS vs PEREZOSOS
# Por defecto son codiciosos (toman lo más posible)
# Agregar ? los hace perezosos (toman lo menos posible)
# =============================================================================
print("\n=== Codicioso vs Perezoso ===")

html = "<b>negrita</b> y <i>cursiva</i>"

print("Codicioso .* (toma todo):")
print(re.findall(r"<.*>", html))     # ['<b>negrita</b> y <i>cursiva</i>']

print("Perezoso .*? (toma lo mínimo):")
print(re.findall(r"<.*?>", html))    # ['<b>', '</b>', '<i>', '</i>']

# Ejercicio: extraer contenido entre etiquetas
def extraer_etiqueta(html, tag):
    patron = rf"<{tag}>(.*?)</{tag}>"
    return re.findall(patron, html, re.DOTALL)

print("\n=== Extraer contenido de etiquetas ===")
print(extraer_etiqueta("<b>Hola</b> mundo <b>Python</b>", "b"))
# ['Hola', 'Python']


# =============================================================================
# 4. LOOKAHEAD Y LOOKBEHIND
# Verifican contexto sin incluirlo en el match
# (?=...) lookahead positivo  — lo que sigue debe ser...
# (?!...) lookahead negativo  — lo que sigue NO debe ser...
# (?<=...) lookbehind positivo — lo que antecede debe ser...
# (?<!...) lookbehind negativo — lo que antecede NO debe ser...
# =============================================================================
print("\n=== Lookahead positivo (?=) ===")
# Encontrar números seguidos de "kg"
texto = "Tengo 5kg de arroz, 3 litros de leche y 2kg de azúcar"
print(re.findall(r"\d+(?=kg)", texto))    # ['5', '2']

print("\n=== Lookahead negativo (?!) ===")
# Encontrar números NO seguidos de "kg"
print(re.findall(r"\d+(?!kg)", texto))    # incluye '3' y partes de otros números

print("\n=== Lookbehind positivo (?<=) ===")
# Extraer lo que viene después del símbolo $
precios = "Total: $150, Descuento: $30, Final: $120"
print(re.findall(r"(?<=\$)\d+", precios))  # ['150', '30', '120']


# =============================================================================
# 5. FLAGS ÚTILES
# re.IGNORECASE (re.I) — no distingue mayúsculas/minúsculas
# re.MULTILINE  (re.M) — ^ y $ aplican por línea
# re.DOTALL     (re.S) — el . también captura saltos de línea
# =============================================================================
print("\n=== Flags ===")

texto_multi = """ERROR: fallo en módulo A
INFO: proceso OK
WARNING: memoria alta
ERROR: timeout"""

print("Líneas que empiezan con ERROR (MULTILINE):")
print(re.findall(r"^ERROR.*", texto_multi, re.MULTILINE))

print("\nBúsqueda sin distinguir mayúsculas:")
print(re.findall(r"error", texto_multi, re.IGNORECASE))


# =============================================================================
# 6. re.sub AVANZADO — reemplazar con función
# =============================================================================
print("\n=== re.sub con función ===")

# Censurar números de tarjeta de crédito (dejar solo últimos 4 dígitos)
def censurar_tarjeta(texto):
    def reemplazar(match):
        numero = match.group()
        return "*" * (len(numero) - 4) + numero[-4:]
    return re.sub(r"\b\d{16}\b", reemplazar, texto)

print(censurar_tarjeta("Tu tarjeta 1234567890123456 fue procesada"))
# Tu tarjeta ************3456 fue procesada

# Convertir fechas de YYYY-MM-DD a DD/MM/YYYY
def convertir_fecha(texto):
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", texto)

print(convertir_fecha("Nacimiento: 1998-05-23, Graduación: 2020-11-15"))
# Nacimiento: 23/05/1998, Graduación: 15/11/2020


# =============================================================================
# 7. EJERCICIOS COMBINADOS (nivel parcial)
# =============================================================================
print("\n=== EJERCICIO COMBINADO 1 — Validar y extraer cédula colombiana ===")
# Cédula: 8 a 10 dígitos, puede tener puntos como separadores de miles
def validar_cedula(cedula):
    patron = r"^\d{1,3}(\.\d{3})*$"
    limpia = cedula.replace(".", "")
    return bool(re.match(patron, cedula)) and 8 <= len(limpia) <= 10

print(validar_cedula("1.234.567.890"))   # True
print(validar_cedula("98765432"))        # False (sin puntos, formato libre)
print(validar_cedula("123"))             # False

print("\n=== EJERCICIO COMBINADO 2 — Parser de log ===")
def parsear_log(linea):
    """
    Extrae nivel, timestamp y mensaje de una línea de log.
    Formato: [NIVEL] 2024-01-15 10:30:00 - mensaje
    """
    patron = r"\[(\w+)\]\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+-\s+(.*)"
    match = re.match(patron, linea)
    if match:
        return {
            "nivel":     match.group(1),
            "fecha":     match.group(2),
            "hora":      match.group(3),
            "mensaje":   match.group(4)
        }
    return None

log = "[ERROR] 2024-01-15 10:30:00 - Conexión rechazada por el servidor"
print(parsear_log(log))
