# SCRIPT QUE DIBUJA TODA LA INTERFAZ GRÁFICA

# LIBRERIAS
import proceso
import numpy as np
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename

p_proc = proceso.procesamiento() # CREACIÓN DEL OBJETO PROCESO

# **********************************************
# FUNCIONES PARA LOS MENSAJES EMERGENTES
def mensaje_gracias():
    mb.showinfo("Agradecimientos",
                "Dr. Maricela Bravo Contreras\nDr. Juan Carlos Chang Wong\nMtro. José Miguel Zarate\nIng. Deyanira de la Peña Peña")


def mensaje_sobre():
    mb.showinfo("Acerca de...",
                "Proyecto de Integracion en Ingeniería en Computación\nPrograma elaborado por Edgar González Santos\nMatricula 208305804")


def mensaje_error_opcion():
    mb.showerror('Error', "Por favor seleccione una opción valida")


def mensaje_error_numero():
    mb.showerror('Error', "Número invalido")


def mensaje_error_dato():
    mb.showerror('Error', "Dato incorrecto")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN QUE ABRE EL BUSCADOR DE ARCHIVOS
def buscar_archivo():
    f = askopenfilename()
    print(f)
    p_proc.abrir_imagen(f)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN QUE VALIDA EL NÚMERO DEL CONTRASTE
def valida_contraste():
    try:
        res = int(n1.get())
        if res < 2:
            mb.showerror('Error', "Valor demasiado bajo para el contraste")
        elif res > 7:
            mb.showerror('Error', "Valor demasiado alto para el contraste")
        else:
            p_proc.contraste(res)
    except (ValueError, AttributeError):
        mensaje_error_numero()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN QUE VALIDA EL NÚMERO DEL DESENFOQUE
def valida_desenfoque():
    try:
        res = int(n2.get())
        if res < 2:
            mb.showerror("Error", 'Porcentaje de desenfoque muy pequeño')
        elif res > 15:
            mb.showerror("Error", 'Porcentaje de desenfoque muy grande')
        elif res % 2 == 0:
            mb.showerror("Error", 'Porcentaje par')
        else:
            p_proc.desenfoque(res)
    except (ValueError, AttributeError):
        mensaje_error_numero()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN QUE VALIDA EL NÚMERO DE LA ESCALA
def valida_escala():
    try:
        res = int(n3.get())
        opc = var.get()
        if opc == 'Micrometros':
            res = res*0.00001
            p_proc.opcion_escala(res)
        if opc == 'Nanometros':
            res = res*0.00000001
            p_proc.opcion_escala(res)
        if opc == 'Milimetros':
            res = res*0.1
            p_proc.opcion_escala(res)
        if opc == 'Pulgadas':
            res = res*2.54
            p_proc.opcion_escala(res)
        if opc == ' ':
            mensaje_error_opcion()
    except ValueError:
        mensaje_error_numero()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN QUE DESPLIEGA EL CONTEO CON EL TAMAÑO DE LA MUESTRA
def valida_conteo():
    try:
        res = int(n4.get())
        win1 = tk.Toplevel(root)
        win1.title('Conteo')
        win1.geometry("200x200+820+400")
        SBar = tk.Scrollbar(win1)
        SBar.pack(side=tk.RIGHT, fill='y')
        a, b = p_proc.conteo(res)
        TxBox = tk.Text(win1, yscrollcommand=SBar.set)
        TxBox.pack(expand=0, fill=tk.BOTH)
        for i, j, count in zip(a, np.roll(a, -1), b):
            TxBox.insert(tk.END, "{}-{}\t{}\n".format(i, j, count))
        SBar.config(command=TxBox.yview)
    except(AttributeError, ZeroDivisionError):
        mensaje_error_dato()


# **************************************************************************
# FUNCIÓN QUE MUESTRA LA VENTANA DE LA ESCALA
def ventana_escala():
    win = tk.Toplevel(root)
    win.title("Escala de la imagen")
    win.geometry('+100+160')
    win.iconbitmap("Icons/pro_Ima.ico")
    label = tk.Label(win, text="Ingrese la escala: ")
    label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.config(justify='center', textvariable=n3)
    var.set(' ')
    options = ['Micrometros', 'Nanometros', 'Milimetros', 'Pulgadas']
    option = tk.OptionMenu(win, var, *options)
    option.grid(row=0, column=2, padx=5, pady=5)
    option.config(justify='center', textvariable=var)
    button = tk.Button(win, text='OK', command=valida_escala)
    button.grid(row=0, column=3, padx=5, pady=5)


