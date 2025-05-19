#Bibliotecas
import pymysql      #Escribir en la terminal " pip install PyMySQL" para instalar la biblioteca que conectara Python y SQL



#Conexion Python y SQL
conexion = pymysql.connect(user="root", password="",        #En "user" corresponde al nombre del usuario de la base de datos, lo mismo aplica para "password" que es la contraseña.
                                   host="127.0.0.1",        #En "host" corresponde a nuestro servidor local (La IP).
                                   database="prueba",       #En "database" corresponde a el nombre (la conexion sql) de la base de datos a utilizar.
                                   port=3306)               #En "port" corresponde a nuestro puerto del servidor.
print(conexion)                                             #Imprime una serie de caracteres que indica que se ha conectado correctamente, de lo contrario mostrara error.Ahi 



#Para crear Tablas
cursor = conexion.cursor()                                  #Creamos un cursor par alamacenar la informacion en memoria, ya sea para leerla o modificarla
cursor.execute("CREATE TABLE IF NOT EXISTS Ciudad(Ciudad VARCHAR(255) NOT NULL, Pais VARCHAR(100) NOT NULL, PRIMARY KEY (Ciudad))")



#Pedir datos por teclado
Datos = []                                                  #Lista para almacenar los datos ingresados por el usuario
ciudad= input("Ingresa una ciudad: ")
pais= input("Ingresa un pais: ")
Datos.append((ciudad,pais))                                 



#Insertar los datos en la tabla
cursor.executemany("INSERT INTO Ciudad (Ciudad, Pais) VALUES(%s,%s)", Datos)
#Actualizar datos
#cursor.executemany("UPDATE Ciudad SET Ciudad=%s, Pais=%s WHERE Pais = 'Mexico'", Datos)
#Borrar datos
#cursor.execute("DELETE FROM Ciudad WHERE Pais = %s", (Datos[0][1],))



#Guardamos los cambios hechos a la Base de Datos
conexion.commit()



#Para buscar consultas
cursor = conexion.cursor()                                #Declarar la consulta
cursor.execute("select Ciudad, Pais from Ciudad")         #Seleccionar los datos a consultar.
for ciudad, pais in cursor.fetchall():                   #Ciclo for utilizado para mostrar todos los datos.
    print(ciudad, " | " ,pais)



#Cierre del cursor
cursor.close()



#Cierre de la conexion
conexion.close()                                           