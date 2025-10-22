import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import os
from utils.driver_factory import create_driver

@pytest.fixture
def setup_teardown(request):
    driver = create_driver()
    yield driver  # Aquí se ejecuta el test

    # --- SOLO si el test falló ---
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
        driver.save_screenshot(screenshot_path)

    driver.quit()

# Hook para registrar el resultado del test (necesario para saber si falló)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)
