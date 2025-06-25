import os
import time
from selene import browser
import pytest
import subprocess
from typing import Generator


@pytest.fixture(scope="function")
def open_page():
    yield
    browser.quit()


@pytest.fixture(scope="session", autouse=True)
def auto_open_allure_report(request: pytest.FixtureRequest) -> Generator:
    """Автоматически открывает Allure-отчет после выполнения всех тестов"""
    yield
    time.sleep(5)

    allure_results_dir = request.config.getoption("--alluredir")
    allure_report_dir = "./allure-report"

    if not os.path.exists(allure_results_dir):
        pytest.fail(f"Directory {allure_results_dir} does not exist!")

    # Проверка наличия результатов
    for _ in range(5):
        if os.listdir(allure_results_dir):
            break
        time.sleep(1)
    else:
        pytest.fail(f"No test results in {allure_results_dir} after waiting!")

    # Закрыть все плагины, которые могут мешать
    for plugin in request.config.pluginmanager.get_plugins():
        if hasattr(plugin, "close"):
            plugin.close()

    # Сгенерировать HTML-отчет
    subprocess.run(
        f"allure generate {allure_results_dir} -o {allure_report_dir} --clean",
        shell=True,
        check=True
    )

    # Открыть отчет в браузере
    subprocess.Popen(
        f"allure open {allure_report_dir}",
        shell=True
    )