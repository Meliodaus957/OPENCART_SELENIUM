# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Настройки WebDriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 15)
#
# # URL административной панели
# admin_url = 'http://192.168.0.112:8081//administration/'
#
# # Данные для входа
# username = 'user'
# password = 'bitnami'
#
# try:
#     # 1️⃣ Авторизация в административной панели
#     driver.get(admin_url)
#     wait.until(EC.presence_of_element_located((By.ID, 'input-username'))).send_keys(username)
#     driver.find_element(By.ID, 'input-password').send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#     # 2️⃣ Переход к разделу добавления товара
#     wait.until(EC.presence_of_element_located((By.ID, 'menu-catalog'))).click()
#     wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Products'))).click()
#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.page-header > div > div > a'))).click()
#
#     # 3️⃣ Заполнение вкладки "General"
#     wait.until(EC.presence_of_element_located((By.ID, 'input-name-1'))).send_keys('sad')
#     driver.find_element(By.ID, 'input-meta-title-1').send_keys('sad')
#
#     # 4️⃣ Переход на вкладку "Data"
#     driver.find_element(By.LINK_TEXT, 'Data').click()
#     wait.until(EC.presence_of_element_located((By.ID, 'input-model'))).send_keys('sad')
#
#     # 5️⃣ Переход на вкладку "SEO" и заполнение Keyword
#     driver.find_element(By.LINK_TEXT, 'SEO').click()
#     seo_input = wait.until(EC.presence_of_element_located((By.NAME, "product_seo_url[0][1]")))
#     seo_input.send_keys("sad")
#
#     # 6️⃣ Сохранение товара
#     driver.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > button').click()
#
#     # 7️⃣ Проверка успешного сохранения
#     success_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert-success')))
#     assert 'Success: You have modified products!' in success_alert.text
#
# finally:
#     # Закрытие браузера
#     driver.quit()
