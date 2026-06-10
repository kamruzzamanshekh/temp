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

    temp = driver.find_element("css selector", "div.display-temp")

    assert temp.is_displayed(), "Temperature is not visible"
    assert temp.text.strip() != "", "Temperature value is empty"