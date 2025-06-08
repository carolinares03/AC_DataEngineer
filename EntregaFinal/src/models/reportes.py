# En src/models/reportes.py
import matplotlib.pyplot as plt
from src.db.conector import ConectorBDD
from utils.logging import log 

class Reportes:
    @staticmethod
    @log
    def productos_por_categoria():
        #Genera un gráfico de torta con la cantidad de productos por categoría.
        db = ConectorBDD()
        query = '''
            SELECT c.CategoryName AS Categoria, COUNT(p.ProductID) AS Cantidad
            FROM products p
            JOIN categories c ON p.CategoryID = c.CategoryID
            GROUP BY c.CategoryName;
        '''
        df = db.ejecutar_sql(query)

        if df.empty:
            print("No hay datos para generar el gráfico.")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(df['Cantidad'], labels=df['Categoria'], autopct='%1.1f%%', startangle=90)
        plt.title('Distribución de productos por categoría')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    @log
    def ventas_por_empleado():
        #Muestra un gráfico de barras con el total vendido por cada empleado
        db = ConectorBDD()
        query = '''
            SELECT e.FirstName AS Nombre, e.LastName AS Apellido, SUM(s.TotalPrice) AS TotalVendido
            FROM sales s
            JOIN employees e ON s.SalesPersonID = e.EmployeeID
            GROUP BY s.SalesPersonID;
        '''
        df = db.ejecutar_sql(query)

        if df.empty:
            print("No hay datos de ventas para mostrar.")
            return

        nombres = df['Nombre'] + " " + df['Apellido']
        plt.figure(figsize=(10, 6))
        plt.bar(nombres, df['TotalVendido'], color='skyblue')
        plt.xticks(rotation=45, ha='right')
        plt.title('Ventas totales por empleado')
        plt.ylabel('Total vendido ($)')
        plt.tight_layout()
        plt.show()

    @staticmethod
    @log
    def mejores_clientes(top_n=10):
        # Muestra los top N clientes que más compraron (total $)
        db = ConectorBDD()
        query = f'''
            SELECT cu.FirstName AS Nombre, cu.LastName AS Apellido, SUM(s.TotalPrice) AS TotalGastado
            FROM sales s
            JOIN customers cu ON s.CustomerID = cu.CustomerID
            GROUP BY s.CustomerID
            ORDER BY TotalGastado DESC
            LIMIT {top_n};
        '''
        df = db.ejecutar_sql(query)

        if df.empty:
            print("No hay datos de clientes para mostrar.")
            return

        nombres = df['Nombre'] + " " + df['Apellido']
        plt.figure(figsize=(10, 6))
        plt.barh(nombres[::-1], df['TotalGastado'][::-1], color='seagreen')
        plt.title(f'Top {top_n} clientes por monto gastado')
        plt.xlabel('Total gastado ($)')
        plt.tight_layout()
        plt.show()

    @staticmethod
    @log
    def productos_mas_vendidos(top_n=10):
        # Muestra los productos más vendidos por cantidad
        db = ConectorBDD()
        query = f'''
            SELECT p.ProductName AS Producto, SUM(s.Quantity) AS TotalVendido
            FROM sales s
            JOIN products p ON s.ProductID = p.ProductID
            GROUP BY s.ProductID
            ORDER BY TotalVendido DESC
            LIMIT {top_n};
        '''
        df = db.ejecutar_sql(query)

        if df.empty:
            print("No hay ventas registradas.")
            return

        plt.figure(figsize=(10, 6))
        plt.barh(df['Producto'][::-1], df['TotalVendido'][::-1], color='coral')
        plt.title(f'Top {top_n} productos más vendidos')
        plt.xlabel('Cantidad vendida')
        plt.tight_layout()
        plt.show()