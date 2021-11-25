import random
import string
from colorama import Fore
from colorama import Style
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from os import system
system("title "+'KryptoN#2137 AboutYou Account Generator')
print(Fore.RED)
print("---------------------------------------")
print("KryptoN#2137 AboutYou Account Generator")
print("---------------------------------------")
print(Fore.WHITE)

# Make sure chromedriver is in the same folder

def slow_type(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)


global email_list
email_list = []


def work():

    email_min_lenght = int(input('Min email lenght: '))
    email_max_lenght = int(input('Max email lenght: '))
    domain = input('Input your domain: @')
    how_many = int(input('How many accounts do you want: '))
    firstName = input('First name: ')
    lastName = input('Last name: ')

    def answer_1():
        global pass_choice, password_return, password_max_lenght, password_static_return
        answer = input('Static or random password s/r: ').lower()

        if answer == 's':
            pass_choice = 's'
            password_static_return = input('Input password: ')
        elif answer == 'r':
            pass_choice = 'r'
            password_max_lenght = int(input('Max password lenght: '))
        else:
            print(Fore.RED+'Wrong choice!'+Fore.WHITE)
            answer_1()

    answer_1()
    discord_webhook = input('Input webhook or leave blank: ')

    for _ in range(how_many):

        global driver
        PATH = 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

        email_number = random.randint(email_min_lenght, email_max_lenght)
        email = ''.join(random.choice(string.ascii_letters)
                        for x in range(email_number))
        email_return = email + '@'+domain
        email_list.append(email_return)

        if pass_choice == 'r':
            password_number = random.randint(6, password_max_lenght)
            password_return = ''.join(random.choice(
                string.ascii_letters) for x in range(password_number))
        else:
            password_return = password_static_return

        driver.get("https://www.aboutyou.pl/?loginFlow=register")
        start = time.time()
        time.sleep(3)

        cookie = WebDriverWait(driver, 4, 1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[2]"))
        cookie.click()
        try:
            mobile_button = WebDriverWait(driver, 3, 1).until(lambda d: d.find_element_by_xpath(
                "/html/body/main/div[7]/button"))
            mobile_button.click()
        except:
            pass

        register = WebDriverWait(driver, 3, 1).until(
            lambda d: d.find_element_by_xpath("/html/body/main/div[2]/header/div/div[1]/div[3]/ul/li[2]/div/a"))
        register.click()

        first_name = WebDriverWait(driver, 3, 1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/label/input"))
        first_name.clear()
        first_name.send_keys(firstName)
        #slow_type(first_name, firstName)

        last_name = WebDriverWait(driver, 3, 1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/label/input"))
        last_name.clear()
        last_name.send_keys(lastName)
        #slow_type(last_name, lastName)

        email_address = WebDriverWait(driver, 3, 1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div[1]/label/input"))
        email_address.clear()
        email_address.send_keys(email_return)
        #slow_type(email_address, email_return)

        password = WebDriverWait(driver, 3, 1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/label/input"))
        password.clear()
        password.send_keys(password_return)
        #slow_type(password, password_return)

        time.sleep(0.5)
        preferences = WebDriverWait(driver, 3, 0.1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[3]/fieldset/div/label[1]/div"))
        preferences.click()

        time.sleep(0.5)
        newsletter = WebDriverWait(driver, 3, 0.1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/label/span"))
        newsletter.click()

        time.sleep(0.5)
        # Register
        register = WebDriverWait(driver, 3, 0.1).until(lambda d: d.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/form/div[4]/button/span"))
        register.click()
        time.sleep(5)

        end = time.time()
        creating_time = end - start
        creating_time = round(creating_time, 2)

        date = datetime.now()
        currdate = "["+str(date.hour) + ':' + \
            str(date.minute) + ':' + str(date.second) + "]"
        print(Fore.GREEN+currdate+'Account Created!'+Fore.WHITE)

        with open('ay_email_out.txt', 'a') as f:
            f.write(email_return+":"+password_return+'\n')

        current_site_url = driver.current_url

        if discord_webhook != '':
            if current_site_url == 'https://www.aboutyou.pl/?loginFlow=register':

                print(Fore.GREEN+currdate+'Account Created!'+Fore.WHITE)
                # with open('zalando_email_out.txt', 'a') as f:
                #    f.write(email_return + ':'+password_return+'\n')

                webhook = DiscordWebhook(discord_webhook)
                embed = DiscordEmbed(
                    title='Successful Register!', color='39C16C')
                embed.set_footer(
                    text='KryptoN#2137 AboutYou Account Generator')
                embed.set_timestamp()

                embed.add_embed_field(name='🌍Site', value='AboutYou')
                embed.add_embed_field(
                    name='📧Email', value=str('||'+email_return+'||'))
                embed.add_embed_field(name='⏰Time', value=str(creating_time))
                webhook.add_embed(embed)
                response = webhook.execute()
            

        driver.quit()


work()
# Discord:
# KryptoN#2137
