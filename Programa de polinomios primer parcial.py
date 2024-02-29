class Nodo:
    #Se inicializa un nodo de un polinomio con un coeficiente y un grado.
    def __init__(self, coeficiente, grado):
        self.coeficiente = coeficiente
        self.grado = grado
        self.siguiente = None
        self.anterior = None

class Polinomio:
    #se inicializa un polinomio vacío.
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_componente(self, coeficiente, grado):
        #Se agrega un término al polinomio
        nuevo_nodo = Nodo(coeficiente, grado)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            self.cola = nuevo_nodo

    def mostrar(self):
        #Muestra los términos del polinomio.
        actual = self.cabeza
        while actual is not None:
            print(f"{actual.coeficiente}x^{actual.grado}", end=" ")
            actual = actual.siguiente
        print()

    def sumar_restar(self, otro_polinomio, operacion):
        #Suma o resta dos polinomios y devuelve el resultado
        resultado = Polinomio()
        actual_a = self.cabeza
        actual_b = otro_polinomio.cabeza

        while actual_a is not None or actual_b is not None:
            coeficiente_a = actual_a.coeficiente if actual_a else 0
            coeficiente_b = actual_b.coeficiente if actual_b else 0
            grado = actual_a.grado if actual_a else (actual_b.grado if actual_b else 0)


            if operacion == 'suma':
                nuevo_coeficiente = coeficiente_a + coeficiente_b
            elif operacion == 'resta':
                nuevo_coeficiente = coeficiente_a - coeficiente_b

            grado = actual_a.grado if actual_a else actual_b.grado
            resultado.agregar_componente(nuevo_coeficiente, grado)

            if actual_a:
                actual_a = actual_a.siguiente
            if actual_b:
                actual_b = actual_b.siguiente

        return resultado

    def evaluar(self, valor):
        #Evalúa el polinomio para un valor dado.
        resultado = 0
        actual = self.cabeza
        while actual is not None:
            resultado += actual.coeficiente * (valor ** actual.grado)
            actual = actual.siguiente
        return resultado

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Ingresar términos del Polinomio A")
    print("2. Ingresar términos del Polinomio B")
    print("3. Mostrar Polinomios")
    print("4. Sumar Polinomios")
    print("5. Restar Polinomios")
    print("6. Evaluar Polinomio con un valor")
    print("7. Salir")

# Crear polinomios A y B
polinomio_a = Polinomio()
polinomio_b = Polinomio()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\nIngresar términos del Polinomio A:")
        while True:
            coeficiente = int(input("Ingrese el coeficiente (o 0 para finalizar): "))
            if coeficiente == 0:
                break
            grado = int(input("Ingrese el grado: "))
            polinomio_a.agregar_componente(coeficiente, grado)

    elif opcion == '2':
        print("\nIngresar términos del Polinomio B:")
        while True:
            coeficiente = int(input("Ingrese el coeficiente (o 0 para finalizar): "))
            if coeficiente == 0:
                break
            grado = int(input("Ingrese el grado: "))
            polinomio_b.agregar_componente(coeficiente, grado)

    elif opcion == '3':
        print("\nPolinomio A:")
        polinomio_a.mostrar()
        print("\nPolinomio B:")
        polinomio_b.mostrar()

    elif opcion == '4':
        resultado_suma = polinomio_a.sumar_restar(polinomio_b, 'suma')
        print("\nResultado de la suma:")
        resultado_suma.mostrar()

    elif opcion == '5':
        resultado_resta = polinomio_a.sumar_restar(polinomio_b, 'resta')
        print("\nResultado de la resta:")
        resultado_resta.mostrar()

    elif opcion == '6':
        polinomio = input("Seleccione el polinomio a evaluar (A o B): ")
        valor = int(input("Ingrese el valor para evaluar el polinomio: "))
        if polinomio.lower() == 'a':
            resultado_evaluacion = polinomio_a.evaluar(valor)
            print(f"\nResultado de evaluar el polinomio A en {valor}: {resultado_evaluacion}")
        elif polinomio.lower() == 'b':
            resultado_evaluacion = polinomio_b.evaluar(valor)
            print(f"\nResultado de evaluar el polinomio B en {valor}: {resultado_evaluacion}")
        else:
            print("Polinomio no válido.")

    elif opcion == '7':
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Inténtelo de nuevo.")

#Cada nodo en esta lista tiene un enlace que apunta al siguiente
#nodo en la secuencia. Esta estructura se utiliza para representar los términos de un polinomio
#Lista doblemente enlazada: Además del enlace al siguiente nodo, cada nodo tiene un enlace adicional que apunta al nodo anterior en la secuencia. Este tipo de lista 
#se utiliza para mantener un seguimiento del nodo anterior en el contexto de agregar nuevos términos al polinomio.
#Iván Ordoñez carnet: 1567523