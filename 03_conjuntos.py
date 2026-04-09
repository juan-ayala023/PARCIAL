# ============================================================
#  CONJUNTOS (sets) EN PYTHON - Guía de Estudio
#  Parcial Algoritmos y Programación 4
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. OPERACIONES DE CONJUNTOS — SINTAXIS
# ──────────────────────────────────────────────────────────
# A | B   o  A.union(B)              → Unión (todos)
# A & B   o  A.intersection(B)       → Intersección (en ambos)
# A - B   o  A.difference(B)         → Diferencia (en A pero no en B)
# A ^ B   o  A.symmetric_difference(B) → Simétrica (en uno pero no en ambos)
# A <= B  o  A.issubset(B)           → A es subconjunto de B

# ──────────────────────────────────────────────────────────
# 2. DATOS DEL PARCIAL
# ──────────────────────────────────────────────────────────
club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte     = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

# ──────────────────────────────────────────────────────────
# 3. FUNCIÓN 1: estudiantes_en_todos — intersección de los 3
# ──────────────────────────────────────────────────────────
# Nadie está en los 3 clubes con estos datos → conjunto vacío

def estudiantes_en_todos():
    """Retorna estudiantes inscritos en LOS TRES clubes."""
    return club_ciencias & club_deportes & club_arte

print("=== Estudiantes en los 3 clubes ===")
print(estudiantes_en_todos())   # set() → vacío


# ──────────────────────────────────────────────────────────
# 4. FUNCIÓN 2: solo_un_club — exactamente un club
# ──────────────────────────────────────────────────────────
# Estrategia: (en ciencias pero no en los otros dos)
#           | (en deportes pero no en los otros dos)
#           | (en arte pero no en los otros dos)

def solo_un_club():
    """Retorna estudiantes que están en EXACTAMENTE un club."""
    solo_ciencias  = club_ciencias  - club_deportes - club_arte
    solo_deportes  = club_deportes  - club_ciencias  - club_arte
    solo_arte      = club_arte      - club_ciencias  - club_deportes
    return solo_ciencias | solo_deportes | solo_arte

print("\n=== Solo en un club ===")
print(solo_un_club())
# Esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}


# ──────────────────────────────────────────────────────────
# 5. FUNCIÓN 3: clubes_de_estudiante
# ──────────────────────────────────────────────────────────
def clubes_de_estudiante(nombre):
    """Retorna lista de clubes a los que pertenece el estudiante."""
    clubes = []
    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")
    return clubes

print("\n=== clubes_de_estudiante ===")
print(clubes_de_estudiante("Carlos"))   # ["Ciencias", "Deportes"]
print(clubes_de_estudiante("Julia"))    # ["Arte"]
print(clubes_de_estudiante("Ana"))      # ["Ciencias", "Arte"]
print(clubes_de_estudiante("Gabriel"))  # ["Deportes", "Arte"]


# ──────────────────────────────────────────────────────────
# 6. BONUS: tabla completa de todos los estudiantes
# ──────────────────────────────────────────────────────────
print("\n=== Tabla completa ===")
todos = club_ciencias | club_deportes | club_arte
for estudiante in sorted(todos):
    print(f"  {estudiante}: {clubes_de_estudiante(estudiante)}")


# ──────────────────────────────────────────────────────────
# 7. RESUMEN VISUAL DE OPERACIONES
# ──────────────────────────────────────────────────────────
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\n=== Operaciones base ===")
print(f"A = {A}")
print(f"B = {B}")
print(f"A | B  (unión)        = {A | B}")       # {1,2,3,4,5,6}
print(f"A & B  (intersección) = {A & B}")       # {3,4}
print(f"A - B  (diferencia)   = {A - B}")       # {1,2}
print(f"B - A  (diferencia)   = {B - A}")       # {5,6}
print(f"A ^ B  (simétrica)    = {A ^ B}")       # {1,2,5,6}
