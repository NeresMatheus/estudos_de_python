# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": str(ROOT_FOLDER / 'pdfs'),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


def download_diario(ano, mes, dia):
    TIME_TO_WAIT = 10

    result = ''

    # options = '--headless',

    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.jornalminasgerais.mg.gov.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'dataJornal')
        )
    )
    search_input.send_keys(dia)
    search_input.send_keys(mes)
    search_input.send_keys(ano)
    try:
        browser.find_element(By.ID, 'pesquisarSomenteData').click()
        browser.find_element(By.ID, 'linkDownloadPDF').click()
        sleep(TIME_TO_WAIT)
        result = (str(dia) + '/' + str(mes) + '/' + str(ano), 'succeed')
    except:
        result = (str(dia) + '/' + str(mes) + '/' + str(ano), 'failed')

    return result


if __name__ == '__main__':
    resultado = download_diario(2023, 7, 20)
    print(resultado)
    TIME_TO_WAIT = 10
