from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from time import sleep
import warnings
import pwinput
import platform

warnings.filterwarnings("ignore", category=DeprecationWarning) 

takiplistesi = []
takipcilistesi = []

chrome_options = chromeOptions()
chrome_options.headless = True

firefox_options = firefoxOptions()
firefox_options.headless = True

class Program:
    def __init__(self,driver):
        try:
            print('\033c')
            self.program = driver
            Program.ascii(self)
            self.menu = int(input('\033c'+self.index+'\n[1] İki Aşamalı Doğrulama ile\n[2] Normal Giriş (Daha stabil çalışır.)\n\nINPUT: '))
            print('\033c', self.index)
            Program.instagram(self)

        except (ZeroDivisionError, ValueError):
            print('\033c'+self.index+'INPUT ERROR... PROGRAM RESTARTED...')
            sleep(3)
            return Program()
        
    def instagram(self):
        Program.giris(self)
        Program.islem(self, 'takip')
        Program.islem(self, 'takipci')
        Program.islem(self, 'sonuc')

    def giris_bilgi(self):
        try:
            self.username = input(str("Kullanıcı Adı: "))
            self.password = pwinput.pwinput(prompt="Şifre: ", mask="*")

            print('\033c', self.index + '[OK]')
            sleep(1)
            print('\033c', self.index)
            self.program.get('https://www.instagram.com')
            sleep(3)
            self.username_input = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
            self.password_input = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
            self.username_input.send_keys(self.username)
            self.password_input.send_keys(self.password)
            sleep(1)
            self.login_button = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
            self.login_button.click()
            sleep(10)

        except (ZeroDivisionError, ValueError, ElementClickInterceptedException):
            print('\033c', self.index + 'INPUT ERROR... PROGRAM RESTARTED...')
            sleep(3)
            self.program.quit()
            return Program()
        
    def giris(self):
        while True:
            try:
                if self.menu == 1:
                    Program.giris_bilgi(self)
                    self.twocode = pwinput.pwinput(prompt="İki aşamalı doğrulama kodunu giriniz: ", mask="*")
                    print('\033c', self.index + '\n[OK]\n')
                    sleep(1)
                    twofactor_input = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div[1]/div/label/input')
                    twofactor_input.send_keys(self.twocode)
                    self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div[2]/button').click()
                    sleep(10)
                    print('\033c', self.index)
                    print('LOGIN [OK]')
                    sleep(1)
                    break

                elif self.menu == 2:
                    Program.giris_bilgi(self)
                    sleep(5)
                    print('LOGIN [OK]')
                    sleep(1)
                    break

                else:
                    self.program.quit()
                    return Program()

            except NoSuchElementException:
                print('\033c', self.index + 'INPUT ERROR... PROGRAM RESTARTED...')
                sleep(3)
                self.program.quit()
                return Program()
        
    def islem(self, islemkodu):
        while True:
            try:
                self.program.get("https://www.instagram.com/{}".format(self.username))
                sleep(5)
                if islemkodu == 'takip':
                    self.takipedilensayisi = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span').text
                    print('\nTAKİP EDİLEN SAYISI: '+str(self.takipedilensayisi))
                    self.takipedilensayisi = int(self.takipedilensayisi) + 10
                    self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a').click()
                    sleep(2)
                    Program.scroll(self, self.takipedilensayisi)
                    print('\nTAKİP [OK]')
                    sleep(1)
                    for i in range(1, self.takipedilensayisi):
                        islem1 = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{}]/div/div/div/div[2]/div/div/span[1]'.format(i))
                        print(str(i)+' --> '+islem1.text)
                        takiplistesi.append(islem1.text)
                    break

                if islemkodu == 'takipci':
                    self.takipcisayisi = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span').text
                    print('\nTAKİPÇİ SAYISI: '+str(self.takipcisayisi))
                    self.takipcisayisi = int(self.takipcisayisi) + 10
                    self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
                    sleep(2)
                    Program.scroll(self, self.takipcisayisi)
                    print('\nTAKİPÇİ [OK]')
                    sleep(1)
                    for i in range(1, self.takipcisayisi):
                        islem2 = self.program.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{}]/div/div/div/div[2]/div/div/span[1]'.format(i))
                        name=islem2.text.split()
                        print(str(i)+' --> '+name[0])
                        takipcilistesi.append(name[0])
                    break

                if islemkodu == 'sonuc':
                    print('\nTAKİP ETMEYEN [OK]')
                    count = 0
                    xx = list(set(takiplistesi)-set(takipcilistesi))
                    for i in xx:
                        count += 1
                        print(str(count)+" --> " +i+"\n")
                    self.program.quit()
                    break

            except NoSuchElementException:
                break

    def scroll(self, x):
        self.x = x
        js = """
        var s = document.querySelector("._aano");
        s.scrollTo(0, s.scrollHeight);
        var ss = s.scrollHeight;
        ss;
        """
        for a in range(0, self.x//4):
            sleep(0.2)
            self.program.execute_script(js)
    

    def ascii(self):
        self.index = str('''
           __           _____     __    _ 
 ______ __/ /  ___ ____/ _/ /__  / /__ (_)
/ __/ // / _ \/ -_) __/ _/ / _ \/  '_// / 
\__/\_, /_.__/\__/_/ /_//_/\___/_/\_\/_/  
   /___/                                  
'''+"\nunfollowers"+"\t"*4+"v1.1\n"+"="*44+"\n")

system = platform.system()

if system == 'Windows':
    Program(driver=webdriver.Chrome(options=chrome_options))

elif system == 'Linux':
    Program(driver=webdriver.Firefox(options=firefox_options))

else:
    print('İşletim sistemi tanınmadı. Program başlatılamadı.')
