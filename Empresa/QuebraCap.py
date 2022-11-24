from impulse import Solver
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://democaptcha.com/demo-form-eng/hcaptcha.html")
    solver = Solver(driver)
    solver.run()