class Nodo(): #clase "auxiliar" para guardar los nodos y su informacion, asi como en las diapositivas del profe
    def __init__ (self, valor,padre = None):
        self.valor = valor
        self.padre = padre
        self.izquierda = None
        self.derecha = None
        self.h = 0
    def __str__(self):
        return str(self.valor)

class ArbolBinario():

    def __init__(self,raiz=None):
        self.len = 0
        self.h = 0
        self._listaRetorno = []
        self._hojas = 0
        self._hijos = 0
        self._racimo = 0
        if raiz == None:
            self.raiz = None
        elif type(raiz) == int:
            self.raiz = None
        else:
            self.raiz = None
            self.insertar(raiz)
        

    def _insertarAux(self, valor):
        Nuevo = Nodo(valor)
        self.len+=1

        if self.len == 1:
            self.raiz = Nuevo
            self.h = 1
            Nuevo.h = 1
            return False  

        padre = self.raiz
        aux = 2 #1 de la raiz y 1 porque el nodo no cuenta la vez que pasa por el hijo
        while True:

            if Nuevo.valor < padre.valor and padre.izquierda == None:
                Nuevo.padre = padre
                padre.izquierda = Nuevo
                Nuevo.h = aux
                if aux>self.h:
                    self.h = aux
                return True

            elif Nuevo.valor < padre.valor:
                padre = padre.izquierda

            elif Nuevo.valor > padre.valor and padre.derecha == None:
                Nuevo.padre = padre
                padre.derecha = Nuevo
                if aux>self.h:
                    self.h = aux 
                Nuevo.h = aux
                return True

            elif Nuevo.valor > padre.valor:
                padre = padre.derecha

            else:
                self.size -= 1
                return False
            aux += 1


    def insertar(self, valores): #eficiencia O(N*h)
        for valor in valores: #O(N)
            self._insertarAux(valor) #O(h)


    def busque(self, valor):
        nodo = self.raiz
        while nodo.valor != valor:
            if valor < nodo.valor and nodo.izquierda != None:
                nodo = nodo.izquierda
            elif valor > nodo.valor and nodo.derecha != None:
                nodo = nodo.derecha
            else:
                return False
        return nodo    


    def PreOrden(self,raiz):
        if self.len == 0:
            return

        self._listaRetorno+=[raiz.valor]
        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)
        
        
        return self._listaRetorno

    def EnOrden(self,raiz):
        if self.len == 0:
            return

        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        self._listaRetorno+=[raiz.valor]

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)
        
        return self._listaRetorno
    
    def EnOrdenInv(self,raiz):
        if self.len == 0:
            return

        if raiz.derecha != None:
            self.EnOrdenInv(raiz.derecha)

        self._listaRetorno+=[raiz.valor]

        if raiz.izquierda != None:
            self.EnOrdenInv(raiz.izquierda)

        return self._listaRetorno

    def PosOrden(self,raiz):
        if self.len == 0:
            return

        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)

        self._listaRetorno+=[raiz.valor]

        
        return self._listaRetorno
    
    def contarhojas(self,raiz):
        if self.len == 0:
            return

        if raiz.derecha ==None and raiz.izquierda == None:
            self._hojas += 1

        if raiz.izquierda != None:
            self.contarhojas(raiz.izquierda)

        if raiz.derecha != None:
            self.contarhojas(raiz.derecha)
        return self._hojas
    
    def contarHijos(self,raiz):
        if self.len == 0:
            return

        if (raiz.derecha == None) ^ (raiz.izquierda == None):
            self._hijos += 1

        if raiz.izquierda != None:
            self.contarHijos(raiz.izquierda)

        if raiz.derecha != None:
            self.contarHijos(raiz.derecha)
        return self._hijos
    
    def VerificarRacimo(self,raiz):
        if self.len == 0:
            return 

        if self.h == raiz.h:
            self._racimo += 1 
        if raiz.izquierda != None:
            self.VerificarRacimo(raiz.izquierda)

        if raiz.derecha != None:
            self.VerificarRacimo(raiz.derecha)
        return 2**(self.h-1) == self._racimo



a = ArbolBinario([30, 20])
a.insertar([40, 10, 50, 25, 35])

print(a.PreOrden(a.raiz))




        
        


