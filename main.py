from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
data = {}
produk = []
harga_produk = []

for page in range(1,5):
    driver.get(f"https://www.tokopedia.com/search?navsource=home&page={page}&q=tenda%20camping&source=universe&srp_component_id=02.02.01.02&st=product")
    jumlah_guliran = 17

    # Tentukan waktu penundaan (dalam detik) antara setiap pengguliran
    waktu_tunggu = 2

    # Lakukan pengguliran dengan menggunakan JavaScript
    for _ in range(jumlah_guliran):
        # Eksekusi JavaScript untuk menggulir ke bawah
        driver.execute_script("window.scrollBy(0, 300);")  # Menggulir 300 piksel ke bawah
    
        # Tunggu beberapa waktu sebelum melakukan pengguliran berikutnya
        time.sleep(waktu_tunggu)
    nama = driver.find_elements(By.XPATH,"//div[@class='prd_link-product-name css-3um8ox']")
    harga = driver.find_elements(By.XPATH,"//div[@class='prd_link-product-price css-h66vau']")

    for nama_produk in nama:
        produk.append(nama_produk.text)
        print(nama_produk.text)

    for price in harga:
        harga_produk.append(price.text)
        print(price.text)

data['Produk'] = produk
data['Harga'] = harga_produk
df = pd.DataFrame(data)
df.to_csv('tokopedia.csv')

driver.quit()