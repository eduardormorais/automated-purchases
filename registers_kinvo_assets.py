import os
from pwinput import pwinput
from kinvo.usecase import KinvoScrapping
from utils import read_file_registros_csv, select_option_user
from loguru import logger
from dotenv import load_dotenv


def read_user_inputs():
    _email = input("E-mail: ")
    _password = pwinput("Password: ")
    return _email, _password


if __name__ == "__main__":
    load_dotenv()
    PATH_DATA = os.environ["PATH_DATA_KINVO"]
    logger.info(
        "**************************** Dados para a operação ****************************"
    )
    logger.info("Planilha de compras: ")
    path_data = select_option_user(PATH_DATA)
    df_negociacoes = read_file_registros_csv(path_data)
    email, password = read_user_inputs()
    logger.info(f"Base de ativos: {df_negociacoes}")
    KinvoScrapping(email, password).execute(df_negociacoes)
