import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

from src.models.empleado import Employee
from src.models.producto import Producto
from src.models.reportes import Reportes

# ---- Tests para Employee ----

def test_nombre_completo_con_inicial():
    emp = Employee(FirstName="Ana", MiddleInitial="M", LastName="Gómez")
    assert emp.nombre_completo() == "Ana M Gómez"

def test_nombre_completo_sin_inicial():
    emp = Employee(FirstName="Luis", MiddleInitial=None, LastName="Pérez")
    assert emp.nombre_completo() == "Luis Pérez"

def test_antiguedad_correcta():
    hace_5_anios = datetime.now() - timedelta(days=365 * 5)
    emp = Employee(HireDate=hace_5_anios)
    assert emp.antiguedad() == 5

def test_antiguedad_sin_fecha():
    emp = Employee()
    assert emp.antiguedad() is None

def test_es_mayor_de_edad_true():
    mayor = Employee(BirthDate=datetime.now() - timedelta(days=365 * 25))
    assert mayor.es_mayor_de_edad() is True

def test_es_mayor_de_edad_false():
    menor = Employee(BirthDate=datetime.now() - timedelta(days=365 * 16))
    assert menor.es_mayor_de_edad() is False

def test_es_mayor_de_edad_sin_fecha():
    emp = Employee()
    assert emp.es_mayor_de_edad() is None

def test_repr_empleado():
    emp = Employee(FirstName="Rosa", LastName="Martínez", HireDate=datetime.now() - timedelta(days=365 * 3))
    repr_str = repr(emp)
    assert "Rosa" in repr_str and "Martínez" in repr_str and "3 años" in repr_str


# ---- Tests para Producto ----

def test_aplicar_descuento_correcto():
    p = Producto(ProductName="Jabón", Price=100.0)
    p.aplicar_descuento(10)
    assert abs(p.Price - 90.0) < 1e-6

def test_aplicar_descuento_invalidos():
    p = Producto(ProductName="Jabón", Price=100.0)
    with pytest.raises(ValueError):
        p.aplicar_descuento(-5)
    with pytest.raises(ValueError):
        p.aplicar_descuento(150)

def test_es_alergico_true():
    for val in ['yes', 'true', 'sí', 'si', 'YES', 'Si']:
        p = Producto(IsAllergic=val)
        assert p.es_alergico() is True

def test_es_alergico_false():
    for val in ['no', 'false', 'none', '', None]:
        p = Producto(IsAllergic=val if val is not None else "")
        assert p.es_alergico() is False

def test_repr_producto():
    p = Producto(ProductName="Crema", Price=50, VitalityDays=365)
    rep = repr(p)
    assert "Crema" in rep and "50" in rep and "365" in rep


# ---- Tests para Reportes (con mocks) ----

@patch('src.models.reportes.ConectorBDD')
@patch('matplotlib.pyplot.show')
def test_productos_por_categoria(mock_show, mock_db):
    # Mock de df con datos
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.__getitem__.side_effect = lambda k: ['Cat1', 'Cat2'] if k == 'Categoria' else [10, 20]
    mock_db.return_value.ejecutar_sql.return_value = mock_df

    Reportes.productos_por_categoria()
    mock_show.assert_called_once()

@patch('src.models.reportes.ConectorBDD')
@patch('matplotlib.pyplot.show')
def test_ventas_por_empleado(mock_show, mock_db):
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.__getitem__.side_effect = lambda k: ['Juan', 'Ana'] if k == 'Nombre' else ['Perez', 'Lopez'] if k == 'Apellido' else [1000, 2000]
    mock_db.return_value.ejecutar_sql.return_value = mock_df

    Reportes.ventas_por_empleado()
    mock_show.assert_called_once()

@patch('src.models.reportes.ConectorBDD')
@patch('matplotlib.pyplot.show')
def test_mejores_clientes(mock_show, mock_db):
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.__getitem__.side_effect = lambda k: ['Juan', 'Ana'] if k == 'Nombre' else ['Perez', 'Lopez'] if k == 'Apellido' else [3000, 4000]
    mock_db.return_value.ejecutar_sql.return_value = mock_df

    Reportes.mejores_clientes(top_n=2)
    mock_show.assert_called_once()

@patch('src.models.reportes.ConectorBDD')
@patch('matplotlib.pyplot.show')
def test_productos_mas_vendidos(mock_show, mock_db):
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.__getitem__.side_effect = lambda k: ['Prod1', 'Prod2'] if k == 'Producto' else [50, 75]
    mock_db.return_value.ejecutar_sql.return_value = mock_df

    Reportes.productos_mas_vendidos(top_n=2)
    mock_show.assert_called_once()
