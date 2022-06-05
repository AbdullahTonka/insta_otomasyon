from  selenium import webdriver
import time


insta_isim="rickintheworld"
insta_sifre="oldrick123"


while True:
    isim = 'rickintheworld'
    sifre = 'oldrick123'
    takip_edilecek_hesap_isim='aykutelmas'

    if isim==insta_isim and sifre==insta_sifre:
        print("--------giriş başarılı--------")
        browser = webdriver.Chrome("C:\\Users\\admin\\Desktop\\WebDriver\\chromedriver.exe"),
        browser.get('https://www.instagram.com/accounts/login/?hl=tr')
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(insta_isim)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(insta_sifre)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)

        x = input('işlemi tekrarlamak için --Enter-- tuşuna basınız.')

    else:
        print("kullanıcı adı veya şifre hatalı")
        x=input('işlemi tekrarlamak için --Enter-- tuşuna basınız.')
