"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un banco necesita un sistema para gestionar la cola de clientes en espera.
Los clientes tienen diferentes tipos de atención (preferencial, normal) y
se debe poder atender, consultar y gestionar la cola.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Cliente) con los atributos necesarios
2. Diseñar la clase Lista (Cola) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos
6. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Cliente):
   - Debe almacenar: nombre, tipo de atención (preferencial/normal), 
     tiempo estimado de atención en minutos
   - Debe poder enlazarse con otro cliente

b) Clase LISTA (Cola):
   - Los clientes preferenciales van al INICIO
   - Los clientes normales van al FINAL


PUNTO 2 (1.0): AGREGAR CLIENTE - RECURSIVO
------------------------------------------
Implementa un método para agregar un cliente.
- Si es preferencial: insertar al inicio de los preferenciales
- Si es normal: insertar al final de la cola
- OBLIGATORIO usar recursividad para encontrar la posición


PUNTO 3 (1.0): TIEMPO DE ESPERA - RECURSIVO
-------------------------------------------
Implementa un método que calcule el tiempo de espera de un cliente
dado su nombre (suma de tiempos de todos los que están antes).
- OBLIGATORIO usar recursividad
- Retorna -1 si el cliente no está en la cola


PUNTO 4 (1.0): ATENDER SIGUIENTE
--------------------------------
Implementa un método que retire y retorne el primer cliente de la cola.
- Retorna None si la cola está vacía


PUNTO 5 (1.0): CONTAR POR TIPO - RECURSIVO
------------------------------------------
Implementa un método que cuente cuántos clientes hay de cada tipo.
- OBLIGATORIO usar recursividad
- Retorna una tupla (preferenciales, normales)

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Cliente)


# PUNTO 1b: Clase Lista (Cola)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

"""
if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)
    
    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()
    
    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))
    
    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())
    
    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)
"""

#SOLUCION
#1)a- 
class Cliente:
    def __init__(self, nombre, tipo, tiempo):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo = tiempo
        self.siguiente = None

#1)b- 
class Cola:

    def __init__(self):
        self.inicio = None

    def visitar(self, nombre, tipo, tiempo):
        nuevo_cliente = Cliente(nombre, tipo, tiempo)
        nuevo_cliente.siguiente = self.inicio
        self.inicio = nuevo_cliente

    def tiempo_total(self):
        def recursivo(nodo):
            if nodo is None:
                return 0
            return nodo.tiempo + recursivo(nodo.siguiente)
        return recursivo(self.inicio)

    def buscar_por_dominio(self, texto):
        nueva = Historial()
        def recursivo(nodo):
            if nodo is None:
                return
            recursivo(nodo.siguiente)
            if texto in nodo.url:
                nueva.visitar(nodo.nombre, nodo.tipo, nodo.tiempo)
        recursivo(self.inicio)
        return nueva

    def eliminar_rapidas(self, x):
        def recursivo(nodo):
            if nodo is None:
                return None
            if nodo.tiempo < x:
                return recursivo(nodo.siguiente)
            nodo.siguiente = recursivo(nodo.siguiente)
            return nodo
        self.inicio = recursivo(self.final)

    def mostrar(self):
        actual = self.final
        i = 1
        while actual:
            print(f"{i}. {actual.nombre} | {actual.tipo} | {actual.tiempo} min")
            actual = actual.siguiente
            i += 1

#2)
 def agregar(self, nombre, tipo, tiempo):
        nuevo = Cliente(nombre, tipo, tiempo, preferencial )

        def recursivo(nodo):
            if nodo is None or nuevo.preferencial > nodo.preferencial:
            nuevo.siguiente = nodo
            return nuevo
            nodo.siguiente = recursivo(nodo.siguiente)
            return nodo

        self.inicio = recursivo(self.inicio)


#3)
def suma_condicion(self, nombre):
        return self._suma_cond_rec(self.inicio)

    def _suma_cond_rec(self, nodo):
        if nodo is None:
            return 0
            
        if nodo.nombre > 0:
            return nodo.nombre + self._suma_cond_rec(nodo.siguiente)

        return self._suma_cond_rec(nodo.siguiente)

#4)
    def buscar(self):
        return self._buscar_rec(self.inicio)

    def _buscar_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.prioridad == Cola:
            return nodo

        return self._buscar_rec(nodo.siguiente)


#5)
    def contar_tipo(self):
        def recursivo(nodo):
            if nodo is None:
                return 0
            suma = 1 if nodo.tipo else 0
            return suma + recursivo(nodo.siguiente)

        return recursivo(self,preferenciales, normales)

