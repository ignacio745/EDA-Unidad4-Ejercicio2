from Arbol import Arbol

if __name__ == "__main__":
    unArbol = Arbol()
    unArbol.insertar(5)
    unArbol.insertar(10)
    unArbol.insertar(7)
    unArbol.insertar(12)
    unArbol.insertar(15)
    unArbol.insertar(2)
    unArbol.insertar(1)
    unArbol.insertar(3)

    unArbol.suprimir(10)

    unArbol.frontera()
