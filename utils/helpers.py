def validar_url(driver, texto):
    return texto in driver.current_url
