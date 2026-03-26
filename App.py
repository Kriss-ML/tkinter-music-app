import tkinter as tk
from tkinter import ttk
import filtro_datos as fil

class persona:
    def __init__(self, nombre, apellidos, dni, poblacion, pais ):
        self.nombre=nombre.title()
        self.apellidos=apellidos.title()
        self.dni=dni.upper()
        self.poblacion=poblacion.title()
        self.pais=pais.upper()
        
        
    
class gustos_musicales:
    def __init__(self, cancion, grupo, genero):
        self.cancion=cancion.title()
        self.grupo=grupo.title()
        self.genero=genero.upper()
        
    

class registro(persona,gustos_musicales):
        def __init__(self, nombre, apellidos, dni, poblacion, pais, cancion, grupo, genero):
         persona.__init__(self, nombre, apellidos, dni, poblacion, pais)
         gustos_musicales.__init__(self, cancion, grupo, genero)          
        
        def obtener_registro(self):
            return {"nombre":self.nombre,
                    "apellidos":self.apellidos,
                    "dni":self.dni,
                    "poblacion":self.poblacion,
                    "pais":self.pais,
                    "cancion":self.cancion,
                    "grupo":self.grupo,
                    "genero":self.genero
                    }          

    
    
class App:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.title("Registro de Datos Deusto Formacion, Ejercicio1 Modulo 5")
        ventana.resizable(False,False)
        ventana.config(bg="silver")
        ventana_ancho=800
        ventana_alto=580
        try:
            ancho_windows=ventana.winfo_screenwidth()
            alto_windows=ventana.winfo_screenheight()
            x=(ancho_windows//2)-(ventana_ancho//2)
            y=(alto_windows//2)-(ventana_alto//2)
            ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}") #esto es para centrar la ventana 
        except tk.TclError as e:
            print("..No se pudo centrar la ventana se requiere sistema operativo Windows")
            ventana.geometry(f"{ventana_ancho}x{ventana_alto}")
        self.generar_formulario()
    
    def limpiar(self):
        listatxt=self.lista_objetos_txt()
        for txt in listatxt.values():
            txt.delete(0, tk.END)
        self.txtnombre.focus_set()

    def cargar_datos(self):
        nombre_del_archivo="registro_gustos_musicales.txt"
        #limpiar los datos para insertar los nuevos
        for valores in self.tabla.get_children():
            self.tabla.delete(valores)
      
        with open (nombre_del_archivo, "r",encoding="utf-8") as archivo:
            try:
                for linea in archivo:
                    datos=linea.strip().split(",")
                    self.tabla.insert("", "end",values=datos)
                print("se han cargado los datos correctamente")
            except Exception as e:
                      
                print("Upps ha ocurrido un error:", e)
            return                    
    
    def guardar_registro_txt(self,registro_objeto):
        nombre_archivo="registro_gustos_musicales.txt"
        try:
            valores=registro_objeto.obtener_registro().values()
            print(valores)
            registro_en_linea=",".join(valores) + "\n"
            with open(nombre_archivo, mode="a", encoding="utf-8") as archivo:
                archivo.write(registro_en_linea)
            print("Se ha creado un nuevo registro")                
        

        except Exception as e:
            print(f"UPPS ha ocurrido un error: {e}")
        mensaje="Se ha creado un nuevo registro correctamente!"
        self.cargar_datos()
        self.limpiar()



    def generar_formulario(self):           
        frame_formulario=tk.Frame(ventana, width=385, height=200, bg="black")
        frame_formulario.grid(column=0, row=0, padx=5, pady=5)
        frame_formulario.grid_propagate(False)
        
        frame_formulario_musical=tk.Frame(ventana, width=385, height=200, bg="black")
        frame_formulario_musical.grid(column=1, row=0, pady=5, padx=5)
        frame_formulario_musical.grid_propagate(False)

        frame_datos=tk.Frame(ventana, width=790, height=355, bg="black")
        frame_datos.grid(column=0, row=1, pady=5, padx=5, columnspan=2)
        frame_datos.grid_propagate(False)
        frame_datos.grid_rowconfigure(0, weight=1)
        frame_datos.grid_columnconfigure(0, weight=1)
        #frame_scrollvar=tk.Frame(frame_datos, width bg="withe")
        #-----Objetos de Entrada y etiquetas---
        nombre_label= tk.Label(frame_formulario, text="Registro de Datos Personales", bg="black", fg="green4", font=("Arial",16,"bold"))
        nombre_label.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky="nsew")
        nombre_label= tk.Label(frame_formulario, text="Nombre:", bg="black", fg="green", font=("Arial",10,"bold"))
        nombre_label.grid(row=1, column=0, padx=5, pady=5,sticky="e" )
        self.txtnombre=tk.Entry(frame_formulario, width=20)
        self.txtnombre.grid(row=1, column=1, sticky="w")
        apellidos_label= tk.Label(frame_formulario, text="Apellidos:", bg="black", fg="green", font=("Arial",10,"bold"))
        apellidos_label.grid(row=2, column=0, padx=5, pady=5,sticky="e" )
        self.txtapellido=tk.Entry(frame_formulario, width=20)
        self.txtapellido.grid(row=2, column=1, sticky="w")
        dni_label= tk.Label(frame_formulario, text="DNI:", bg="black", fg="green", font=("Arial",10,"bold"))
        dni_label.grid(row=3, column=0, padx=5, pady=5,sticky="e" )
        self.txtdni=tk.Entry(frame_formulario, width=10, )
        self.txtdni.grid(row=3, column=1, sticky="w")        
        poblacion_label= tk.Label(frame_formulario, text="Poblacion:", bg="black", fg="green", font=("Arial",10,"bold"))
        poblacion_label.grid(row=4, column=0, padx=5, pady=5,sticky="e" )
        self.txtpoblacion=tk.Entry(frame_formulario, width=20)
        self.txtpoblacion.grid(row=4, column=1, sticky="w")
        pais_label= tk.Label(frame_formulario, text="Pais:", bg="black", fg="green", font=("Arial",10,"bold"))
        pais_label.grid(row=5, column=0, padx=5, pady=5,sticky="e" )
        self.txtpais=tk.Entry(frame_formulario, width=20)
        self.txtpais.grid(row=5, column=1, sticky="w")
        #-----[Gustos Musicales]-----
        titulo_gustos_musicales=tk.Label(frame_formulario_musical, text="Gustos Musicales", bg="black", fg="gold", font=("Arial",16,"bold") )
        titulo_gustos_musicales.grid(row=0, column=0, sticky="nsew", columnspan=3)
        cancion_label= tk.Label(frame_formulario_musical, text="Cancion Favorita:", bg="black", fg="gold", font=("Arial",10,"bold"))
        cancion_label.grid(row=1, column=0, padx=5, pady=5,sticky="e" )
        self.txtcancion=tk.Entry(frame_formulario_musical, width=20)
        self.txtcancion.grid(row=1, column=1, sticky="w")
        grupo_label= tk.Label(frame_formulario_musical, text="Grupo Musical:", bg="black", fg="gold", font=("Arial",10,"bold"))
        grupo_label.grid(row=2, column=0, padx=5, pady=5,sticky="e" )
        self.txtgrupo=tk.Entry(frame_formulario_musical, width=20)
        self.txtgrupo.grid(row=2, column=1, sticky="w")
        genero_label= tk.Label(frame_formulario_musical, text="Genero Musical:", bg="black", fg="gold", font=("Arial",10,"bold"))
        genero_label.grid(row=3, column=0, padx=5, pady=5,sticky="e" )
        #-------------[Combobox]----------
        lista_de_generos=["Romanticas", "Rock", "Metal", "Reggueton", "Bachata","Pop", "Flamenco", "Rumba", "Salsa", "Hip-Hop", "Trap", "Electrónica" ]
        self.combo_genero= ttk.Combobox(frame_formulario_musical, value=lista_de_generos)
        self.combo_genero.grid(row=3, column=1, sticky="w")       
        boton_agregar=tk.Button(frame_formulario_musical, text="Agregar", command=self.agregar_datos)
        boton_agregar.grid(row=4, column=0, pady=10)
        #---------------[self.tabla]-----------------
        columnas=["nombre","apellidos", "dni", "poblacion", "pais", "cancion","grupo","genero"]
        ancho_columna=95
        self.tabla=ttk.Treeview(frame_datos, height=10, columns=columnas, show="headings", selectmode="browse" )
        self.tabla.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.heading("dni", text="DNI")
        self.tabla.heading("poblacion", text="Poblacion")
        self.tabla.heading("pais", text="Pais")
        self.tabla.heading("cancion", text="Cancion_fav.")
        self.tabla.heading("grupo", text="Grupo_fav.")
        self.tabla.heading("genero", text="Genero_fav.")
        #----se usa el for para no repetir el codigo donde cada columna contiene la misma configuracion 
        for columna in columnas:
            self.tabla.column(columna,anchor=tk.CENTER, width=ancho_columna, minwidth=ancho_columna, stretch=tk.NO)
        self.tabla.grid_propagate(False)
        self.tabla.grid_rowconfigure(0, weight=1)
        self.tabla.grid_columnconfigure(0, weight=1)
    #--------ScrollVar---------
        scrollbar_vertical = ttk.Scrollbar(frame_datos, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.grid(row=0, column=1, sticky="ns")      
        #al generar la tabla llama al archivo txt para cargarla con los datos ingresados  
       
        self.cargar_datos()  

    def lista_objetos_txt(self):
        return  {"nombre":self.txtnombre,
                "apellidos":self.txtapellido,
                "dni":self.txtdni,
                "poblacion":self.txtpoblacion,
                "pais":self.txtpais,
                "cancion":self.txtcancion,
                "grupo":self.txtgrupo,
                "genero":self.combo_genero
        }
    #Aqui extra los datos de los objetos uno a uno de la lista de objetos clave valor        
    def extraer_datos(self):
        lista_objetos=self.lista_objetos_txt()
        datos={}
        for clave, valor in lista_objetos.items():
            datos[clave]= valor.get()
            
        return datos
    
    def agregar_datos(self):#--el filtro de modulo creado solo funciona con diccionarios.    
        datos=self.extraer_datos()
        
        if not fil.estaVacio(datos):#Filtro para las cajas de texto si estan vacias 
            self.enfoque_de_caja()
            return
        #----se crea un diccionario temporar para comprobar todos los datos que sean Alfabetico
        diccionario_sin_nie= {clave: valor for clave, valor in datos.items() if clave != "dni"}
        print(diccionario_sin_nie)
        if not fil.soloAlfabetico(diccionario_sin_nie):     
            self.enfoque_de_caja()
            return
       
        solo_dni={"dni":datos.get("dni")}#--se crea un diccionario solo con el dato nie para comprobarlo
                
        if not fil.documentoDNI(solo_dni):
            self.enfoque_de_caja()
            return
        try:
            agregar_registro_nuevo=registro(
                nombre=datos["nombre"],
                apellidos=datos["apellidos"],
                poblacion=datos["poblacion"],
                dni=datos["dni"],
                pais=datos["pais"],
                cancion=datos["cancion"],
                grupo=datos["grupo"],
                genero=datos["genero"]
                )
            print(f"Los datos a guardar son:{agregar_registro_nuevo.obtener_registro()}")
        except Exception as e:
            print("UUPS Ha ocurrido un error:",e)
            return                               
                           
        self.guardar_registro_txt(agregar_registro_nuevo)

            

           
        #----esta funcion hace el enfoque en la caja actua dependiendo de la clave que se obtiene 
        #----en el modulo filtrar datos
    def enfoque_de_caja(self):
        clave=fil.Clave
        lista=self.lista_objetos_txt()
        lista[clave].focus_set()
        lista[clave].select_range(0,tk.END)       
    
    
if __name__=="__main__":
    ventana=tk.Tk()
    app=App(ventana)
    ventana.mainloop()

