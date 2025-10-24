 Proyecto Pre Entrega de Automation Testing
 
Proposito: Validar flujos básicos de Sauce Demo, Incluye automatización del login, verificación del catálogo de productos y validación del carrito de compras.


- **Python 3.13**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML**
- **Google Chrome / ChromeDriver**
- **Git / GitHub**



 Instalación de dependencias
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/EveAntonella/pre-entrega-automation-testing-evelinn-rodriguez.git
   cd pre-entrega-automation-testing-evelinn-rodriguez
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Agregar al Path las variables de entorno y scripts
   C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313\Scripts
   C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313


Ejecutar con comando pytest tests/

 🔐 Login
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
