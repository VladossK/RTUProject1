import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import bs4
import smtplib
from email.mime.text import MIMEText


def product_parcing(product_name):
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    url = "https://www.rimi.lv/e-veikals?utm_source=web&utm_medium=link"
    driver.get(url)
    time.sleep(2)

    click_cookie=driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    click_cookie.click()

    time.sleep(2)

    # JA IR BANNERS
    try:
        click_banner=driver.find_element(By.CLASS_NAME, "modal__close")   
        click_banner.click()
    except: 
        pass

    click_search=driver.find_element(By.ID, "search-input")
    click_search.send_keys(product_name)
    click_search.send_keys(Keys.ENTER)

    url = driver.current_url
    get_info = requests.get(url)

    if get_info.status_code == 200:
        web_info=bs4.BeautifulSoup(get_info.content, 'html.parser')
        find_name=web_info.find_all(class_="card__name")
        find_price=web_info.find_all(class_="price-tag card__price")
        cena = []
        # Cenu parsing
        for i in find_price:
            euro = i.findChild("span").string
            cents = i.findChild("sup").string
            price = f'{euro}.{cents}€'
            cena.append(price)
        # Produktu parcing 
        produkti = []
        for product in find_name:
            product = product.string
            produkti.append(product)
        # Pievenoju uz vārdnicu 
        final = dict(zip(produkti, cena))
        return final
    driver.quit()


def choose():

    name = input("Lūdzu, ievadiet produkta nosaukumu: ")
    result = product_parcing(name)
    products = []

    # Show products un append
    for i, (key,value) in enumerate(result.items(),1):
        print(f"{i}.{key} {value}")
        temp = (f"{key} {value}")
        products.append(temp)

    choice = int(input("Kadu numuru pievienot grozā? (0 = nekādu) "))
    if choice == 0 or choice > 20 or choice < 0 :
        return 
    
    key, value = list(result.items())[choice-1]
    print(f"Produkts {key} ir pievienots grozam")
    return key, value 
    

def send_email(pirkumi,date,mail,full_price):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    flag = True 
    while flag == True:
        try:
            # Authentication
            s.login("remindermr9@gmail.com", "vevv yivi hptn qigq")
            # message to be sent
            message = MIMEText('Šis dienas pirkumi: \n\n'+"\n".join(pirkumi) + f"\n\n\t\tPilna cena: {full_price:.2f}€")
            message["Subject"] = f'Veikala apmeklējums {date}'
            # sending the mail
            s.sendmail("remindermr9@gmail.com", mail, message.as_string())
            print("Ziņojums ir veiksmīgi nosūtīts.")
            flag = False 
        except:
            print("Nosūtot ziņojumu, radās kļūda")
            flag = True
            mail = input("Lūdzu, ievadit e-mail atkartoti: ")
    # terminating the session
    s.quit()


#join
def main():

    groza = []
    choose_yn = 'y'
    count = 0
    while choose_yn == 'y':
        temp = choose()
        if temp is not None:
            full_price = float(temp[1].replace("€", ""))
            count += full_price
            app = " ".join(temp)
            groza.append(app)
        choose_yn = input('Vai vēlaties pievienot vēl? (y/n) ').lower()

    e_mail = input('Lūdzu, ievadiet e-pasta adresi, kur nosutīt piezīmi: ')
    data = input('Kurā datumā vēlaties apmeklēt veikalu? ')
    
    send_email(groza, data, e_mail, count)
    
main()
