import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Optional: start maximized
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver  # Provide the driver to the test
    
    # Teardown
    driver.quit()