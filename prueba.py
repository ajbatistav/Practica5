import sqlite3

con = sqlite3.connect("mydb.db")
cursor = con.cursor()
query0 = """
CREATE TABLE  contactos(contactoid integer primary key autoincrement, nombrecontacto text, numerocontacto integer, correocontacto text); """

query2 = """ SELECT * FROM contactos; """
def insertar (nombrecontacto,numerocontacto,correocontacto):
   query1 = """ INSERT INTO contactos(nombrecontacto, numerocontacto, correocontacto) VALUES (?,?,?); """
   info_tupla = (nombrecontacto,numerocontacto,correocontacto)
   cursor.execute(query1, info_tupla)
   con.commit()
   print("Datos Guardados")
   

print("Bienbenido a su agenda")
def menu():
    print("Que desea hacer: ")
    print("1.Agregar nuevo contacto.")
    print("2.Ver todos los contactos.")
    print("3.Buscar contacto por nombre o numero de telefono.")
    print("4.Actualizar un contacto.")
    print("5.Eliminar un contacto.")
    print("6.Salir.")

#cursor.execute(query0)
menu()
select = int(input("> "))
while select != 6:
    if select == 1: #agregar contacto
        print("Porfavor complete los siguientes campos")
        nombrecontacto = str(input("Nombre: "))
        numerocontacto = int(input("Numero: "))
        correocontacto = str(input("Correo Electronico: "))
        insertar(nombrecontacto,numerocontacto,correocontacto)             
        

        menu()
        select = int(input("> "))

    if select == 2: #Ver todos los contactos
        print("Lista de contactos: ")
        cursor.execute(query2)
        result = cursor.fetchall()
        print(result)
        
        menu()
        select = int(input("> "))
    
    if select == 3: #buscar contacto




