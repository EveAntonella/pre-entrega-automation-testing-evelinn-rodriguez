import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.mark.order(3)
def test_carrito(setup_teardown):
    driver = setup_teardown
    driver.get(URL)

    # Login
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Agregar el primer producto al carrito
    primer_boton = driver.find_elements(By.CLASS_NAME, "btn_inventory")[0]
    primer_boton.click()

    # Verificar que el contador del carrito se incremente
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", f"El contador del carrito no se actualizó correctamente. Valor actual: {contador}"

    # Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    # Validar que el producto esté en el carrito
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito != "", "El producto no se muestra en el carrito."
