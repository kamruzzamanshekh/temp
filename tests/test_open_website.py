import time


def test_current_temperature_visible(driver):
    url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"
    driver.get(url)

    item = driver.find_element("xpath", "/html/body/div/div[3]/div/div[3]/a[7]/span")
    item.click()
    time.sleep(5)  # Wait for the page to load after clicking
    # Locate the element using XPath
    element = driver.find_element("xpath", '//*[@id="current"]/div/div/div[2]/div[1]/div/div/div/div[1]')

    # Get the text/value
    value = element.text.strip()
    print("Current weather value:", value)