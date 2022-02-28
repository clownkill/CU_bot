from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def all_cards_parse():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://www.computeruniverse.net/en/c/hardware-components/pci-express-graphics-cards'
    driver.get(url)

    g_cards = driver.find_element(
        by=By.CLASS_NAME, value='c-pl__main--rows'
    ).find_elements(by=By.CLASS_NAME, value='c-productItem')
    for g_card in g_cards:
        card_name = g_card.find_element(by=By.CLASS_NAME, value='c-productItem__head__name').text
        card_href = g_card.find_element(by=By.CLASS_NAME, value='c-productItem__head__name').get_attribute('href')
        print(f'{card_name}\t{card_href}')


def main():
    all_cards_parse()


if __name__ == '__main__':
    main()
