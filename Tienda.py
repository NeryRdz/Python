import pymysql
from prettytable import PrettyTable
from datetime import datetime
import csv

#Conexion de Python a MySQL
conexion = pymysql.connect(user="root", 
                          password="",
                          host="127.0.0.1",
                          port=3306)
print("Conexion a MySQL establecida.")


#Crear la base de datos su no existe
cursor = conexion.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Tienda")
cursor.close()

#Conexion a la base de datos
conexion = pymysql.connect(user="root", 
                          password="",
                          host="127.0.0.1",
                          database="Tienda",
                          port=3306)
print("Conexion a la base de datos establecida.")                       


#Para crear Tablas
cursor = conexion.cursor()                                  

# Tabla Categoria
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categoria(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT NULL
) ENGINE=InnoDB""")

# Tabla Proveedor
cursor.execute("""
CREATE TABLE IF NOT EXISTS Proveedor(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(75) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    direccion VARCHAR(150) NOT NULL
) ENGINE=InnoDB""")

# Tabla Cliente
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(75) NOT NULL,
    email VARCHAR(120) NOT NULL,
    telefono VARCHAR(30) NOT NULL
) ENGINE=InnoDB""")

# Tabla Producto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Producto(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(75) NOT NULL,
    descripcion TEXT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock_actual INT NOT NULL DEFAULT 0,
    categoria_id INT NOT NULL,
    proveedor_id INT NOT NULL,
    FOREIGN KEY(categoria_id) REFERENCES Categoria(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
    FOREIGN KEY(proveedor_id) REFERENCES Proveedor(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB""")

# Tabla Ventas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Ventas(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cliente_id INT NOT NULL,
    total DECIMAL(12,2) NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES Cliente(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB""")

# Tabla Detalle_Ventas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Detalle_Ventas(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    venta_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY(venta_id) REFERENCES Ventas(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(producto_id) REFERENCES Producto(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB""")

# Tabla Movimiento_Inventario
cursor.execute("""
CREATE TABLE IF NOT EXISTS Movimiento_Inventario(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    producto_id INT NOT NULL,
    tipo ENUM('entrada', 'salida', 'ajuste') NOT NULL,
    cantidad INT NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    motivo VARCHAR(80) NOT NULL DEFAULT 'Movimiento de inventario',
    FOREIGN KEY(producto_id) REFERENCES Producto(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB""")

cursor.execute("SELECT COUNT(*) FROM Categoria")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO Categoria (nombre, descripcion) VALUES
    ('Electrónica', 'Dispositivos electrónicos y gadgets'),
    ('Ropa', 'Prendas de vestir para todas las edades'),
    ('Alimentos', 'Productos alimenticios y comestibles'),
    ('Hogar', 'Artículos para el hogar y decoración'),
    ('Deportes', 'Equipamiento deportivo y accesorios'),
    ('Juguetes', 'Juguetes para niños y coleccionables'),
    ('Libros', 'Libros de todos los géneros literarios'),
    ('Belleza', 'Productos de cuidado personal y cosméticos'),
    ('Jardinería', 'Herramientas y plantas para jardín'),
    ('Muebles', 'Mobiliario para hogar y oficina'),
    ('Tecnología', 'Equipos tecnológicos y computación'),
    ('Automotriz', 'Repuestos y accesorios para vehículos'),
    ('Salud', 'Productos médicos y de bienestar'),
    ('Oficina', 'Suministros y artículos de oficina'),
    ('Mascotas', 'Alimentos y accesorios para mascotas'),
    ('Instrumentos Musicales', 'Instrumentos y equipos de audio'),
    ('Ferretería', 'Herramientas y materiales de construcción'),
    ('Joyeria', 'Joyas y accesorios de moda'),
    ('Viajes', 'Equipaje y artículos para viajar'),
    ('Bebés', 'Productos para bebés y niños pequeños');
    """)
    conexion.commit()


cursor.execute("SELECT COUNT(*) FROM Proveedor")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO Proveedor (nombre, telefono, direccion) VALUES
    ('TecnoSuministros S.A.', '555-1234567', 'Av. Tecnológica 123, Ciudad Digital'),
    ('ModaTotal Import', '555-2345678', 'Calle de la Moda 45, Distrito Textil'),
    ('Distribuciones Alimenticias', '555-3456789', 'Zona Industrial 78, Bodega 12'),
    ('Hogar y Estilo', '555-4567890', 'Centro Comercial Plaza, Local 34'),
    ('Deportes Extremos', '555-5678901', 'Av. Deportiva 56, Polideportivo'),
    ('Juguetería Fantasía', '555-6789012', 'Calle Infantil 89, Plaza de los Niños'),
    ('Librería El Saber', '555-7890123', 'Av. Cultural 101, Zona Universitaria'),
    ('Belleza Natural', '555-8901234', 'Centro Comercial Galerías, Local 56'),
    ('Jardines y Más', '555-9012345', 'Carretera Verde Km 12.5'),
    ('Muebles Elegantes', '555-0123456', 'Av. del Mueble 200, Polígono Industrial'),
    ('TecnoGlobal', '555-1122334', 'Parque Tecnológico, Edificio 3'),
    ('AutoPartes Rápidas', '555-2233445', 'Av. Automotriz 300, Zona Industrial'),
    ('Farmacia Salud Total', '555-3344556', 'Calle Salud 45, Centro Médico'),
    ('Suministros de Oficina', '555-4455667', 'Av. Comercial 67, Distrito Financiero'),
    ('Mundo Mascota', '555-5566778', 'Calle Animales 123, Plaza de las Mascotas'),
    ('Música y Sonido', '555-6677889', 'Av. Musical 88, Distrito Cultural'),
    ('Ferretería Industrial', '555-7788990', 'Zona Industrial Pesada, Nave 5'),
    ('Joyas Preciosas', '555-8899001', 'Centro Comercial Diamante, Local 1'),
    ('Equipaje Viajero', '555-9900112', 'Terminal Aérea, Local 23'),
    ('Bebélandia', '555-0011223', 'Av. Familiar 145, Plaza Infantil');
    """)
    conexion.commit()

