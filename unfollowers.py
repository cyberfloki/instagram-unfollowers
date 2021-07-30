from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from colorama import init, Fore, Back, Style
import time
from time import sleep
import getpass
init(autoreset=True)

followinglist = list()
followerslist = list()

class Program:
    def __init__(self):
        try:
            print('\033c')
            options = Options()
            options.headless = True
            self.program = webdriver.Firefox(options=options)
            Program.ascii(self)
            print(self.index)
            self.menu = int(input("[1] Two Factor Authentication\n[2] No Two Factor Authentication"+Fore.GREEN+"(stable)\n\n"+Fore.WHITE+"INPUT : "))
            print('\033c',self.index)
            Program.instagram(self)
        except (ZeroDivisionError,ValueError):
            print('\033c'+self.index+Fore.RED+"INPUT ERROR... PROGRAM RESTARTED..."+Fore.WHITE)
            time.sleep(3)
            return Program()       

    def instagram(self):
        Program.login(self)
        Program.Following(self)
        Program.Followers(self)
        Program.x(self)
        
    def scroll(self,x):
        self.x = x
        js = """
        s = document.querySelector(".isgrP");
        s.scrollTo(0,s.scrollHeight);
        var ss = s.scrollHeight;
        return ss;
        """

        ss = self.program.execute_script(js)
        for a in range(0,self.x//2):
            time.sleep(0.3)
            end = ss
            ss = self.program.execute_script(js)

    def loginInfo(self):
        try:
            self.username = input(str("Username : "))
            self.password = getpass.getpass("Password : ")
            print('\033c',self.index)
            print(Fore.GREEN+"[OK]"+Fore.WHITE)
            time.sleep(1)
            print('\033c',self.index)
            self.program.get("https://www.instagram.com")
            sleep(2.5)
            self.username_input = self.program.find_element_by_css_selector("input[name='username']")
            self.password_input = self.program.find_element_by_css_selector("input[name='password']")
            self.username_input.send_keys(self.username)
            self.password_input.send_keys(self.password)
            self.login_button = self.program.find_element_by_xpath("//button[@type='submit']")
            self.login_button.click()
            sleep(10)

        except (ZeroDivisionError,ValueError,ElementClickInterceptedException):
            print('\033c',self.index+Fore.RED+"INPUT ERROR... PROGRAM RESTARTED..."+Fore.WHITE)
            time.sleep(3)
            self.program.quit()
            return Program()

    def login(self):
        while True:
            try:        
                if self.menu == 1:
                    Program.loginInfo(self)
                    self.twocode = input(str("TWO FACTOR CODE : "))
                    print('\033c'+self.index+Fore.GREEN+"\n[OK]\n"+Fore.WHITE)
                    time.sleep(1)
                    twofactor_input = self.program.find_element_by_css_selector("input[name='verificationCode']")
                    twofactor_input.send_keys(self.twocode)
                    self.program.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button').click()
                    sleep(10)
                    self.program.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                    sleep(5)
                    print('\033c',self.index)
                    print("LOGIN"+Fore.GREEN+"  [OK]"+Fore.WHITE)
                    time.sleep(1)
                    break
                    

                elif self.menu == 2:
                    Program.loginInfo(self)
                    self.program.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                    sleep(5)
                    print("LOGIN"+Fore.GREEN+"  [OK]"+Fore.WHITE)
                    time.sleep(1)
                    break

                else:
                    print('\033c',self.index+Fore.RED+"INPUT ERROR... PROGRAM RESTARTED..."+Fore.WHITE)
                    time.sleep(3)
                    self.program.quit()
                    return Program()

            except NoSuchElementException:
                print('\033c',self.index+Fore.RED+"ERROR PROGRAM RESTARTED..."+Fore.WHITE)
                time.sleep(3)
                self.program.quit()
                return Program()
            
    def Following(self):
        while True:
            try:
                self.program.get("https://www.instagram.com/%s" % self.username)
                sleep(1)
                self.followingcount = self.program.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
                self.followingcount = int(self.followingcount) + 10
                self.program.find_element_by_xpath('//a[contains(@href, "%s")]' % "following").click()
                time.sleep(1)
                Program.scroll(self,self.followingcount)
                print("\nFOLLOW"+Fore.GREEN+"  [OK]"+Fore.WHITE)

                for i in range(1,self.followingcount):
                    scr1 = self.program.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/ul/div/li[%s]' % i)
                    self.program.execute_script("arguments[0].scrollIntoView();", scr1)
                    text = scr1.text.encode('utf-8').split()
                    followinglist.append(text[0].decode())

            except NoSuchElementException:
                break
    
    def Followers(self):
        while True:
            try:
                self.program.get("https://www.instagram.com/%s" % self.username)
                sleep(1)
                self.followerscount = self.program.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
                self.followerscount = int(self.followerscount) + 10
                self.program.find_element_by_xpath('//a[contains(@href, "%s")]' % "followers").click()
                sleep(1)
                Program.scroll(self,self.followerscount)
                print("\nFOLLOWERS"+Fore.GREEN+"  [OK]"+Fore.WHITE)

                for i in range(1,self.followerscount):
                    scr1 = self.program.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
                    self.program.execute_script("arguments[0].scrollIntoView();", scr1)
                    text = scr1.text.encode('utf-8').split()
                    followerslist.append(text[0].decode())
            
            except NoSuchElementException:
                break

    def x(self):
        print("\nUNFOLLOWERS",Fore.GREEN+" [OK]\n"+Fore.WHITE)
        sleep(2)
        count = 0
        xx = list(set(followinglist)-set(followerslist))
        for i in xx:
            count += 1
            print(Fore.GREEN+str(count)+" --> " +Fore.WHITE+i+"\n")

        self.program.quit()

    def ascii(self):
        self.index = str(Fore.GREEN+'''
           __           _____     __    _ 
 ______ __/ /  ___ ____/ _/ /__  / /__ (_)
/ __/ // / _ \/ -_) __/ _/ / _ \/  '_// / 
\__/\_, /_.__/\__/_/ /_//_/\___/_/\_\/_/  
   /___/                                  
'''+"\nunfollowers"+"\t"*4+"v1.0\n"+"="*44+"\n"+Fore.WHITE)

Program()