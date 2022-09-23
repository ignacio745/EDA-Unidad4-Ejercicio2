from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Arbol import Arbol


class Arbol:
    __elemento: None
    __izq: Arbol
    __der: Arbol


    def __init__(self) -> None:
        self.__elemento = None
        self.__izq = None
        self.__der = None

    
    def vacio(self):
        return self.__elemento == None

    
    def getElemento(self):
        return self.__elemento
    

    def cambiarHijo(self, antiguoHijo, nuevoHijo):
        if self.__izq is antiguoHijo:
            self.__izq = nuevoHijo
        elif self.__der is antiguoHijo:
            self.__der = nuevoHijo
        else:
            raise Exception("El arbol {0} no tiene como hijo al arbol {1}".format(self, antiguoHijo))
            
    

    def insertar(self, elemento):
        if self.__elemento == None:
            self.__elemento = elemento
            self.__izq = Arbol()
            self.__der = Arbol()
        
        else:
            if elemento < self.__elemento:
                self.__izq.insertar(elemento)
            
            elif self.__elemento < elemento:
                self.__der.insertar(elemento)
            
            elif elemento == self.__elemento:
                raise Exception("El elemento {0} ya existe".format(elemento))
                
    

    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der
    
    def setDer(self, nuevoDer:Arbol):
        self.__der = nuevoDer
    
    def setIzq(self, nuevoIzq:Arbol):
        self.__izq = nuevoIzq
    
    def suprimir(self, elemento, padre:(Arbol | None)=None):
        if self.__elemento == None:
            raise Exception("[ERROR] El elemento {0} no esta en el arbol".format(elemento))
        if self.__elemento == elemento:

            if self.__izq.vacio() and self.__der.vacio():
                self.__elemento = None
                self.__izq = None
                self.__der = None

            elif self.__izq.vacio() and padre != None:
                padre.cambiarHijo(self, self.__der)

            elif self.__der.vacio() and padre != None:
                padre.cambiarHijo(self, self.__izq)

            else:
                anterior = self
                infimo = self.__der

                while not infimo.getIzq().vacio():
                    anterior = infimo
                    infimo = infimo.getIzq()
                self.__elemento = infimo.getElemento()
                anterior.cambiarHijo(infimo, infimo.getDer())


        elif elemento < self.__elemento:
            self.__izq.suprimir(elemento, self)
        elif self.__elemento < elemento:
            self.__der.suprimir(elemento, self)
        
                



    
    def buscar(self, elemento):
        if self.__elemento == None:
            raise Exception("El elemento {0} no se encuentra en el arbol".format(elemento))
        
        if self.__elemento == elemento:
            return self.__elemento
        
        elif elemento < self.__elemento:
            return self.__izq.buscar(elemento)
        
        elif self.__elemento < elemento:
            return self.__der.buscar(elemento)



    def inorden(self):
        if self.__elemento != None:
            self.__izq.inorden()
            print(self.__elemento)
            self.__der.inorden()


    
    def preorden(self):
        if self.__elemento != None:
            print(self.__elemento)
            self.__izq.preorden()
            self.__der.preorden()



    def postorden(self):
        if self.__elemento != None:
            self.__izq.postorden()
            self.__der.postorden()
            print(self.__elemento)
    


    def nivel(self, elemento, nivelAnterior = 0):
        if self.__elemento == None:
            raise Exception("No existe el elemento {0} en el arbol".format(elemento))

        if self.__elemento == elemento:
            return nivelAnterior + 1

        elif elemento < self.__elemento:
            return self.__izq.nivel(elemento, nivelAnterior+1)

        elif self.__elemento < elemento:
            return self.__der.nivel(elemento, nivelAnterior+1)



    def hoja(self, elemento):
        if self.__elemento == elemento:
            if self.__izq.vacio() and self.__der.vacio():
                return True
            else:
                return False
        
        else:
            if elemento < self.__elemento:
                return self.__izq.hoja(elemento)
            elif self.__elemento < elemento:
                return self.__der.hoja(elemento)
    


    def hijo(self, elementoHijo, elementoPadre):
        if self.__elemento == elementoPadre:
            if self.__izq.getElemento() == elementoHijo or self.__der.getElemento() == elementoHijo:
                return True
            else:
                return False
        
        else:
            if elementoPadre < self.__elemento and not self.__izq.vacio():
                return self.__izq.hijo(elementoHijo, elementoPadre)

            elif self.__elemento < elementoPadre and not self.__der.vacio():
                return self.__der.hijo(elementoHijo, elementoPadre)
            
            else:
                return False



    def padre(self, elementoPadre, elementoHijo):
        return self.hijo(elementoHijo, elementoPadre)
    


    def altura(self):
        if self.__izq != None:
            alturaSegunIzq = self.__izq.altura() + 1
        else:
            alturaSegunIzq = 0
        
        if self.__der != None:
            alturaSegunDer = self.__der.altura() + 1
        else:
            alturaSegunDer = 0
        
        return max(alturaSegunIzq, alturaSegunDer)

    def frontera(self):
        if self.__izq.vacio() and self.__der.vacio():
            print(self.__elemento)
        else:
            if not self.__izq.vacio():
                self.__izq.frontera()
            if not self.__der.vacio():
                self.__der.frontera()