cursor.execute("SELECT COUNT(*) FROM Cliente")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO Cliente (nombre, email, telefono) VALUES
    ('Juan Pérez', 'juan.perez@email.com', '555-1111111'),
    ('María González', 'maria.gonzalez@email.com', '555-2222222'),
    ('Carlos López', 'carlos.lopez@email.com', '555-3333333'),
    ('Ana Martínez', 'ana.martinez@email.com', '555-4444444'),
    ('Luis Rodríguez', 'luis.rodriguez@email.com', '555-5555555'),
    ('Sofía Hernández', 'sofia.hernandez@email.com', '555-6666666'),
    ('Jorge Díaz', 'jorge.diaz@email.com', '555-7777777'),
    ('Laura García', 'laura.garcia@email.com', '555-8888888'),
    ('Pedro Sánchez', 'pedro.sanchez@email.com', '555-9999999'),
    ('Mónica Ramírez', 'monica.ramirez@email.com', '555-0000000'),
    ('Roberto Castro', 'roberto.castro@email.com', '555-1212121'),
    ('Elena Torres', 'elena.torres@email.com', '555-2323232'),
    ('Fernando Ruiz', 'fernando.ruiz@email.com', '555-3434343'),
    ('Patricia Vargas', 'patricia.vargas@email.com', '555-4545454'),
    ('Ricardo Mendoza', 'ricardo.mendoza@email.com', '555-5656565'),
    ('Gabriela Silva', 'gabriela.silva@email.com', '555-6767676'),
    ('Daniel Ortega', 'daniel.ortega@email.com', '555-7878787'),
    ('Adriana Morales', 'adriana.morales@email.com', '555-8989898'),
    ('José Guzmán', 'jose.guzman@email.com', '555-9090909'),
    ('Verónica Ríos', 'veronica.rios@email.com', '555-0101010');
    """)
    conexion.commit()

cursor.execute("SELECT COUNT(*) FROM Producto")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO Producto (nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id) VALUES
    ('Smartphone X', 'Teléfono inteligente última generación', 899.99, 50, 1, 1),
    ('Laptop Pro', 'Portátil de alto rendimiento', 1299.99, 30, 11, 11),
    ('Camiseta básica', 'Camiseta de algodón unisex', 19.99, 200, 2, 2),
    ('Arroz 1kg', 'Arroz blanco de grano largo', 2.50, 500, 3, 3),
    ('Balón de fútbol', 'Balón oficial tamaño 5', 29.99, 75, 5, 5),
    ('Muñeca articulada', 'Muñeca coleccionable 30cm', 24.99, 120, 6, 6),
    ('Libro de Python', 'Aprende Python desde cero', 39.99, 80, 7, 7),
    ('Crema hidratante', 'Crema facial para todo tipo de piel', 14.99, 150, 8, 8),
    ('Mesa de centro', 'Mesa moderna de madera', 149.99, 25, 10, 10),
    ('Teclado mecánico', 'Teclado gaming con retroiluminación', 79.99, 60, 11, 1);
    """)
    conexion.commit()  


