import re 
from tkinter import messagebox
Clave=""
#filtro de diccionarios creado por Cristian Chacon 
def ventana_alerta(clave, valor, mensaje):
    global Clave
    messagebox.showerror("Error con el tipo de dato",mensaje)
    Clave=clave
    return 
def ventana_positiva(mensaje):
    messagebox.showinfo("Exito:",mensaje)
    return

def estaVacio(diccionario):
    for clave, valor in diccionario.items():
        if valor=="":
            mensaje_error=f"Advertencia el Campo: {clave.upper()} esta Vacio"
            ventana_alerta(clave, valor, mensaje_error)
            return False   
    return True 
    
def soloAlfabetico(diccionario): #Esa funcion solo acepta Alfabetico(Solo letras)
    
    patron=(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$")
    for clave, valor in diccionario.items():
        if not re.fullmatch(patron, valor):
            print(f"La clave: {clave} con el valor: {valor} es de tipo {type(valor)}")
            mensaje_error=f"Advertencia el campo: [{clave.upper()}]solo permite Caracteres [Alfabeticos]"
            ventana_alerta(clave,valor,mensaje_error)
            return False
    return True # solo si todo el diccionario es alfabetico devuelve True      

def soloNumerico(diccionario):
    patron=(r"^[0-9 ]+$")
    for clave ,valor in diccionario.items():
        if not re.fullmatch(patron, str(valor)):
            mensaje_error=f"Advertencia el campo:[{clave.upper()}]Admite solo numeros"
            print(f"la clave {clave} con el valor: {valor} es de tipo{type(valor)}")
            ventana_alerta(clave, valor ,mensaje_error)
            return False 
    return True

def alfaNumerico(diccionario):
    patron=r"^[A-Za-z0-9 ]+$"
    for clave, valor in diccionario.items():
        if not re.fullmatch(patron, valor):
            mensaje=f"El campo: {clave.upper()}solo acepta valores AlfaNumericos"
            ventana_alerta(clave, valor, mensaje)
            return False
    return True   
        


def documentoDNI(diccionario):
    patron_dni=r"^\d{8}[A-Za-z]$"                    
    for clave , valor in diccionario.items():
        if  not re.fullmatch(patron_dni, valor):
            mensaje_error=f"Advertencia  el campo :[{clave.upper()}] No cumple el formato requerido: DNI:58715098N" 
            ventana_alerta(clave,valor, mensaje_error)
            return False
    print("Comprobacion de DNI Correcta")           
    return True  


def documentoNIE(diccionario):
    patron_nie=r"^[XYZ]\d{7}[A-Za-z]$"
    for clave , valor in diccionario.items():
        if not re.fullmatch(patron_nie, valor):
            mensaje_error=f"Advertencia El campo: [{clave.upper()}] Admite para el formato NIE:Y8718509H" 
            ventana_alerta(clave,valor, mensaje_error)
            return False
    print("Comprobacion de Nie Correcta")           
    return True   


def fecha(diccionario):
    patron_fecha = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
    for clave , valor in diccionario.items():
        if not re.fullmatch(patron_fecha, valor):
            mensaje=f"el campo {clave.upper()}, El formato de fecha es [dd/mm/aaaa]"
            ventana_alerta(clave, valor, mensaje)
            return False
    return True     

def prueba():
    diccionario={"Nombre":"123456"}
    if not soloAlfabetico(diccionario):
        print("solo permite alfabetico")
        return
    print("esta correcto")
    exit()
