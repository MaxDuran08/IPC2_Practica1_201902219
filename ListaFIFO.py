class Nodo:

    def __init__(self,Orden,NombreCliente,Pizzas,TiempoOrden,TiempoPedido,SegundoEntrada,MinutoEntrada,HorasEntrada):
        self.Orden=Orden
        self.NombreCliente=NombreCliente
        self.Pizzas=Pizzas
        self.TiempoOrden=TiempoOrden
        self.TiempoPedido=TiempoPedido
        self.SegundosEntrada=SegundoEntrada
        self.MinutosEntrada=MinutoEntrada
        self.HorasEntrada=HorasEntrada
        self.SiguienteOrden=None

    def __str__(self):
        return str(self.Orden)+" ,"+str(self.NombreCliente)+" ,"+str(self.Pizzas)+" ,"+str(self.TiempoOrden)+" ,"+str(self.TiempoPedido)+" ,"+str(self.SegundosEntrada)+" ,"+str(self.MinutosEntrada)

class ListaFIFO:
    
    def __init__(self):
        self.Primero=None
        self.Tamaño=0
        

    def Push(self,Orden,NombreCliente,Pizzas,TiempoOrden,TiempoPedido,SegundoEntrada,MinutoEntrada,HorasEntrada):
        
        NuevoNodo=Nodo(Orden,NombreCliente,Pizzas,TiempoOrden,TiempoPedido,SegundoEntrada,MinutoEntrada,HorasEntrada)
        if self.Tamaño==0:
            self.Primero=NuevoNodo
        else:
            Actual=self.Primero
            while Actual.SiguienteOrden!=None:
                Actual=Actual.SiguienteOrden
            Actual.SiguienteOrden=NuevoNodo
        self.Tamaño+=1
    
    def Pop(self):
        if self.Tamaño!=0:
            self.Primero=self.Primero.SiguienteOrden
        else:
            self.Primero=None
        self.Tamaño-=1
        
    def __len__(self):
        return self.Tamaño

    def __str__(self):
        String="["
        Actual=self.Primero
        while Actual!=None:
            #String+="("+str(Actual.Posicion)+")"
            String+=str(Actual)
            if Actual.SiguienteOrden!=None:
                String+=str(", ")
            Actual=Actual.SiguienteOrden
        String+="]"
        return String


