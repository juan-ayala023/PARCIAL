class Pacientes:
    def __init__(self, nombre, edad, urgencia, atendido=False):
        self.nombre = nombre
        self.edad = edad
        self.urgencia = urgencia
        self.atendido = atendido
        self.siguiente = None

    def __str__(self):
        estado = "Atendido Correctamente" if self.atendido else "Sin atender"
        return f"[{estado}] {self.nombre} - Edad: {self.edad} - Urgencia: {self.urgencia}"
    
class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("  Sin pacientes")
            return
        
        while actual:
            print(f"  {actual}")
            actual = actual.siguiente

    def agregar(self, nombre, edad, urgencia):

        nuevo_paciente = Pacientes(nombre, edad, urgencia)

        self.cabeza = self._agregar_recursivo(nuevo_paciente, self.cabeza)
        
    def _agregar_recursivo(self, nuevo_paciente, actual):
        if actual is None or nuevo_paciente.urgencia > actual.urgencia:
            nuevo_paciente.siguiente = actual
            return nuevo_paciente
        
        actual.siguiente = self._agregar_recursivo(nuevo_paciente, actual.siguiente)
        return actual

    def contar_criticos(self):
       return self._contar_criticos_recursivo(self.cabeza)
    
    def _contar_criticos_recursivo(self, actual):
        if actual is None:
            return 0
        
        es_critico = 1 if (actual.urgencia >= 4 and not actual.atendido) else 0
        
        return es_critico + self._contar_criticos_recursivo(actual.siguiente)

    def filtrar(self, edad_minima):
        nueva_lista = ListaPacientes()
        
        nueva_lista.cabeza = self._filtrar_recursivo(self.cabeza, edad_minima)

        return nueva_lista

    def _filtrar_recursivo(self, actual, edad_minima):
       
        if actual is None:
            return None

        siguiente_filtrado = self._filtrar_recursivo(actual.siguiente, edad_minima)

        if actual.edad >= edad_minima:
            nuevo_nodo = Pacientes(actual.nombre, actual.edad, actual.urgencia, actual.atendido)
            nuevo_nodo.siguiente = siguiente_filtrado
            return nuevo_nodo
        else:
            return siguiente_filtrado
        
if __name__ == "__main__":
    lista = ListaPacientes()
    
    lista.agregar("Juan", 30, 3)
    lista.agregar("Juana", 85, 5)
    lista.agregar("Simon", 70, 3)
    lista.agregar("Esteban", 70, 4)
    lista.agregar("Laura", 37, 4)
    
    print("--- Pacientes (Ordenada por Urgencia) ---")
    lista.mostrar()

    print(f"\nPacientes críticos sin atender: {lista.contar_criticos()}")

    print("\n--- Lista Filtrada (Solo >= 60 años) ---")
    lista = lista.filtrar(60)
    lista.mostrar()
    
    print("\n--- Verificando Lista Original ---")
    lista.mostrar()