class Tienda():
    def main(self):
        while True:
            print(
"""
=== SISTEMA DE GESTIÓN DE INVENTARIO ===
1. Productos
2. Ventas
3. Reportes
4. Inventario
5. Salir
""")

            opcion = int(input("Eliga una opcion (1-5): "))
            if opcion == 1:
                tda.Productos()
            elif opcion == 2:
                tda.Ventas()
            elif opcion == 3:
                tda.Reportes()
            elif opcion == 4:
                tda.Inventario()
            elif opcion == 5:    
                break
            else:
                print("Selecciona una opcion valida")

    def Productos(self):
        print("=== Productos ===")

        cursor.execute("""
        SELECT p.id,p.nombre,p.descripcion,p.precio,p.stock_actual,c.nombre AS Categoria,p2.nombre AS Proveedor FROM producto p
        INNER JOIN categoria c ON p.categoria_id = c.id
        INNER JOIN proveedor p2 ON p.proveedor_id = p2.id;""")
        tabla = PrettyTable()
        tabla.field_names = [desc[0] for desc in cursor.description]

        for fila in cursor.fetchall():
            tabla.add_row(fila)

        print(tabla)
        
        op = int(input("1. Agregar producto\n2. Editar Producto\n3. Buscar \n4. Salir\nTu opcion: "))

        if op == 1:
            print("=== Agregar Productos ===")
            nombre = input("Ingresa el nombre del producto: ")
            descr = input("Ingresa descripcion (opcional): ")
            precio = float(input("Ingresa un precio al producto: "))
            stock = int(input("Ingresa el stock de este producto: "))

            cursor.execute("SELECT id, nombre FROM Categoria GROUP BY nombre ORDER BY id ASC")
            categorias = cursor.fetchall()
            print("\nCategorías disponibles:")
            for cat in categorias:
                print(f"{cat[0]}. {cat[1]}")

            cat = int(input("\nSelecciona una categoría: "))

            cursor.execute("SELECT id FROM Categoria WHERE id = %s", (cat,))
            if not cursor.fetchone():
                print("Selecciona una categoria existente")
                return

            cursor.execute("SELECT id, nombre FROM Proveedor GROUP BY nombre ORDER BY id ASC")
            proveedores = cursor.fetchall()
            print("\nProveedores disponibles:")
            for prov in proveedores:
                print(f"{prov[0]}. {prov[1]}")
            proveedor_id = int(input("\nSelecciona un proveedor: "))
            
            cursor.execute("SELECT id FROM Proveedor WHERE id = %s", (proveedor_id,))
            if not cursor.fetchone():
                print("Selecciona un proveedor existente")
                return

            cursor.execute("""
            INSERT INTO Producto (nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id)
            VALUES (%s, %s, %s, %s, %s, %s)""",(nombre, descr, precio, stock, cat, proveedor_id))
            conexion.commit()

        elif op == 2:
            print("=== Editar Productos ===")
            cursor.execute("SELECT id, nombre FROM producto GROUP BY nombre ORDER BY id ASC")
            productos = cursor.fetchall()
            print("\nProductos disponibles:")
            for producto in productos:
                print(f"{producto[0]}. {producto[1]}") 

            productoid = int(input("Que producto deseas editar?: "))

            cursor.execute("SELECT id FROM Producto WHERE id = %s", (productoid,))
            if not cursor.fetchone():
                print("Selecciona un producto existente")
                return
            
            cursor.execute("""
            SELECT p.id,p.nombre,p.descripcion,p.precio,p.stock_actual,
            c.id,p2.id,c.nombre AS Categoria,p2.nombre AS Proveedor 
            FROM producto p
            INNER JOIN categoria c ON p.categoria_id = c.id
            INNER JOIN proveedor p2 ON p.proveedor_id = p2.id
            WHERE p.id = %s""",(productoid,))
            producto = cursor.fetchone()

            nuevo = {
                "nombre": producto[1],
                "descripcion": producto[2],
                "precio": producto[3],
                "stock": producto[4],
                "categoriaid": producto[5],
                "proveedorid": producto[6]
            }
            while True:
                print("\nDatos actuales del producto:")
                print(f"1. Nombre: {producto[1]}")
                print(f"2. Descripción: {producto[2]}")
                print(f"3. Precio: {producto[3]}")
                print(f"4. Stock: {producto[4]}")
                print(f"5. Categoria : {producto[7]}")
                print(f"6. Proveedor: {producto[8]}")

                campo = int(input("""
                ¿Qué campo desea editar?
                1. Nombre
                2. Descripción
                3. Precio
                4. Stock
                5. Categoría
                6. Proveedor
                7. Guardar cambios y salir
                8. Salir sin guardar
                Tu opcion: 
                """))
                if campo == 1:
                    nuevo["nombre"] = input("Ingrese el nuevo nombre del producto: ")

                elif campo == 2:
                    nuevo["descripcion"] = input("Ingrese la nueva descripcion del producto: ")

                elif campo == 3:
                    nuevo["precio"] = float(input("Ingrese el nuevo precio del producto: "))

                elif campo == 4:
                    nuevo["stock"] = input("Ingrese el nuevo stock del producto: ")

                elif campo == 5:
                    cursor.execute("SELECT id, nombre FROM Categoria GROUP BY nombre ORDER BY id ASC")
                    categorias = cursor.fetchall()
                    print("\nCategorías disponibles:")
                    for cat in categorias:
                        print(f"{cat[0]}. {cat[1]}")
                    nuevo["categoriaid"] = int(input("Ingrese la nueva categoria del producto: "))
                    
                    cursor.execute("SELECT id FROM Categoria WHERE id = %s", (nuevo["categoriaid"],))
                    if not cursor.fetchone():
                        print("Selecciona una categoria existente")
                        return

                elif campo == 6:
                    cursor.execute("SELECT id, nombre FROM Proveedor GROUP BY nombre ORDER BY id ASC")
                    proveedores = cursor.fetchall()
                    print("\Proveedores disponibles:")
                    for proveedor in proveedores:
                        print(f"{proveedor[0]}. {proveedor[1]}")
                    nuevo["proveedorid"] = int(input("Ingrese el proveedor del producto: "))

                    cursor.execute("SELECT id FROM Proveedor WHERE id = %s", (nuevo["proveedorid"],))
                    if not cursor.fetchone():
                        print("Selecciona un proveedor existente")
                        return
                    
                elif campo == 7:
                    cursor.execute("""
                    UPDATE Producto SET
                    nombre = %s,
                    descripcion = %s,
                    precio = %s,
                    stock_actual = %s,
                    categoria_id = %s,
                    proveedor_id = %s
                    WHERE id = %s
                    """,
                    (nuevo['nombre'],
                    nuevo['descripcion'],
                    nuevo['precio'],
                    nuevo['stock'],
                    nuevo['categoriaid'],
                    nuevo['proveedorid'],
                    productoid))

                    conexion.commit()
                    break
                elif campo == 8:
                    print("No se realizaron cambios")
                    break
                else:
                    print("Selecciona una opcion existente.")    

        elif op == 3:
            print("=== Buscar Productos ===")
            cursor.execute("SELECT id, nombre FROM producto GROUP BY nombre ORDER BY id ASC")
            productos = cursor.fetchall()
            print("\nProductos disponibles:")
            for producto in productos:
                print(f"{producto[0]}. {producto[1]}") 

            productoid = int(input("Que producto deseas ver sus especificaciones? : "))
            
            cursor.execute("SELECT id FROM Categoria WHERE id = %s",(productoid,))
            if not cursor.fetchone():
                print("El producto no existe")
                return

            cursor.execute("""
            SELECT p.id,p.nombre,p.descripcion,p.precio,p.stock_actual,c.nombre AS Categoria,p2.nombre AS Proveedor 
            FROM producto p
            INNER JOIN categoria c ON p.categoria_id = c.id
            INNER JOIN proveedor p2 ON p.proveedor_id = p2.id
            WHERE p.id = %s""",(productoid,))
            producto = cursor.fetchone()
            print("\nDatos actuales del producto:")
            print(f"1. Nombre: {producto[1]}")
            print(f"2. Descripción: {producto[2]}")
            print(f"3. Precio: {producto[3]}")
            print(f"4. Stock: {producto[4]}")
            print(f"5. Categoria : {producto[5]}")
            print(f"6. Proveedor: {producto[6]}")

        else:
            print("Selecciona una opcino valida")

    def Ventas(self):
        print("== Ventas ==")
        op2 = int(input("1. Cliente existente \n2. Cliente nuevo\nTu opcion: "))
        if op2 == 1:
            cursor.execute("SELECT id,nombre FROM Cliente")
            clientes = cursor.fetchall()
            print("\nClientes disponibles:")
            for cliente in clientes:
                print(f"{cliente[0]}. {cliente[1]}")
            cliente_id = int(input("Selecciona el cliente (ID): "))

            cursor.execute("SELECT id FROM Cliente WHERE id = %s", (cliente_id))
            if not cursor.fetchone():
                print("El cliente no existe")
                return

        elif op2 == 2:
            nombrecliente = input("Ingresa el nombre: ")
            emailcliente = input("Ingresa el email: ")
            telcliente = input("Ingresa el telefono: ")

            cursor.execute("INSERT INTO Cliente(nombre,email,telefono) VALUES (%s,%s,%s)",(nombrecliente,emailcliente,telcliente))
            conexion.commit()
            cliente_id = cursor.lastrowid
            print("Cliente agregado")
        else:
            print("Selecciona una opcion valida")
            
        carrito = []
        total = 0
        iva = 1.16

        while True:
            ventaop = int(input("1. Agregar producto\n2. Finalizar venta\n3. Cancelar\nTu opcion: "))
            if ventaop == 1:
                

                print("=== Disponibles ===")
                cursor.execute("""
                SELECT p.id,p.nombre,p.descripcion,p.precio,p.stock_actual,c.nombre AS Categoria,p2.nombre AS Proveedor FROM producto p
                INNER JOIN categoria c ON p.categoria_id = c.id
                INNER JOIN proveedor p2 ON p.proveedor_id = p2.id;""")
                tabla = PrettyTable()
                tabla.field_names = [desc[0] for desc in cursor.description]

                for fila in cursor.fetchall():
                    tabla.add_row(fila)

                print(tabla)

                producto_id = int(input("Agrega el producto al carrito:"))

                cursor.execute("SELECT id FROM Producto WHERE id = %s", (producto_id,))
                if not cursor.fetchone():
                    print("Selecciona un producto existente")
                    return
                
                cursor.execute("SELECT nombre,precio,stock_actual FROM Producto WHERE id = %s",(producto_id,))
                datosproducto = cursor.fetchone()
                cant = int(input("Cuanto deseas llevar?: "))
                
                if cant <= 0:
                    print("Ingrese una cantidad positiva")
                    return

                if int(datosproducto[2])-cant < 0:
                    print("La cantidad seleccionada excede del stock")
                    return

                total += cant*float(datosproducto[1])

                #               Nombre              Precio    Cantidad
                carrito.append((datosproducto[0],datosproducto[1],cant,producto_id))

                print("== Productos agregados ==")
                for i, producto in enumerate(carrito):
                    print(f"{i+1}. {producto[0]}       --       {producto[2]} x ${producto[1]} = {producto[1]*producto[2]}")
                    
                print("------------------------------------")
                print(f"Subtotal:{total:.2f}")
                print(f"Total (IVA incluido): ${total * iva:.2f}")

            elif ventaop == 2:
                if carrito:
                    cursor.execute("INSERT INTO Ventas(fecha,cliente_id,total) VALUES(%s,%s,%s)",
                                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),cliente_id,total*iva))
                    conexion.commit()
                    venta_id = cursor.lastrowid
                    
                    for dato in carrito:
                        cursor.execute("INSERT INTO Detalle_Ventas(venta_id,producto_id,cantidad,precio_unitario) VALUES(%s,%s,%s,%s)",
                                    (venta_id,dato[3],dato[2],dato[1]))
                        cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(dato[3]))
                        stockactual = cursor.fetchone()[0]
                        cursor.execute("UPDATE Producto SET stock_actual = %s WHERE id = %s",(int(stockactual)-dato[2],dato[3]))
                    conexion.commit()

                    print("Venta finalizada.")
                    break
                else:
                    print("No hay articulos en el carrito")
            elif ventaop == 3:
                print("Venta cancelada.")
                break
            else:
                print("Selecciona una opcion valida")

    def Reportes(self):
        print("== Reportes ==")

        print("\n--- Productos con bajo stock (Menor a 10 unidades) ---")
        cursor.execute("SELECT nombre,stock_actual FROM Producto WHERE stock_actual < 10")
        bajostock = cursor.fetchall()
        if bajostock:
            for producto in bajostock:
                print(f"- {producto[0]}: {producto[1]} unidades")
        else:
            print("No hay ningun producto con stock bajo.")

        print("\n--- Productos más vendidos (Mes Actual) ---")
        cursor.execute("""
        SELECT p1.nombre,p1.stock_actual,p1.precio,SUM(dv.cantidad) AS Ventas
        FROM Producto p1
        INNER JOIN Detalle_Ventas dv ON p1.id = dv.producto_id
        INNER JOIN Ventas v ON dv.venta_id = v.id                    
        WHERE MONTH(v.fecha) = MONTH(CURDATE()) AND YEAR(v.fecha) = YEAR(CURDATE())
        GROUP BY dv.producto_id 
        ORDER BY dv.producto_id DESC LIMIT 3;""")

        masvendido = cursor.fetchall()
        if masvendido:
            for producto in masvendido:
                print(f"- {producto[0]}: {producto[1]} unidades    --${producto[2]}c/u")
        else:
            print("No hay ningun producto mas vendido este mes.")

        print("\n--- Ventas por categoría ---")
        cursor.execute("""
        SELECT c.nombre, SUM(dv.precio_unitario*dv.cantidad) AS Total FROM Producto p
        INNER JOIN categoria c ON p.categoria_id = c.id
        INNER JOIN Detalle_Ventas dv ON p.id = dv.producto_id
        GROUP BY c.nombre ORDER BY Total DESC;""")

        ventascat = cursor.fetchall()
        if ventascat:
            for producto in ventascat:
                print(f"- {producto[0]}: ${producto[1]:.2f}")
        else:
            print("No hay ninguna categoria mas vendida.")

        opp = int(input("\n1. Generar reporte detallado\n2. Exportar a CSV\n3. Salir\nTu opcion: "))
        
        if opp == 1:
            print("\n=== Productos con bajo stock ===")
            cursor.execute("""
            SELECT p.nombre AS Producto,p.stock_actual AS Stock,c.nombre AS Categoria,
            p.precio AS Precio,p2.nombre AS Proveedor,p2.telefono AS Contacto
            FROM producto p
            INNER JOIN categoria c ON p.categoria_id = c.id
            INNER JOIN proveedor p2 ON p.proveedor_id = p2.id
            WHERE p.stock_actual < 10
            ORDER BY p.stock_actual ASC, p.nombre;
            """)
            tabla = PrettyTable()
            tabla.field_names = [desc[0] for desc in cursor.description]
            for fila in cursor.fetchall():
                tabla.add_row(fila)
            print(tabla)

            print("\n=== Top 10 Productos Mas Vendidos (Este mes) ===")
            cursor.execute("""
            SELECT p.nombre AS Producto,SUM(dv.cantidad) AS Unidades,FORMAT(SUM(dv.cantidad*dv.precio_unitario),2) AS Total,
            FORMAT(AVG(dv.precio_unitario),2) AS Precio_Promedio, p.stock_actual AS Stock_Actual
            FROM Producto p
            INNER JOIN Detalle_Ventas dv ON p.id = dv.producto_id
            INNER JOIN Ventas v ON dv.venta_id = v.id                    
            WHERE MONTH(v.fecha) = MONTH(CURDATE()) AND YEAR(v.fecha) = YEAR(CURDATE())
            GROUP BY p.id ORDER BY Unidades DESC LIMIT 10;
            """)
            tabla = PrettyTable()
            tabla.field_names = [desc[0] for desc in cursor.description]
            for fila in cursor.fetchall():
                tabla.add_row(fila)
            print(tabla)

            print("\n=== Ventas por Categoria ===")
            cursor.execute("""
            SELECT c.nombre AS Categoria,COUNT(DISTINCT v.id) AS Transacciones,SUM(dv.cantidad) AS Unidades,
            FORMAT(SUM(dv.cantidad*dv.precio_unitario),2) AS Ventas_Totales, FORMAT(COUNT(DISTINCT v.cliente_id) / COUNT(DISTINCT v.id) * 100,1) AS Fidelizacion
            FROM Categoria c
            INNER JOIN Producto p ON c.id = p.categoria_id
            INNER JOIN Detalle_Ventas dv ON p.id = dv.producto_id
            INNER JOIN Ventas v ON dv.venta_id = v.id
            GROUP BY c.id ORDER BY Ventas_Totales DESC;
            """)
            tabla = PrettyTable()
            tabla.field_names = [desc[0] for desc in cursor.description]
            for fila in cursor.fetchall():
                tabla.add_row(fila)
            print(tabla)

        elif opp == 2:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"downloads/reporte_{timestamp}.csv"

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                
                writer.writerow(["Reporte Generado", datetime.now().strftime("%d/%m/%Y %H:%M")])
                writer.writerow([])

                cursor.execute("""
                SELECT p.nombre AS Producto,p.stock_actual AS Stock,c.nombre AS Categoria,
                p.precio AS Precio,p2.nombre AS Proveedor,p2.telefono AS Contacto
                FROM producto p
                INNER JOIN categoria c ON p.categoria_id = c.id
                INNER JOIN proveedor p2 ON p.proveedor_id = p2.id
                WHERE p.stock_actual < 10
                ORDER BY p.stock_actual ASC, p.nombre;
                """)
                writer.writerow(["Productos con bajo stock (menor a 10 unidades)"])
                writer.writerow([desc[0] for desc in cursor.description])
                writer.writerows(cursor.fetchall())
                writer.writerow([])

                cursor.execute("""
                SELECT p.nombre AS Producto,SUM(dv.cantidad) AS Unidades,FORMAT(SUM(dv.cantidad*dv.precio_unitario),2) AS Total,
                FORMAT(AVG(dv.precio_unitario),2) AS Precio_Promedio, p.stock_actual AS Stock_Actual
                FROM Producto p
                INNER JOIN Detalle_Ventas dv ON p.id = dv.producto_id
                INNER JOIN Ventas v ON dv.venta_id = v.id                    
                WHERE MONTH(v.fecha) = MONTH(CURDATE()) AND YEAR(v.fecha) = YEAR(CURDATE())
                GROUP BY p.id ORDER BY Unidades DESC LIMIT 5;
                """)
                writer.writerow(["Productos mas vendidos (este mes)"])
                writer.writerow([desc[0] for desc in cursor.description])
                writer.writerows(cursor.fetchall())
                writer.writerow([])
                
                cursor.execute("""
                SELECT c.nombre AS Categoria,COUNT(DISTINCT v.id) AS Transacciones,SUM(dv.cantidad) AS Unidades,
                FORMAT(SUM(dv.cantidad*dv.precio_unitario),2) AS Ventas_Totales, FORMAT(COUNT(DISTINCT v.cliente_id) / COUNT(DISTINCT v.id) * 100,1) AS Fidelizacion
                FROM Categoria c
                INNER JOIN Producto p ON c.id = p.categoria_id
                INNER JOIN Detalle_Ventas dv ON p.id = dv.producto_id
                INNER JOIN Ventas v ON dv.venta_id = v.id
                GROUP BY c.id ORDER BY Ventas_Totales DESC;
                """)
                writer.writerow(["Ventas por categoria"])
                writer.writerow([desc[0] for desc in cursor.description])
                writer.writerows(cursor.fetchall())
                writer.writerow([])

            print(f"\n Reporte exportado correctamente como: {filename}")
        else:
            print("Selecciona una opcion valida")
    def Inventario(self):
        entrada = {
            1: "Compra",
            2: "Devolución",
            3: "Producción",
            4: "Otro"
        }
        salida = {
            1: "Consumo interno",
            2: "Daño",
            3: "Donacion",
        }
        ajuste = {
            1: "Conteo Fisico",
            2: "Caducidad",
            3: "Error"
        }
        print("== Gestion de inventario ==")
        opgi = int(input("1. Entrada(compra a proveedores)\n2. Salida(pérdidas)\n3. Ajustes\n4. Volver\nTu opcion: "))
        if opgi == 1:
            print("-- Entrada --")
            cursor.execute("SELECT id,nombre FROM Producto")
            for id,nombre in cursor.fetchall():
                print(f"{id}. {nombre}")

            producto_id = int(input("Ingresa el producto: "))
            cursor.execute("SELECT id FROM Categoria WHERE id = %s", (producto_id))
            if not cursor.fetchone():
                print("Selecciona un producto existente")
                return
            
            tipo = "entrada"
            cant = int(input("Ingresa la cantidad a agregar para el stock:"))
            if cant <= 0:
                print("Escoge una cantidad no negativa")
                return
            opcionmotivo = int(input("1. Compra \n2. Devolucion\n3. Produccion\n4. Otro\nTu opcion:"))

            if opcionmotivo in entrada:
                motivo = entrada[opcionmotivo]
            else:
                print("Opcion invalida")
            
            cursor.execute("INSERT INTO Movimiento_Inventario(producto_id,tipo,cantidad,fecha,motivo) VALUES(%s,%s,%s,%s,%s)",
                        (producto_id,tipo,cant,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),motivo))
            
            cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(producto_id))
            stock_actual = cursor.fetchone()[0]
            cursor.execute("UPDATE Producto SET stock_actual = %s WHERE id = %s",(stock_actual+cant,producto_id))

            conexion.commit()
            print("Entrada registrada correctamente.")

        elif opgi == 2:
            print("-- Salida --")
            cursor.execute("SELECT id,nombre FROM Producto")
            for id,nombre in cursor.fetchall():
                print(f"{id}. {nombre}")

            producto_id = int(input("Ingresa el producto: "))
            cursor.execute("SELECT id FROM Categoria WHERE id = %s", (producto_id))
            if not cursor.fetchone():
                print("Selecciona un producto existente")
                return
            
            cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(producto_id))
            cantidad = cursor.fetchone()[0]
            if int(cantidad) <= 0:
                print("No se puede disminuir el stock de este producto.")
                return
            
            tipo = "salida"
            cant = int(input("Ingresa la cantidad a disminuir del stock:"))
            if cant <= 0:
                print("Escoge una cantidad no negativa")
                return
            opcionmotivo = int(input("1. Consumo interno \n2. Daño\n3. Donacion\nTu opcion: "))

            if opcionmotivo in salida:
                motivo = salida[opcionmotivo]
            else:
                print("Opcion invalida")

            cursor.execute("INSERT INTO Movimiento_Inventario(producto_id,tipo,cantidad,fecha,motivo) VALUES(%s,%s,%s,%s,%s)",
                        (producto_id,tipo,cant,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),motivo))
            
            cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(producto_id))
            stock_actual = cursor.fetchone()[0]
            cursor.execute("UPDATE Producto SET stock_actual = %s WHERE id = %s",(stock_actual-cant,producto_id))

            conexion.commit()
            print("Salida registrada correctamente.")

        elif opgi == 3:
            print("-- Ajuste --")
            cursor.execute("SELECT id,nombre FROM Producto")
            for id,nombre in cursor.fetchall():
                print(f"{id}. {nombre}")

            producto_id = int(input("Ingresa el producto: "))
            cursor.execute("SELECT id FROM Categoria WHERE id = %s", (producto_id))
            if not cursor.fetchone():
                print("Selecciona un producto existente")
                return
            
            tipo = "ajuste"
            cant = int(input("Ingresa la cantidad (- para decremento): "))

            cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(producto_id))
            cantidad = cursor.fetchone()[0]
            if cant+int(cantidad) <= 0:
                print(f"A este producto no se le pueden decrementar {cant} unidades")
                return
            opcionmotivo = int(input("1. Conteo Fisico \n2. Caducidad\n3. Error\nTu opcion:"))

            if opcionmotivo in ajuste:
                motivo = ajuste[opcionmotivo]
            else:
                print("Opcion invalida")

            cursor.execute("INSERT INTO Movimiento_Inventario(producto_id,tipo,cantidad,fecha,motivo) VALUES(%s,%s,%s,%s,%s)",
                        (producto_id,tipo,cant,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),motivo))
            
            cursor.execute("SELECT stock_actual FROM Producto WHERE id = %s",(producto_id))
            stock_actual = cursor.fetchone()[0]
            cursor.execute("UPDATE Producto SET stock_actual = %s WHERE id = %s",(stock_actual+cant,producto_id))

            conexion.commit()
            print("Ajuste registrado correctamente.")
        else:
            print("Selecciona una opcion valida")
            
tda = Tienda()
tda.main()