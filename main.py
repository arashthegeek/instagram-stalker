#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep as sl

def main(username):
    chrome_path = "C:\\Program Files\\chrome-win64\\chrome.exe" #آدرس exe کروم شما
    chrome_driver_path = "C:\\Users\\USER\\Desktop\\instagram stalker\\chromedriver-win64\\chromedriver.exe" #آدرس درایور کروم سلنیوم مختص بر نسخه کروم شما
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:\\Users\\(YourUser)\\AppData\\Local\\Google\\Chrome for Testing\\User Data") # ساب آدرس پروفایل کروم شما و در این مورد از کروم فور تستینگ استفاده شده که دایرکتوری با دایرکتوری کروم عادی فرق دارد
    chrome_options.add_argument("profile-directory=Default") #نام پروفایل شما که Default به معنای پروفایلی که بصورت خودکار استفاده میکند(کروم)
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.binary_location = chrome_path
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    input('Start VPN, login into your acconunt and Press Enter...')
    driver.get(f"https://www.instagram.com/{username}/")
    input("Page was Up then Press Enter...")
    texts = driver.find_elements(By.CSS_SELECTOR, '.x18hxmgj')
    #texts[2] is followers
    #texts[3] is followings
    texts[2].click() #با توجه به موردی که شما میخواهید استفاده کنید این خط را تغییر دهید
    input("iframe was ready then Press Enter...")
    pages_list = []
    while True:
        elements = driver.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for i in elements:
            pages_list.append(i.text.split('\n')[0])
        driver.execute_script('document.querySelector(".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6").scrollTo(0, document.querySelector(".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6").scrollHeight);')
        sl(3) #این مورد بستگی به سرعت عملکرد اینترنت و فیلترشکن شما دارد که در رابطه عکس با سرعت دارد
        newelements = driver.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        if newelements[len(newelements)-1] == elements[len(elements)-1]: break
        
    sorted_pl = list(set(pages_list)) #برای جلوگیری از بهم ریختگی های احتمالی(بر اثر سرعت اینترنت یا غیره...)
    print(sorted_pl)

if __name__ == "__main__":
    username = input("Username: ")
    main(username)