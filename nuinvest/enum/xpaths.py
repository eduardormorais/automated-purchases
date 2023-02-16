from enum import Enum


class XPathsNuInvestEnum(Enum):
    FIELD_CPF = "//*[@id='username']"
    FIELD_PASSWORD = "//*[@id='password']"
    BUTTON_ON_BUY = (
        "//*[@id='main-container']/div[4]/div/div[2]/div/div/div/div[1]/div[1]/button"
    )
    BUTTON_AGREE_POLICY_TERMS = (
        "//*[@id='main-container']/div[4]/div/div[2]/div/div/section/label/span/span"
    )
    BUTTON_CONTINUE = "//*[@id='main-container']/div[4]/div/div[2]/div/div/section/a[2]"
    ABA_DESIRED_VALUE = "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[1]/div/div[1]/ul/li[2]/div"
    BUTTON_OK = "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[1]/div/div[1]/ul/li[2]/div/div/div/div/a"
    FIELD_QUANTITY_TO_BUY = "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[1]/div/div[2]/section/div/div[3]/div/div/div[1]/input"
    CARD_SCREENSHOT = (
        "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[3]/button"
    )
    BUTTON_CONFIRM_BUY = (
        "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[3]/button"
    )
    FIELD_ELETRONIC_ASS = (
        "/html/body/div[2]/div/div[4]/div/div[2]/div/div/form/div/div[1]/input"
    )
    BUTTON_CONFIRM_ELETRONIC_ASS = (
        "/html/body/div[2]/div/div[4]/div/div[2]/div/div/form/button"
    )
    BUTTON_SEE_MY_REQUESTS = (
        "/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div[3]/button"
    )
    FIELD_FILTER_ACTIVE = "//*[@id='main-container']/div[3]/div/div/div/input"
    CARD_ACTIVE = "//*[@id='main-container']/div[3]/div/div/div[2]/ul/li/div"
