from numpy import append
from ListaFIFO import ListaFIFO
from ListaEnlazada import ListaEnlazada
import time
from Graficar import Graficar

class Main():
    def __init__(self):
        self.ListaOrdenes=ListaFIFO()
        self.nOrdenes=1
        self.idOrdenes=1
        self.Correr()

    def Correr(self):
        self.MenuPrincipal()
        while True:
            Opcion=self.ObtenerOpcion(1)
            print("|___/\/\____/\/\/\____|")            
            if Opcion==1:
                self.MenuHacerOrden()
            elif Opcion==2:
                self.MenuEntregarOrder()
            elif Opcion==3:
                self.MenuDesarrollador()
            elif Opcion==0:
                break
            else:
                pizza="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁|
⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀|
⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|"""
                print(pizza)
                print("| 1. Hacer Orden      |")
                print("| 2. Entregar Orden   |")
                print("| 3. Desarrollador    |")
                print("| 0. Salir            |")
                print("|                     |")
                print("|**Ingrese una opcion |")
                print("|     que sea valida**|")
                print("|              ____   |")
                print("|__/\_________/    \_/")
            self.MenuPrincipal()

    def MenuPrincipal(self):
        pizza="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁|
⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀|
⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|"""
        print(pizza)
        print("| 1. Hacer Orden      |")
        print("| 2. Entregar Orden   |")
        print("| 3. Desarrollador    |")
        print("| 0. Salir            |")
        print("|              ____   |")
        print("|__/\_________/    \_/")

    def numero(self,String):
        while True:
            try:
                print(String)
                print("| ",end="")
                valor=int(input())
                print("|                     |")
                if valor<1:
                    print("|                     |")
                    print("| **Ingrese un numero |")
                    print("|    mayor a cero**   |")
                    print("|                     |")
                else:
                    return valor
            except:
                print("|                     |")
                print("|**Ingrese un numero  |")
                print("|  no ingrese letras**|")
                print("|                     |")

    def ObtenerOpcion(self,menu):
        while True:
            try:
                if menu!=1:
                    print("| Opcion: ",end="")
                    opcion=int(input())
                    return opcion   
                else:
                    print(" _____________________")
                    print("| Opcion: ",end="")
                    opcion=int(input())
                    return opcion 
            except:
                if menu==2:
                    print("|                     |")
                    print("|  **Ingrese una      |")
                    print("|    opcion valida**  |")
                    print("|                     |")
                    print("| Ingredientes:       |")
                    print("|                     |")
                    print("| 1. Pepperoni        |")
                    print("| 2. Salchicha        |")
                    print("| 3. Carne            |")
                    print("| 4. Queso            |")
                    print("| 5. Piña             |")
                    print("|                     |")
                elif menu==1:
                    pizza="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁|
⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀|
⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|"""
                    print("|___/\/\____/\/\/\____|") 
                    print(pizza)
                    print("| 1. Hacer Orden      |")
                    print("| 2. Entregar Orden   |")
                    print("| 3. Desarrollador    |")
                    print("| 0. Salir            |")
                    print("|                     |")
                    print("|**Ingrese una opcion |")
                    print("|     que sea valida**|")
                    print("|              ____   |")
                    print("|__/\_________/    \_/")

    def MenuHacerOrden(self):
        print("            ________")
        print("|\_/\______/        \_")
        print("|                     |")
        print("| Ingrese los datos   |")
        print("|                     |")
        print("| Su nombre:          |")
        print("| ",end="")
        nombreCliente=input()
        print("|                     |")
        nPizzas=self.numero("| Cantidad de pizzas: |")
        TiempoPizzasTotal=0
        SegundosInicioPedido=int(time.strftime("%S",time.localtime()))
        MinutosInicioPedido=int(time.strftime("%M",time.localtime()))
        SegundosSalePedido=0
        MinutosSalePedido=0
        Pizzas=ListaEnlazada()
        for i in range(nPizzas):
            Pizza=ListaEnlazada()
            NombrePizza="Pizza #"+str(i+1)
            Pizza.Append(NombrePizza)
            while True:
                print("| ==> ",end="")
                print(NombrePizza)
                print("| Ingredientes:       |")
                print("|                     |")
                print("| 1. Pepperoni        |")
                print("| 2. Salchicha        |")
                print("| 3. Carne            |")
                print("| 4. Queso            |")
                print("| 5. Piña             |")
                print("|                     |")
                Opcion=self.ObtenerOpcion(2)
                if Opcion==1:                    
                    TiempoPizzasTotal+=3
                    Ingrediente=ListaEnlazada()
                    Ingrediente.Append("Pepperoni")
                    Ingrediente.Append(3)
                    Pizza.Append(Ingrediente)
                    print("|                     |")
                    print("| Se agrego: Pepperoni|")
                    print("|                     |")
                    break
                elif Opcion==2:
                    TiempoPizzasTotal+=4
                    Ingrediente=ListaEnlazada()
                    Ingrediente.Append("Salchica")
                    Ingrediente.Append(4)
                    Pizza.Append(Ingrediente)
                    print("|                     |")
                    print("| Se agrego: Salchicha|")
                    print("|                     |")
                    break
                elif Opcion==3:                
                    TiempoPizzasTotal+=10
                    Ingrediente=ListaEnlazada()
                    Ingrediente.Append("Carne")
                    Ingrediente.Append(10)
                    Pizza.Append(Ingrediente)
                    print("|                     |")
                    print("| Se agrego: Carne    |")
                    print("|                     |")
                    break                
                elif Opcion==4:
                    TiempoPizzasTotal+=5
                    Ingrediente=ListaEnlazada()
                    Ingrediente.Append("Queso")
                    Ingrediente.Append(5)
                    Pizza.Append(Ingrediente)
                    print("|                     |")
                    print("| Se agrego: Queso    |")
                    print("|                     |")
                    break
                elif Opcion==5:
                    TiempoPizzasTotal+=2
                    Ingrediente=ListaEnlazada()
                    Ingrediente.Append("Piña")
                    Ingrediente.Append(2)
                    Pizza.Append(Ingrediente)
                    print("|                     |")
                    print("| Se agrego: Piña     |")
                    print("|                     |")
                    break
                else:
                    print("|                     |")
                    print("|**Ingrese una opcion |")
                    print("|     que sea valida**|")
                    print("|                     |")
            Pizzas.Append(Pizza)
            SegundosSalePedido=int(time.strftime("%S",time.localtime()))
            MinutosSalePedido=int(time.strftime("%M",time.localtime()))
            HorasSalePedido=int(time.strftime("%H",time.localtime()))
        TotalSegundosPedido=SegundosSalePedido-SegundosInicioPedido
        TotalMinutosPedido=MinutosSalePedido-MinutosInicioPedido
        TiempoPedido=(float(TotalSegundosPedido)/60)+float(TotalMinutosPedido)
        nombreOrden="Orden #"+str(self.idOrdenes)
        self.ListaOrdenes.Push(nombreOrden,nombreCliente,Pizzas,TiempoPizzasTotal,TiempoPedido,SegundosSalePedido,MinutosSalePedido,HorasSalePedido)
        self.nOrdenes+=1
        self.idOrdenes+=1
        #print(self.ListaOrdenes)
        Graficar(self.GenerarListaGrafica())
        print("| "+str(nombreOrden))
        print("| Cliente:            |")
        print("| "+str(nombreCliente))
        print("| Efectuada a la hora:|")
        print("| "+str(time.strftime("%H:%M:%S",time.localtime())))
        print("|                     |")
        print("|__/\_________/\/\____|")

    def MenuEntregarOrder(self):
        print(" __        ___________")
        print("|  \______/           |")
        print("|                     |")
        if len(self.ListaOrdenes)!=0:
            self.CalcularSalida(self.ListaOrdenes.Primero)
            print("| Se entregara:       |")
            print("| ",end="")
            print(self.ListaOrdenes.Primero.Orden)
            print("|                     |")
            print("| Del cliente:        |")
            print("| ",end="")
            print(self.ListaOrdenes.Primero.NombreCliente)
            print("|                     |")
            print("| La orden estuvo en  |")
            print("| cola durante:       |")
            self.CalcularSalida(self.ListaOrdenes.Primero)
            self.ListaOrdenes.Pop()
            self.nOrdenes-=1
            if (self.nOrdenes-1)>0:
                Graficar(self.GenerarListaGrafica())
        else:
            print("|  **No hay ordenes   |")
            print("|     en espera**     |")
        print("|           ______    |")
        print(" \_________/      \___|")

    def MenuDesarrollador(self):
        print("Ordenes en cola: "+str(self.nOrdenes-1))
        Actual=self.ListaOrdenes.Primero
        if int(self.nOrdenes-1)>0:
            print("**=========================================**")
            print("|| ORDENES:                                ||")
            for i in range(self.nOrdenes-1):
                print("**=========================================**")
                print("||                                         ||")
                print(Actual.Orden)
                print("Nombre del cliente: "+str(Actual.NombreCliente))
                for i in range(len(Actual.Pizzas)):
                    print(Actual.Pizzas[i][0])
                    print("Ingrediente: "+str(Actual.Pizzas[i][1][0]))
                    print("Minutos de preparado: "+str(Actual.Pizzas[i][1][1]))
                print("Tiempo de preparacion para las pizzas:"+str(Actual.TiempoOrden))
                print("Tiempo que paso el usuario haciendo su pedido: "+str(Actual.TiempoPedido*60)+" minutos")
                print("Se genero el pedido en el minuto: "+str(Actual.HorasEntrada)+":"+str(Actual.MinutosEntrada)+"."+str(Actual.SegundosEntrada))
                Actual=Actual.SiguienteOrden
    
    def CalcularSalida(self,O):
        HoraActual=int(time.strftime("%H",time.localtime()))
        MinutoActual=int(time.strftime("%M",time.localtime()))
        SegundoActual=int(time.strftime("%S",time.localtime()))


        TiempoPedido=float(O.TiempoPedido)
        Tiempo1=TiempoPedido
        minutosPedido=int(Tiempo1)
        segundosPedido=int((Tiempo1-int(Tiempo1))*60)

        SegundosT=SegundoActual+segundosPedido-O.SegundosEntrada
        MinutosT=MinutoActual+O.TiempoOrden+minutosPedido-O.MinutosEntrada
        HoraT=HoraActual - O.HorasEntrada

        #print("creacion de pizzas:"+str(O.TiempoOrden))
        #print("minuto actual-Entrada:"+str(MinutoActual-O.MinutosEntrada))
        #print(minutosPedido)
        #print(str(HoraT)+":"+str(MinutosT)+":"+str(SegundosT))

        while MinutosT>59:
            HoraT+=1
            MinutosT-=60
            while SegundosT>59:
                MinutosT+=1
                SegundosT-=60
        Hora=""
        keyHora=False
        if HoraT>0:
            KeyHora=True
            if Hora>9:
                Hora+=str(HoraT)+":"
            else:
                Hora+="0"+str(HoraT)+":"
        if MinutosT>9:
            Hora+=str(MinutosT)+":"
        else:    
            if keyHora:
                Hora+="0"+str(MinutosT)+":"
            else:
                Hora+=str(MinutosT)+":"
        if SegundosT>9:
            Hora+=str(SegundosT)
        else:
            Hora+="0"+str(SegundosT)

        if keyHora:
            Hora+=" horas"
        else:
            Hora+=" minutos"
        print("| ",end="")
        print(Hora)

    def GenerarListaGrafica(self):
        Lista=ListaEnlazada()
        Actual=self.ListaOrdenes.Primero
        for i in range(self.nOrdenes-1):
            ListaTemp=ListaEnlazada()
            ListaTemp.Append(Actual.Orden)
            ListaTemp.Append(Actual.NombreCliente)
            """for i in range(len(Actual.Pizzas)):
                ListaTemp2=ListaEnlazada()
                ListaTemp2.Append(Actual.Pizzas[i][0])
                ListaTemp2.Append(Actual.Pizzas[i][1][0])
                ListaTemp.Append(ListaTemp2)"""
            ListaTemp.Append(Actual.Pizzas)
            Lista.Append(ListaTemp)
            Actual=Actual.SiguienteOrden
        return Lista
        

            
Main()
Li=ListaEnlazada()
Li.Append("x")
Li.Append("y")
Li.Append("z")
cont=len(Li)-1
while cont>-1:
    if cont==(len(Li)-1):
        print("Ultimo:")
        print(Li[cont])
    elif cont==0:
        print("Primero:")
        print(Li[cont])
    else:
        print(Li[cont])
    cont-=1




