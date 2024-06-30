from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

data = {}
produk = []
harga = []
rating = []

driver = webdriver.Chrome()

for page in range(1, 5):
    driver.get(f"https://www.tokopedia.com/search?navsource=home&page={page}&q=tenda%20camping&source=universe&srp_component_id=02.02.01.02&st=product")
    jumlah_scroll = 18

    for _ in range(jumlah_scroll):
        driver.execute_script("window.scrollBy(0, 300);")  # Menggulir 300 piksel ke bawah
        time.sleep(5)

    tenda = driver.find_elements(By.XPATH, "//span[@class='OWkG6oHwAppMn1hIBsC3pQ==']")
    harga_produk = driver.find_elements(By.XPATH, "//div[@class='_8cR53N0JqdRc+mQCckhS0g== Phc0SDQ0Yjt43vf3XuwYOg==']")
    rating_produk = driver.find_elements(By.XPATH, "//span[@class='nBBbPk9MrELbIUbobepKbQ==']")


    for produk_tenda in tenda:
        if produk_tenda:
            produk.append(produk_tenda.text)
        else:
            produk.append("Unknown")

    for harga_tenda in harga_produk:
        if harga_tenda:
            harga.append(harga_tenda.text)
        else:
            harga.append("Unknown")

    for rating_tenda in rating_produk:
        if rating_tenda:
            rating.append(rating_tenda.text)
        else:
            rating.append("Unknown")
    
# Check for mismatched lengths and adjust
max_length = max(len(produk), len(harga), len(rating))

# Ensure all lists are the same length
while len(produk) < max_length:
    produk.append("Unknown")
while len(harga) < max_length:
    harga.append("Unknown")
while len(rating) < max_length:
    rating.append("Unknown")


data['Tenda'] = produk
data['harga'] = harga
data['rating'] = rating

df = pd.DataFrame(data)
df.to_csv('tenda_tokopedia.csv', index=False)

driver.quit()
