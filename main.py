from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get("https://google.com.ua")
    elem = driver.find_element(By.NAME, 'q')
    elem.clear()
    elem.send_keys("Python Developer")
    elem.send_keys(Keys.RETURN)
    results = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
    for result in results[:5]:
        link = result.find_element(By.TAG_NAME, 'a')
        title = result.find_element(By.TAG_NAME, 'h3')
        print(f"{link.get_attribute('href')} - {title.text}")

    driver.close()


if __name__ == "__main__":
    main()
