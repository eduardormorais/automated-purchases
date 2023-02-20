from enum import Enum


class XPathsKinvoEnum(Enum):
    LOGIN_EMAIL = "//*[@id='root']/div/div[1]/main/div/form/div[1]/div[1]/div/input"
    LOGIN_PASSWORD = "//*[@id='root']/div/div[1]/main/div/form/div[1]/div[2]/div/input"
    BUTTON_ENTRAR = "/html/body/div/div/div[1]/main/div/form/div[2]/button"
    BUTTON_EDITAR_PRODUTO = "//*[@id='root']/div/div[1]/div[2]/main/div/div/header/div/div[2]/div/a/div[1]"
    BUTTON_ADICIONAR ="/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/header/div/div/div[1]/div/button"
    BUTTON_APLICACAO ="/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/header/div/div/div[2]/div[1]"
    FIELD_QUANTIDADE = "/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/section/form/div/div[2]/div[1]/div/input"
    FIELD_COTACAO = "/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/section/form/div/div[2]/div[2]/input[1]"
    FIELD_DATE ="/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/section/form/div/div[2]/div[3]/input"
    FIELD_TAXA ="/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/section/form/div/div[2]/div[4]/input[1]"
    BUTTON_CONFIRMAR ="/html/body/div[1]/div/div[1]/div[2]/main/section/main/div[2]/section[1]/div/section[2]/section/form/div/div[3]/button"
