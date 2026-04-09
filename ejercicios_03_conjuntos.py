# =============================================================================
# EJERCICIOS — CONJUNTOS (sets)
# =============================================================================

# Datos base para todos los ejercicios
estudiantes_matematicas = {"Ana", "Carlos", "Diana", "Elena", "Felipe", "Gabriel"}
estudiantes_fisica       = {"Carlos", "Felipe", "Hugo", "Isabel", "Julia"}
estudiantes_quimica      = {"Ana", "Diana", "Hugo", "Karen", "Luis", "Felipe"}
lenguajes_backend        = {"Python", "Java", "Go", "Ruby", "PHP"}
lenguajes_frontend       = {"JavaScript", "TypeScript", "Python", "Dart"}
lenguajes_datos          = {"Python", "R", "Julia", "Scala", "Java"}

# -----------------------------------------------------------------------------
# 1. Estudiantes que están en TODAS las materias (intersección de 3)
#    Resultado esperado: {"Felipe"}
# -----------------------------------------------------------------------------
def en_todas_las_materias():
    return estudiantes_matematicas & estudiantes_fisica & estudiantes_quimica

# -----------------------------------------------------------------------------
# 2. Todos los estudiantes registrados (unión de 3)
# -----------------------------------------------------------------------------
def todos_los_estudiantes():
    return estudiantes_matematicas | estudiantes_fisica | estudiantes_quimica

# -----------------------------------------------------------------------------
# 3. Estudiantes que están SOLO en matemáticas (no en física ni química)
#    Resultado esperado: {"Carlos", "Elena", "Gabriel"}
# -----------------------------------------------------------------------------
def solo_matematicas():
    return estudiantes_matematicas - estudiantes_fisica - estudiantes_quimica

# -----------------------------------------------------------------------------
# 4. Estudiantes en matemáticas o física, pero NO en química
# -----------------------------------------------------------------------------
def mat_o_fis_sin_quimica():
    return (estudiantes_matematicas | estudiantes_fisica) - estudiantes_quimica

# -----------------------------------------------------------------------------
# 5. Verificar si un conjunto es subconjunto de otro
#    ¿Los estudiantes de física están todos también en matemáticas o química?
# -----------------------------------------------------------------------------
def fisica_es_subconjunto():
    return estudiantes_fisica <= (estudiantes_matematicas | estudiantes_quimica)

# -----------------------------------------------------------------------------
# 6. Lenguajes que son útiles para CUALQUIERA de las 3 áreas (backend, frontend, datos)
# -----------------------------------------------------------------------------
def todos_los_lenguajes():
    return lenguajes_backend | lenguajes_frontend | lenguajes_datos

# -----------------------------------------------------------------------------
# 7. Lenguajes exclusivos de backend (no aparecen en frontend ni datos)
#    Resultado esperado: {"Go", "Ruby", "PHP"}
# -----------------------------------------------------------------------------
def solo_backend():
    return lenguajes_backend - lenguajes_frontend - lenguajes_datos

# -----------------------------------------------------------------------------
# 8. Lenguajes que aparecen en EXACTAMENTE DOS áreas
#    (están en 2 de los 3 conjuntos, no en los 3)
# -----------------------------------------------------------------------------
def en_exactamente_dos():
    en_back_front = (lenguajes_backend & lenguajes_frontend) - lenguajes_datos
    en_back_datos = (lenguajes_backend & lenguajes_datos)    - lenguajes_frontend
    en_front_datos= (lenguajes_frontend & lenguajes_datos)   - lenguajes_backend
    return en_back_front | en_back_datos | en_front_datos

# -----------------------------------------------------------------------------
# 9. Dado un nombre, retornar en cuántas materias está inscrito
#    cuantas_materias("Felipe") → 3
#    cuantas_materias("Elena")  → 1
# -----------------------------------------------------------------------------
def cuantas_materias(nombre):
    contador = 0
    if nombre in estudiantes_matematicas: contador += 1
    if nombre in estudiantes_fisica:      contador += 1
    if nombre in estudiantes_quimica:     contador += 1
    return contador

# -----------------------------------------------------------------------------
# 10. Encontrar estudiantes que comparten al menos una materia con un estudiante dado
#     comparten_materia("Felipe") → todos los compañeros en sus mismas materias
# -----------------------------------------------------------------------------
def comparten_materia(nombre):
    companeros = set()
    if nombre in estudiantes_matematicas:
        companeros |= estudiantes_matematicas
    if nombre in estudiantes_fisica:
        companeros |= estudiantes_fisica
    if nombre in estudiantes_quimica:
        companeros |= estudiantes_quimica
    companeros.discard(nombre)   # quitar al propio estudiante
    return companeros


# =============================================================================
# PRUEBAS
# =============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("EJERCICIO 1 — En TODAS las materias")
    print("=" * 55)
    print(en_todas_las_materias())                   # {'Felipe'}

    print("\nEJERCICIO 2 — Todos los estudiantes")
    print(sorted(todos_los_estudiantes()))

    print("\nEJERCICIO 3 — Solo en matemáticas")
    print(solo_matematicas())                        # {'Carlos', 'Elena', 'Gabriel'}

    print("\nEJERCICIO 4 — Mat o Fis, sin Química")
    print(mat_o_fis_sin_quimica())

    print("\nEJERCICIO 5 — ¿Física ⊆ (Mat ∪ Química)?")
    print(fisica_es_subconjunto())                   # True o False

    print("\nEJERCICIO 6 — Todos los lenguajes")
    print(sorted(todos_los_lenguajes()))

    print("\nEJERCICIO 7 — Solo backend")
    print(solo_backend())                            # {'Go', 'Ruby', 'PHP'}

    print("\nEJERCICIO 8 — En exactamente dos áreas")
    print(en_exactamente_dos())                      # {'Java'}

    print("\nEJERCICIO 9 — ¿Cuántas materias?")
    print(f"Felipe: {cuantas_materias('Felipe')}")   # 3
    print(f"Elena:  {cuantas_materias('Elena')}")    # 1
    print(f"Hugo:   {cuantas_materias('Hugo')}")     # 2

    print("\nEJERCICIO 10 — Comparten materia con Felipe")
    print(sorted(comparten_materia("Felipe")))
