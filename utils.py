from datetime import datetime
from loguru import logger
import pandas as pd
import os


def create_directory_screenshot(path_screenshots: str, path_data_buys: str):
    new_path_splt = path_data_buys.split("/")
    new_path = new_path_splt[len(new_path_splt) - 1].split(".")[0]
    if not os.path.exists(f"{path_screenshots}/screenshots/{new_path}"):
        os.makedirs(f"{path_screenshots}/screenshots/{new_path}")
    return f"{path_screenshots}/screenshots/{new_path}"


def read_file_buys_csv(filepath: str) -> pd.DataFrame:
    dataframe_actives = pd.read_csv(filepath)
    dataframe_actives = dataframe_actives[dataframe_actives["quantity"] > 0]
    return dataframe_actives


def read_file_registros_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=";", encoding="utf-8", on_bad_lines="skip")
    df = df.rename(columns={"Dt. Negocia��o": "DataNegociacao", "Pre�o": "Preco"})
    return df


def orderning_files_by_date(base_path: str, files: list) -> list:
    data_files = []
    for file_name in files:
        file_time = os.path.getctime(f"{base_path}/{file_name}")
        date = datetime.fromtimestamp(file_time).strftime("%Y-%m-%d %H:%M:%S")
        data_files.append({"date": date, "file_name": file_name})

    data_files.sort(key=lambda item: item["date"], reverse=False)
    return data_files


def select_option_user(base_path: str) -> str:
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    files = os.listdir(base_path)
    data_files = orderning_files_by_date(base_path, files)
    if len(data_files) == 0:
        logger.error("Arquivos nao encontrados.")
        raise UserInputError(f"Arquivos nao encontrados. {base_path}")

    index = 0
    for file in data_files:
        index += 1
        logger.info(f"{index} - {file['date']} - {file['file_name']}")

    index_file = int(input("Executar a paritr da planilha: "))
    file_select = data_files[int(index_file) - 1]
    logger.info(
        f"Arquivo selecionado: {file_select['date']} - {file_select['file_name']}"
    )
    path = f"{base_path}/{file_select['file_name']}"
    return path


class UserInputError(Exception):
    """Expection for user input values."""
