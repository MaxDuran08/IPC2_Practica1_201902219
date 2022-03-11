import os
from os import system,startfile
import pathlib
import graphviz
class Graficar:
    def __init__(self,Lista):
        self.Lista=Lista
        self.n=""
        self.Crear()
    
    def Crear(self):
        Ruta=self.Calcular()
        RutaPng="Grafica"+str(self.n)

        text="""digraph L{
    node[shape=box fontname="Arial" style=filled]
    bgcolor="white"
    subgraph cluster1{
        label = Cola
        fontname="Arial"
        bgcolor = lightseagreen\n"""
        for i in range(len(self.Lista)):
            info=str(self.Lista[i][0])+"\nCliente: "+str(self.Lista[i][1])+"\n"+"Pizzas: "
            for j in range(len(self.Lista[i][2])):
                info+="\n"+str(self.Lista[i][2][j][0])+" de "+str(self.Lista[i][2][j][1][0])
            text+=str(self.Lista[i][0]).replace(" ","_").replace("#","")+"""[label=\""""+info+"""\",group=1,fillcolor=springgreen3,fontcolor=black];\n"""
        cont=len(self.Lista)-1
        while cont>-1:
            if cont==0:
                text+=str(self.Lista[cont][0]).replace(" ","_").replace("#","")+";"
            else:
                text+=str(self.Lista[cont][0]).replace(" ","_").replace("#","")+"->"
            cont-=1
        text+="""\nx[label="Siguiente en salir",color=lightseagreen]\n{rank=same"""
        for i in range(len(self.Lista)):
            text+=";"+str(self.Lista[i][0]).replace(" ","_").replace("#","")
        text+="}\nx->"+str(self.Lista[0][0]).replace(" ","_").replace("#","")+";\n"
        text+="""} }"""
        
        try:
            src = graphviz.Source(text,format="png")
            src.render(RutaPng)
            if os.path.exists(RutaPng):
                os.remove(RutaPng)
            startfile(str(RutaPng)+".png")
        except:
            print("[ERROR-GRAFICA]: Problema al abrir el archivo")

    def Calcular(self):
        n=None
        if self.n=="":
            n=0
            self.n=0
        else:
            n=self.n
        
        while True:
            ruta="Grafica"+str(n)+".png"
            Existe=os.path.exists(ruta)
            if Existe==True:
                n+=1
            else:
                self.n=n
                return ruta