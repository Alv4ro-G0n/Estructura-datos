import pytest
from proyecto.inventario import agregar_producto, actualizar_stock, eliminar_producto, buscar_producto, inventario, salir

@pytest.fixture
def clean_inventario():
    inventario.clear()
    yield
    inventario.clear()

def test_agregar_producto(clean_inventario):
    result = agregar_producto('Producto1', 10, 15.50)
    assert result == "Producto 'Producto1' agregado con éxito."
    assert 'Producto1' in inventario
    assert inventario['Producto1']['cantidad'] == 10
    assert inventario['Producto1']['precio'] == 15.50

def test_actualizar_stock(clean_inventario):
    inventario['Producto1'] = {'nombre': 'Producto1', 'cantidad': 10, 'precio': 15.50}
    result = actualizar_stock('Producto1', 20)
    assert result == "Stock del producto 'Producto1' actualizado con éxito."
    assert inventario['Producto1']['cantidad'] == 20

def test_eliminar_producto(clean_inventario):
    inventario['Producto1'] = {'nombre': 'Producto1', 'cantidad': 10, 'precio': 15.50}
    result = eliminar_producto('Producto1')
    assert result == "Producto 'Producto1' eliminado con éxito."
    assert 'Producto1' not in inventario

def test_buscar_producto(clean_inventario):
    inventario['Producto1'] = {'nombre': 'Producto1', 'cantidad': 10, 'precio': 15.50}
    result = buscar_producto('Producto1')
    assert result == {
        'nombre': 'Producto1',
        'cantidad': 10,
        'precio': 15.50
    }

def test_buscar_producto_no_existe(clean_inventario):
    result = buscar_producto('ProductoInexistente')
    assert result == "El producto no se encuentra en el inventario."

def test_salir(clean_inventario):
    inventario['Producto1'] = {'nombre': 'Producto1', 'cantidad': 10, 'precio': 15.50}
    result = salir()
    assert result == "Inventario limpio, fin del programa."
    assert len(inventario) == 0
