def test_open_website(driver):
    url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"  # Change this to your target website
    driver.get(url)
    driver.implicitly_wait(100) 

def test_page_title_contains_dhaka(driver):
    url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"
    driver.get(url)

    assert "Dhaka" in driver.title, "Page title does not contain Dhaka"

def test_current_temperature_visible(driver):
    url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"
    driver.get(url)

    item = driver.find_element("xpath", "/html/body/div/div[3]/div/div[3]/a[7]/span")
    item.click()
    # Locate the element using XPath
    element = driver.find_element("xpath", '//*[@id="current"]/div/div/div[2]/div[1]/div/div/div/div[1]')

    # Get the text/value
    value = element.text.strip()
    print("Current weather value:", value)