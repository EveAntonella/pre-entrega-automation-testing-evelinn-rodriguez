# 🧪 Proyecto de Automation Testing - Pre Entrega

## 🎯 Propósito del proyecto
Este proyecto automatiza flujos básicos del sitio https://www.saucedemo.com, aplicando los conocimientos adquiridos hasta la Clase 8.  
Incluye automatización del login, verificación del catálogo de productos y validación del carrito de compras.

---

## 🧰 Tecnologías utilizadas
- **Python 3.13**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML**
- **Google Chrome / ChromeDriver**
- **Git / GitHub**

---

## ⚙️ Instalación de dependencias
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ariadna-rodriguez/pre-entrega-automation-testing-ariadna-rodriguez.git
   cd pre-entrega-automation-testing-ariadna-rodriguez
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Agregar al Path las variables de entorno y scripts, por ejemplo:
   C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313\Scripts
   C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313

---
## ▶️ Ejecución de las pruebas

Ejecutar con comando pytest tests/

## 📋 Casos de prueba incluidos

### 🔐 Login
- Navega a `saucedemo.com`
- Ingresa credenciales válidas
- Verifica redirección a `/inventory.html`
- Comprueba título “Products”

### 🧭 Catálogo
- Verifica título correcto (“Products”)
- Comprueba que existan productos visibles
- Valida presencia de menú y filtro
- Lista nombre y precio del primer producto

### 🛒 Carrito
- Añade el primer producto al carrito
- Verifica incremento del contador
- Navega al carrito y confirma producto agregado

---

## 📊 Reportes y Evidencias
- Reporte HTML: `reports/reporte.html`
- Capturas automáticas en caso de fallo: `reports/screenshots/`

---

## 👩‍💻 Autor
**Ariadna Rodríguez**  
Curso: *Testing Automatizado con Python y Selenium*  
Pre-entrega del Proyecto Final - Clase 8
