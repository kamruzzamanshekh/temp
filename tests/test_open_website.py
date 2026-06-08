def test_open_website(driver):
    url = "https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143"  # Change this to your target website
    driver.get(url)
    driver.implicitly_wait(100) 