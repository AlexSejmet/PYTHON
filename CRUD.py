from tkinter import *
from tkinter import messagebox
import sqlite3



#--------Raiz----------------

raiz=Tk()

#raiz.geometry('500x500')
raiz.resizable(0,0)
raiz.title('Registro Empleados')

ancho=500
largo=500

pantallaAncho=raiz.winfo_screenwidth()
pantallaLargo=raiz.winfo_screenheight()

x = (pantallaAncho - ancho) // 2
y = (pantallaLargo - largo) // 2

raiz.geometry(f"{ancho}x{largo}+{x}+{y}")



#--------Funciones-----------

def conexionBBDD():
	miConexion=sqlite3.connect('Base_Usuarios')
	miCursor=miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			CEDULA VARCHAR (8),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo('BBDD','BBDD creada con éxito')
	except:
		messagebox.showwarning('¡Atención!','La BBDD ya fue creada')




def salirAplicacion():
	valor=messagebox.askquestion('Salir','¿Desea salir de la aplicación?')
	if valor=='yes':
		raiz.destroy()



def limpiarCampos():
	miNombre.set('')
	miId.set('')
	miApellido.set('')
	miCedula.set('')
	miDireccion.set('')
	miPass.set('')
	textoComentario.delete(1.0, END)



def crear():
	miConexion=sqlite3.connect('Base_Usuarios')
	miCursor=miConexion.cursor()

	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
	 "','" + miPass.get() +
	 "','" + miApellido.get() + 
	 "','" + miDireccion.get() + 
	 "','" + textoComentario.get("1.0", END) + "')")"""
	
	try:
		datos=miNombre.get(),miPass.get(),miApellido.get(),miCedula.get(),miDireccion.get(),textoComentario.get('1.0', END) 

		miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?,?)",(datos))

		miConexion.commit()

		messagebox.showinfo('BBDD', 'Registro insertado con éxito')
		limpiarCampos()
	except:
		messagebox.showwarning('¡Atención!','LA BASE DE DATOS NO HA SIDO CREADA')



def leer():
	miConexion=sqlite3.connect('Base_Usuarios')
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	elUsuario=miCursor.fetchall()

	for i in elUsuario:
		miId.set(i[0])
		miNombre.set(i[1])
		miPass.set(i[2])
		miApellido.set(i[3])
		miCedula.set(i[4])
		miDireccion.set(i[5])
		textoComentario.delete(1.0, END)
		textoComentario.insert(1.0, i[6])

		miConexion.commit()

	raiz.withdraw()
	raiz2=Tk()
	#raiz2.geometry('500x500')
	raiz2.resizable(0,0)
	raiz2.title('Resultado busqueda')

	ancho=500
	largo=500
	pantallaAncho=raiz.winfo_screenwidth()
	pantallaLargo=raiz.winfo_screenheight()
	x = (pantallaAncho - ancho) // 2
	y = (pantallaLargo - largo) // 2

	raiz2.geometry(f"{ancho}x{largo}+{x}+{y}")

	miFrame3=Frame(raiz2, bg=pintura)
	miFrame3.pack(expand=True, fill='both')

	def regreso():
		raiz2.withdraw()
		raiz.deiconify()

	titulolabel=Label(miFrame3, text='DATOS',bg=pintura, fg='white', font=(10)).place(x=220, y=10)

	nombrelabel=Label(miFrame3, text='Nombre:',bg=pintura, fg='white', font=(5)).place(x=20, y=70)
	resNombre=Label(miFrame3, text=miNombre.get(), bg=pintura, fg='white', font=(5)).place(x=100, y=70)  

	apellidolabel=Label(miFrame3, text='Apellido:',bg=pintura, fg='white', font=(5)).place(x=20, y=120)
	resApellido=Label(miFrame3, text=miApellido.get(), bg=pintura, fg='white', font=(5)).place(x=100, y=120)   

	cedulalabel=Label(miFrame3, text='Cédula:',bg=pintura, fg='white', font=(5)).place(x=20, y=170) 
	resCedula=Label(miFrame3, text=miCedula.get(), bg=pintura, fg='white', font=(5)).place(x=100, y=170)  

	direccionlabel=Label(miFrame3, text='Dirección:',bg=pintura, fg='white', font=(5)).place(x=20, y=220)
	resDireccion=Label(miFrame3, text=miDireccion.get(), bg=pintura, fg='white', font=(5)).place(x=100, y=220)   

	comentarioslabel=Label(miFrame3, text='Comentarios:',bg=pintura, fg='white', font=(5)).place(x=20, y=270)
	resComent=Label(miFrame3, text=textoComentario.get(1.0, END), bg=pintura, fg='white', font=(5)).place(x=120, y=270)   	

	botonRegreso=Button(raiz2, text='Regresar', cursor='hand2', width=10, height=2, borderwidth = 0, command=regreso)
	botonRegreso.place(x=20, y=445)

	raiz2.mainloop



def actualizar():
	miConexion=sqlite3.connect('Base_Usuarios')
	miCursor=miConexion.cursor()

	"""miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+ miNombre.get() +
		"', PASSWORD='" + miPass.get() +
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())"""

	datos=miNombre.get(),miPass.get(),miApellido.get(),miCedula.get(),miDireccion.get(),textoComentario.get('1.0', END) 
	
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, CEDULA=?, DIRECCION=?, COMENTARIOS=?" +
		"WHERE ID=" + miId.get(),(datos))	

	miConexion.commit()

	messagebox.showinfo('BBDD', 'Registro Actualizado con éxito')
	limpiarCampos()



def eliminar():
	miConexion=sqlite3.connect('Base_Usuarios')
	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	miConexion.commit()

	messagebox.showinfo('BBDD', 'Registro eliminado con éxito')
	limpiarCampos()



 #------Barra Menú----------------

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=400,height=400)


bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='Conectar', command=conexionBBDD)
bbddMenu.add_command(label='Salir', command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label='Borrar campos', command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Crear', command=crear)
crudMenu.add_command(label='Leer',command=leer)
crudMenu.add_command(label='Actualizar', command=actualizar)
crudMenu.add_command(label='Borrar', command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label='Licencia')
ayudaMenu.add_command(label='Acerca de...')

barraMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)



 #-------Entrys----------------------------

pintura='#2f1335'

miFrame=Frame(raiz, bg=pintura)
miFrame.pack(expand=True, fill='both')

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miCedula=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId, width=5, relief='flat')
cuadroID.grid(row=0, column=1, padx=10, pady=10, ipady=3)

cuadroNombre=Entry(miFrame, textvariable=miNombre, width=30, relief='flat')
cuadroNombre.grid(row=1, column=1, padx=10, pady=10, ipady=3)

cuadroApellido=Entry(miFrame, textvariable=miApellido, width=30, relief='flat')
cuadroApellido.grid(row=2, column=1, padx=10, pady=10, ipady=3)

cuadroCedula=Entry(miFrame, textvariable=miCedula, width=30, relief='flat')
cuadroCedula.grid(row=3, column=1, padx=10, pady=10, ipady=3)

cuadroPass=Entry(miFrame, textvariable=miPass, width=30, relief='flat')
cuadroPass.grid(row=4, column=1, padx=10, pady=10, ipady=3)
cuadroPass.config(show='*')

cuadroDireccion=Entry(miFrame, textvariable=miDireccion, width=30, relief='flat')
cuadroDireccion.grid(row=5, column=1, padx=10, pady=10, ipady=3)

textoComentario=Text(miFrame, width=30, height=8, relief='flat')
textoComentario.grid(row=6, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=6, column=2, sticky='nsew')
textoComentario.config(yscrollcommand=scrollVert.set)



 #--------------Etiquetas------------

idlabel=Label(miFrame, text='Buscar por ID:', bg=pintura)
idlabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)  
idlabel.config(fg="white", bg=pintura) 


nombrelabel=Label(miFrame, text='Nombre:',bg=pintura)
nombrelabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)
nombrelabel.config(fg="white", bg=pintura) 


apellidolabel=Label(miFrame, text='Apellido:',bg=pintura)
apellidolabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)
apellidolabel.config(fg="white", bg=pintura)


cedulalabel=Label(miFrame, text='Cédula:',bg=pintura)
cedulalabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)
cedulalabel.config(fg="white", bg=pintura) 


passlabel=Label(miFrame, text='Contraseña:',bg=pintura)
passlabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)
passlabel.config(fg="white", bg=pintura) 


direccionlabel=Label(miFrame, text='Dirección:',bg=pintura)
direccionlabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)
direccionlabel.config(fg="white", bg=pintura) 


comentarioslabel=Label(miFrame, text='Comentarios:',bg=pintura)
comentarioslabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)
comentarioslabel.config(fg="white", bg=pintura) 



 #-------Botones--------

miFrame2=Frame(raiz, bg='#8b8b70')
miFrame2.pack(expand=True, fill='both')

botonCrear=Button(miFrame2, text='Crear', cursor='hand2', width=10, height=2, borderwidth = 0, command=crear)
botonCrear.grid(row=1, column=0, sticky='e', padx=10, pady=10)

botonLeer=Button(miFrame2, text='Leer', cursor='hand2', width=10, height=2, borderwidth = 0, command=leer)
botonLeer.grid(row=1, column=1, sticky='e', padx=10, pady=10)

botonActualizar=Button(miFrame2, text='Actualizar', cursor='hand2', width=10, height=2, borderwidth = 0, command=actualizar)
botonActualizar.grid(row=1, column=2, sticky='e', padx=10, pady=10)

botonBorrar=Button(miFrame2, text='Eliminar', cursor='hand2', width=10, height=2, borderwidth = 0, command=eliminar)
botonBorrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)

botonSalir=Button(miFrame2, text='Salir', cursor='hand2', width=10, height=2, borderwidth = 0, foreground='white', bg='red', command=salirAplicacion)
botonSalir.grid(row=1, column=4, sticky='e', padx=10, pady=10)


raiz.mainloop()
