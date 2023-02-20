import time
import pandas as pd
from retry import retry
from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from loguru import logger
from tqdm import tqdm

from kinvo.enum.xpaths import XPathsKinvoEnum


class KinvoScrapping:
    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password
        self.__url_base = "https://app.kinvo.com.br"
        self.__url_actives = self.__get_url_actives()
        self.__xpaths = XPathsKinvoEnum
        self.__navigator = Chrome()

    def execute(self, dataframe: pd.DataFrame):
        self.__login()
        self.__register_actives(dataframe)

    def __login(self):
        logger.info("Iniciando login.")
        self.__navigator.get(self.__url_base)
        logger.info("Preenchendo campo de e-mail.")
        self.__input_value_element(self.__xpaths.LOGIN_EMAIL.value, self.__email)
        logger.info("Preenchendo campo de senha.")
        self.__input_value_element(self.__xpaths.LOGIN_PASSWORD.value, self.__password)
        logger.info("Clicando em entrar.")
        self.__click_element(xpath_element=self.__xpaths.BUTTON_ENTRAR.value)
        logger.info("Aguardando login...")
        time.sleep(10)
        logger.info("Ok")

    def __register_actives(self, dataframe: pd.DataFrame):
        logger.info("Iniciando processo...")
        for active in tqdm(dataframe.to_dict("records")):
            logger.info(
                f"Registrando aportes ativo: {active['Ativo'][:5]} -  {active['Quantidade Compra']}"
            )
            url = [
                url for url in self.__url_actives if active["Ativo"][:5] in url
            ].pop()
            logger.info(f"Redirecionando URL: {self.__url_base}{url}")
            self.__navigator.get(f"{self.__url_base}{url}")
            logger.info(f"Clicando no botão: Editar Produto")
            self.__click_element(self.__xpaths.BUTTON_EDITAR_PRODUTO.value)
            logger.info(f"Clicando no botão: Adicionar")
            self.__click_element(self.__xpaths.BUTTON_ADICIONAR.value)
            logger.info(f"Clicando no botão: Aplicação")
            self.__click_element(self.__xpaths.BUTTON_APLICACAO.value)
            self.__input_values_aplicacao(active)
            logger.info(f"Processo finalizado, ativo: {active['Ativo']}")
            time.sleep(4)
        logger.info("Processo finalizado. Todos os ativos foram registrados!")

    def __input_values_aplicacao(self, active: dict):
        logger.info(f"Preenchendo campo: Quantidade")
        self.__input_value_element(
            self.__xpaths.FIELD_QUANTIDADE.value, active["Quantidade Compra"]
        )
        logger.info(f"Preenchendo campo: Cotação")
        self.__input_value_element(self.__xpaths.FIELD_COTACAO.value, active["Preco"])
        logger.info(f"Preenchendo campo: Data da compra")
        self.__input_value_element(
            self.__xpaths.FIELD_DATE.value, active["DataNegociacao"]
        )
        logger.info(f"Preenchendo campo: Taxas")
        self.__input_value_element(self.__xpaths.FIELD_TAXA.value, "0")
        logger.info(f"Clicando no botão: Confirmar")
        self.__click_element(self.__xpaths.BUTTON_CONFIRMAR.value)

    @retry(NoSuchElementException, tries=5, delay=6)
    def __input_value_element(self, xpath_element: str, value: str):
        element = self.__navigator.find_element("xpath", xpath_element)
        element.clear()
        element.send_keys(value)

    @retry(NoSuchElementException, tries=5, delay=6)
    def __click_element(self, xpath_element):
        element = self.__navigator.find_element("xpath", xpath_element)
        element.click()

    def __get_url_actives(self) -> []:
        return [
            "/carteira/detalhes-da-acao/RADL3/27607549",
            "/carteira/detalhes-da-acao/BBDC3/26510966",
            "/carteira/detalhes-da-acao/ITUB3/26510799",
            "/carteira/detalhes-da-acao/ENBR3/26510512",
            "/carteira/detalhes-da-acao/BBDC4/27606469",
            "/carteira/detalhes-da-acao/SANB11/26510950",
            "/carteira/detalhes-da-acao/TAEE11/26510489",
            "/carteira/detalhes-da-acao/EQTL3/26510532",
            "/carteira/detalhes-da-acao/EGIE3/26510452",
            "/carteira/detalhes-da-acao/MDIA3/27608361",
            "/carteira/detalhes-da-acao/BBAS3/26510940",
            "/carteira/detalhes-da-acao/MGLU3/26511064",
            "/carteira/detalhes-da-acao/SMAL11/26510689",
            "/carteira/detalhes-da-acao/IVVB11/36882350",
            "/carteira/detalhes-da-acao/BOVX11/26510700",
            "/carteira/detalhes-da-acao/HGRU11/25933245",
            "/carteira/detalhes-da-acao/XPML11/25950343",
            "/carteira/detalhes-da-acao/HSML11/27117625",
            "/carteira/detalhes-da-acao/HCTR11/25933308",
            "/carteira/detalhes-da-acao/VINO11/26270804",
            "/carteira/detalhes-da-acao/HGRE11/25933315",
            "/carteira/detalhes-da-acao/VRTA11/27366953",
            "/carteira/detalhes-da-acao/FIGS11/27117619",
            "/carteira/detalhes-da-acao/VSLH11/24892135",
            "/carteira/detalhes-da-acao/XPPR11/25459051",
            "/carteira/detalhes-da-acao/BCFF11/24858141",
            "/carteira/detalhes-da-acao/VILG11/26270821",
            "/carteira/detalhes-da-acao/URPR11/25639705",
            "/carteira/detalhes-da-acao/BTLG11/25319542",
            "/carteira/detalhes-da-acao/KNRI11/25459006",
            "/carteira/detalhes-da-acao/IRDM11/26270771",
            "/carteira/detalhes-da-acao/RECR11/26895217",
            "/carteira/detalhes-da-acao/MXRF11/25639720",
            "/carteira/detalhes-da-acao/WEGE3/26511316",
            "/carteira/detalhes-da-acao/B3SA3/26511020",
            "/carteira/detalhes-da-acao/ABEV3/26511196",
            "/carteira/detalhes-da-acao/PSSA3/26511040",
            "/carteira/detalhes-da-acao/FLRY3/26511120",
            "/carteira/detalhes-da-acao/CAML3/27608188",
            "/carteira/detalhes-da-acao/SAPR11/26510539",
            "/carteira/detalhes-da-acao/LREN3/26511098",
            "/carteira/detalhes-da-acao/QUAL3/26511140",
            "/carteira/detalhes-da-acao/HGLG11/25818784",
            "/carteira/detalhes-da-acao/CIEL3/45539986",
            "/carteira/detalhes-da-acao/KLBN4/53366629",
            "/carteira/detalhes-da-acao/SANB4/53366662",
            "/carteira/detalhes-da-acao/SAPR4/53366741",
            "/carteira/detalhes-da-acao/TAEE4/53366824",
            "/carteira/detalhes-da-acao/UNIP5/53366748",
            "/carteira/detalhes-da-acao/CPLE5/53366751"
        ]