# **************************************************************************
# FUNCIÓN QUE MUESTRA LA VENTANA DE CONTRASTE
def ventana_contraste():
    win = tk.Toplevel(root)
    win.title("Contraste")
    win.geometry('+100+240')
    win.iconbitmap("Icons/pro_Ima.ico")
    label = tk.Label(win, text="Ingrese cantidad de contraste:")
    label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.config(justify='center', textvariable=n1)
    button = tk.Button(win, text='OK', command=valida_contraste)
    button.grid(row=0, column=2, padx=5, pady=5)
    return win


# **************************************************************************
# FUNCIÓN QUE MUESTRA LA VENTANA DEL DESENFOQUE
def ventana_desenfoque():
    win = tk.Toplevel(root)
    win.title("Desenfoque")
    win.geometry('+100+320')
    win.iconbitmap("Icons/pro_Ima.ico")
    label = tk.Label(win, text="Ingrese porcentaje de desenfoque:")
    label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.config(justify='center', textvariable=n2)
    button = tk.Button(win, text='OK', command=valida_desenfoque)
    button.grid(row=0, column=2, padx=5, pady=5)


# **************************************************************************
# FUNCIÓN QUE MUESTRA LA VENTANA TODOS LOS DATOS ESTADPISTICOS
def ventana_datos():
    try:
        a = p_proc.areas()
        b = p_proc.mediana()
        c = p_proc.desviacion_estandar()
        d = p_proc.minimo()
        e = p_proc.maximo()

        win1 = tk.Toplevel(root)
        win1.title("Areas")
        win1.geometry("200x200+610+100")
        SBar = tk.Scrollbar(win1)
        SBar.pack(side=tk.RIGHT, fill='y')
        TxBox = tk.Text(win1, yscrollcommand=SBar.set)
        TxBox.pack(expand=0, fill=tk.BOTH)
        for i in range(a.shape[0]):
            TxBox.insert(tk.END, "{}\t{}\n".format(str(i+1), str(a[i])))
        SBar.config(command=TxBox.yview)

        win2 = tk.Toplevel(root)
        win2.title("Datos")
        win2.geometry("250x150+820+100")
        etr1 = tk.Label(win2, text='Media: '+str(b))
        etr1.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        etr2 = tk.Label(win2, text='Desviación Estandar: ' + str(c))
        etr2.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        etr3 = tk.Label(win2, text='Mínimo: ' + str(d))
        etr3.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        etr4 = tk.Label(win2, text='Máximo: ' + str(e))
        etr4.grid(row=3, column=0, sticky='w', padx=5, pady=5)
    except(AttributeError, ZeroDivisionError, ValueError):
        mensaje_error_dato()


# **************************************************************************
# FUNCIÓN QUE MUESTRA LAS ÁREAS ORDENADAS EN VENTANA
def ventana_ordenamiento():
    try:
        f = p_proc.areas_ordenadas()
        win = tk.Toplevel(root)
        win.title("Ordenamiento")
        win.geometry("200x200+610+400")
        SBar = tk.Scrollbar(win)
        SBar.pack(side=tk.RIGHT, fill='y')
        TxBox = tk.Text(win, yscrollcommand=SBar.set)
        TxBox.pack(expand=0, fill=tk.BOTH)
        for i in range(f.shape[0]):
            TxBox.insert(tk.END, "{}\t{}\n".format(str(i+1), str(f[i])))
        SBar.config(command=TxBox.yview)
    except(AttributeError, ZeroDivisionError, ValueError):
        mensaje_error_dato()


# **************************************************************************
# FUNCIÓN QUE MUESTRA LA ENTRADA DE TAMAÑO DE LA MUESTRA
def ventana_conteo():
    win = tk.Toplevel(root)
    win.title("Conteo")
    win.geometry('+820+300')
    win.iconbitmap("Icons/pro_Ima.ico")
    label = tk.Label(win, text="Tamaño de muestra")
    label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.config(justify='center', textvariable=n4)
    button = tk.Button(win, text='OK', command=valida_conteo)
    button.grid(row=0, column=2, padx=5, pady=5)
    return win


