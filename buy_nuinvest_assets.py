import os
from dotenv import load_dotenv
from loguru import logger
from pwinput import pwinput
from nuinvest.usecase import (
    NuInvestScrapping,
)
from utils import read_file_buys_csv, create_directory_screenshot, select_option_user


def read_user_inputs():
    _cpf = input("CPF: ")
    _password = pwinput("Password: ")
    _eletronic_ass = pwinput("Eletronic Ass: ")
    return _cpf, _password, _eletronic_ass


if __name__ == "__main__":
    load_dotenv()
    PATH_DATA = os.environ["PATH_DATA_NUINVEST"]
    PATH_SCREENSHOTS = os.environ["PATH_SCREENSHOTS"]
    logger.info(
        "**************************** Dados para a operação ****************************"
    )
    logger.info("Planilha de compras: ")
    path_data = select_option_user(PATH_DATA)
    directory_screenshot = create_directory_screenshot(PATH_SCREENSHOTS, path_data)
    cpf, password, eletronic_ass = read_user_inputs()
    df_actives = read_file_buys_csv(path_data)
    logger.info(f"Compras: {df_actives}")
    NuInvestScrapping(cpf, password, eletronic_ass, directory_screenshot).execute(
        df_actives
    )
