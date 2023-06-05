class Nodo():
    def __init__ (self, valor,padre = None):
        self.valor = valor
        self.padre = padre
        self.izquierda = None
        self.derecha = None
    def __str__(self):
        return str(self.valor)

class ArbolBinario():

    def __init__(self,raiz=None):
        self.raiz = raiz
        self.len = 0

    def insertar(self, valor):
        Nuevo = Nodo(valor)
        self.len+=1

        if self.len == 1:
            self.raiz = Nuevo  
            return False  

        padre = self.raiz
        while True:

            if Nuevo.valor < padre.valor and padre.izquierda == None:
                Nuevo.padre = padre
                padre.izquierda = Nuevo
                return True

            elif Nuevo.valor < padre.valor:
                padre = padre.izquierda

            elif Nuevo.valor > padre.valor and padre.derecha == None:
                Nuevo.padre = padre
                padre.derecha = Nuevo
                return True

            elif Nuevo.valor > padre.valor:
                padre = padre.derecha

            else:
                self.size -= 1
                return False

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

        print(raiz.valor)
        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)


    def EnOrden(self,raiz):
        if self.len == 0:
            return

        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        print(raiz.valor)

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)

    def PosOrden(self,raiz):
        if self.len == 0:
            return

        if raiz.izquierda != None:
            self.PreOrden(raiz.izquierda)

        if raiz.derecha != None:
            self.PreOrden(raiz.derecha)

        print(raiz.valor)


a = ArbolBinario()
a.insertar(1)
a.insertar(2)
a.insertar(3)
print(a.busque(3))
a.PreOrden(a.raiz)


        
        


