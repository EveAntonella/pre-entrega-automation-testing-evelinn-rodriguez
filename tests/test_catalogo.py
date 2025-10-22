import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.mark.order(2)
def test_verificacion_catalogo(setup_teardown):
    driver = setup_teardown
    driver.get(URL)

    # Login
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Validar título de la página
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products", "El título de la página no es correcto."

    # Verificar que haya al menos un producto visible
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el inventario."

    # Verificar elementos importantes de la interfaz
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "El menú lateral no está visible."
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "El filtro de productos no está visible."

    # Listar nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\nPrimer producto: {nombre} - {precio}")
