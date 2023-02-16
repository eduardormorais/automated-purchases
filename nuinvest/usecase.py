from retry import retry
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from loguru import logger

from nuinvest.enum.xpaths import XPathsNuInvestEnum


class NuInvestScrapping:
    def __init__(self, cpf, password, electronic_signature, directory_screenshot):
        self._cpf = cpf
        self._password = password
        self._electronic_signature = electronic_signature
        self._directory_screenshot = directory_screenshot
        self.__xpaths = XPathsNuInvestEnum
        self._navigator = Chrome()
        self._action = ActionChains(self._navigator)

    def execute(self, dataframe: pd.DataFrame):
        self.__login()
        self.__buy_all_actives(dataframe)

    def __login(self):
        self._navigator.get(
            "https://www.nuinvest.com.br/investir/renda-variavel/pedidos"
        )
        element_cpf = self._navigator.find_element(
            "xpath", self.__xpaths.FIELD_CPF.value
        )
        element_password = self._navigator.find_element(
            "xpath", self.__xpaths.FIELD_PASSWORD.value
        )
        element_cpf.send_keys(self._cpf)
        element_password.send_keys(self._password)
        element_cpf.send_keys(Keys.ENTER)

    def __buy_all_actives(self, actives: pd.DataFrame):
        for active in actives.to_dict("records"):
            logger.info(
                f"[x] Comprando: {active['key']} Quantidade: {active['quantity']}"
            )
            self._find_and_click_active_in_list(active.get("key"))
            self._buy_active(active.get("key"), int(active.get("quantity")))

    def _buy_active(self, active_key: str, quantity: int):
        logger.info("Clica em comprar")
        self._click_element(self.__xpaths.BUTTON_ON_BUY.value)
        logger.info("Clica em concordar com os termos de politica")
        self._click_element(self.__xpaths.BUTTON_AGREE_POLICY_TERMS.value)
        logger.info("Clica em continuar")
        self._click_element(self.__xpaths.BUTTON_CONTINUE.value)

        try:
            logger.info("Clica na aba, valor desejado")
            self._click_element(self.__xpaths.ABA_DESIRED_VALUE.value)
            logger.info("Clica em ok")
            self._click_element(self.__xpaths.BUTTON_OK.value)
        except ElementNotInteractableException:
            pass

        logger.info(f"Seleciona a quantidade de ativos a comprar: {quantity}")
        self._input_value_element(
            self.__xpaths.FIELD_QUANTITY_TO_BUY.value,
            str(quantity),
        )

        self._save_screenshot(
            self.__xpaths.CARD_SCREENSHOT.value,
            active_key,
        )
        logger.info("Clica em comprar")
        self._click_element(
            self.__xpaths.BUTTON_CONFIRM_BUY.value,
        )
        logger.info(f"Informa assinatura eletronica")
        self._input_value_element(
            self.__xpaths.FIELD_ELETRONIC_ASS.value,
            self._electronic_signature,
        )
        logger.info(f"Clica em confirmar assinatura eletronica")
        self._click_element(self.__xpaths.BUTTON_CONFIRM_ELETRONIC_ASS.value)
        logger.info(f"Clica em ver meus pedidos")
        self._click_element(self.__xpaths.BUTTON_SEE_MY_REQUESTS.value)

    def _find_and_click_active_in_list(self, active_key: str):
        self._input_value_element(self.__xpaths.FIELD_FILTER_ACTIVE.value, active_key)
        self._click_element(self.__xpaths.CARD_ACTIVE.value)

    @retry(NoSuchElementException, tries=5, delay=4)
    def _input_value_element(self, xpath_element: str, value: str):
        element = self._navigator.find_element("xpath", xpath_element)
        element.clear()
        element.send_keys(value)

    @retry(NoSuchElementException, tries=15, delay=3)
    def _click_element(self, xpath_element):
        element = self._navigator.find_element("xpath", xpath_element)
        element.click()

    @retry(NoSuchElementException, tries=5, delay=4)
    def _save_screenshot(self, xpath_element: str, filename: str):
        element = self._navigator.find_element("xpath", xpath_element)
        self._action.move_to_element(element).perform()
        time.sleep(1)
        self._navigator.get_screenshot_as_file(
            f"{self._directory_screenshot}/{filename}.png"
        )