# **************************************************************************
# FUNCIÓN DE LA IMAGEN BINARIA
def ventana_binario():
    try:
        p_proc.imgBinary()
    except (AttributeError):
        mensaje_error_dato()


# **************************************************************************
# FUNCIÓN QUE CREA EL EXCEL
def creacion_excel():
    try:
        p_proc.crear_excel()
    except(AttributeError):
        mb.showerror('Error', "No hay datos que guardar")

# ----------------------------------------------------------
# VENTANA PRINCIPAL DEL PROGRAMA, DONDE SE REALIZA TODA LAS OPERACIONES
root = tk.Tk()  # CREACIÓN DE LA VENTANA RAIZ
root.geometry("500x20+100+100")  # TAMAÑO DE VENTANA
root.title("Proyecto de Integrción en Ingeniería en Computación")  # TITULO DE LA VENTANA
root.iconbitmap("Icons/pro_Ima.ico")  # ICONO

# *************
# DECLARACIÓN DE VARIABLES PARA LOS DATOS DE ENTRADA
n1 = tk.StringVar()
n2 = tk.StringVar()
n3 = tk.StringVar()
n4 = tk.StringVar()
var = tk.StringVar()

# ----------------------------------------------------------
# CREACIÓN DEL MENÚ
menu_barra = tk.Menu(root)  # BARRA DE MENÚ EN LA VENTANA RAIZ
root.config(menu=menu_barra)  # ASIGNA NOMBRE AL MENU

# ----------------------------------------------------------
archivo_menu = tk.Menu(menu_barra, tearoff=0)  # MENÚ ARCHIVO
# BOTONES DENTRO DEL MENÚ ARCHIVO
archivo_menu.add_command(label="Nuevo", command=buscar_archivo)
archivo_menu.add_command(label="Guardar", command=creacion_excel)
archivo_menu.add_command(label="Cerrar", command=proceso.func_cerrar)
archivo_menu.add_command(label="Salir", command=root.destroy)

# ----------------------------------------------------------
menu_procesamiento = tk.Menu(menu_barra, tearoff=0) # MENÚ PROCESAMIENTO
# BOTONES DENTRO DEL MENÚ DE PROCESAMIENTO
menu_procesamiento.add_command(label='Escala', command=ventana_escala)
menu_procesamiento.add_command(label='Contraste', command=ventana_contraste)
menu_procesamiento.add_command(label='Desenfoque', command=ventana_desenfoque)
menu_procesamiento.add_command(label='Binario', command=ventana_binario)
menu_procesamiento.add_command(label='Deteccion', command=p_proc.deteccion)

# ----------------------------------------------------------
menu_estadistica = tk.Menu(menu_barra, tearoff=0) #MENÚ ESTADÍSTICA
submenu1 = tk.Menu(menu_estadistica) # SUBMENÚ
# BOTONES DENTRO DEL SUBMENÚ
menu_estadistica.add_command(label='Datos', command=ventana_datos)
menu_estadistica.add_command(label='Ordenamiento', command=ventana_ordenamiento)
menu_estadistica.add_command(label='Conteo', command=ventana_conteo)
submenu2 = tk.Menu(menu_estadistica) #SUBMENÚ
# BOTONES DENTRO DEL SUBMENÚ
submenu2.add_command(label='Conteo', command=p_proc.grafica_conteo)
submenu2.add_command(label='Normal', command=p_proc.grafica_normal)
menu_estadistica.add_cascade(label='Gráficas', menu=submenu2)

# ----------------------------------------------------------
# DECLARACIÓN DE LOS NOMBRES DE LOS BOTONES DEL MENÚ
menu_barra.add_cascade(label='Archivo', menu=archivo_menu)
menu_barra.add_cascade(label='procesamiento', menu=menu_procesamiento)
menu_barra.add_cascade(label='Análisis', menu=menu_estadistica)
menu_barra.add_cascade(label="Acerca de...", command=mensaje_sobre)
menu_barra.add_cascade(label='Agradecimientos', command=mensaje_gracias)

# ----------------------------------------------------------
root.mainloop()  # MANTIENE LA VENTANA ACTIVA
