from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_card_links(driver, end_page):
    card_links = []
    for page in range(1, end_page+1):
        url = f'https://www.computeruniverse.net/en/c/hardware-components/pci-express-graphics-cards?page={page}'
        driver.get(url)

        g_cards = driver.find_element(
            by=By.CLASS_NAME, value='c-pl__main--rows'
        ).find_elements(by=By.CLASS_NAME, value='c-productItem')

        # card_links = [card.find_element(by=By.CLASS_NAME, value='c-productItem__head__name').get_attribute('href') for card in g_cards]

        for g_card in g_cards:
            card_links.append(g_card.find_element(by=By.CLASS_NAME, value='c-productItem__head__name').get_attribute('href'))
    return card_links


def get_end_page(driver):
    url = 'https://www.computeruniverse.net/en/c/hardware-components/pci-express-graphics-cards'
    driver.get(url)

    paginations = driver.find_elements(by=By.CLASS_NAME, value='Pagination__naviButton__inner')
    for a_elem in paginations[::-1]:
        if a_elem.text.isnumeric():
            return int(a_elem.text)


def parse_card_page(driver, url):
    driver.get(url)

    price_div = driver.find_element(by=By.CLASS_NAME, value='price-box')
    price = price_div.find_elements(by=By.TAG_NAME, value='span').text

    print(price_div)



def main():
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # end_page = get_end_page(driver)
    # card_links = get_card_links(driver, end_page)
    # for card in card_links:
    #     print(card)

    url = 'https://www.computeruniverse.net/en/p/90836256'
    parse_card_page(driver, url)

if __name__ == '__main__':
    main()
