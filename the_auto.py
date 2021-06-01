from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, requests



print("")
print("--- Treasure Referral BOT ---")
print("")

before = int(input("how much is ur total storage now?(GB): "))
print(" 1x process = 10 GB")
how_many = int(input("how many process do u want?: "))

if how_many <= 0:
    print(" Nope, minimum 1x process")
    exit()
else:
    pass

print("")
print("The bot will repeat the process for", how_many, "time(s) or increase in storage of", how_many * 10, "GB")
print("---- it is recommended to not go over 5x -----")
time.sleep(3)

after = how_many * 10
treasure = input("Input ur treasure ref link: ")

def auto():
    delay = time.sleep
    driver_1 = webdriver.Chrome(ChromeDriverManager().install())
    driver_2 = webdriver.Chrome(ChromeDriverManager().install())
    print("")
    print("now get chill, don't u dare push/press anything. ok?")
    print("1x process estimated for 5 minutes")
    print("")
    delay(5)

    tmpr_email = "https://emailfake.com"
    the_api = 'https://api.namefake.com'

    driver_1.get(treasure)
    
    data_gen = requests.get(the_api).json()

    the_name = (data_gen['name'])
    passwds = (data_gen['password'])
    e_u = (data_gen['email_u'])
    e_d = (data_gen['email_d'])
    #uuid for fulfill the requirement of the password length.
    #i got some case the password is less than requirement's length
    uuid = (data_gen['uuid'])

    driver_1.maximize_window()
    driver_2.maximize_window()
    delay(4)
    print("Maximizing Window...")
    delay(2)
    
    print("getting tempr email cred")
    driver_2.get(tmpr_email + '/' + e_u + '@' + e_d)
    delay(4)
    
    driver_2.find_element_by_xpath('//*[@id="copbtn"]').click()
    delay(2)

    driver_1.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(Keys.CONTROL, "v")
    delay(2)
    
    #name
    driver_1.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(the_name)
    print("some name...")
    delay(7)
    
    #passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(passwds + uuid)
    print("some password...")
    delay(7)
    
    #confir-passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-3"]').send_keys(passwds + uuid)
    delay(7)

    #uncheckbox
    driver_1.find_element_by_xpath('//*[@id="opt-in-checkbox"]/label/div').click()
    delay(7)

    #signup
    driver_1.find_element_by_xpath('//*[@id="continue-button"]').click()
    print("finishing...")
    delay(7)

    #yes_continue
    driver_1.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-alert-dialog/div[3]/button[2]').click()
    delay(15)
    print("registering...")
    delay(1)
    print("")
    print("patient ya bosquu, waiting for the email")
    delay(40)

    driver_2.find_element_by_xpath('//*[@id="refresh"]/div').click()
    link = driver_2.find_element_by_xpath('//*[@id="hs_cos_wrapper_module_16158863191553_"]/p[1]/span/strong').text
    delay(7)
    print("get the activation code.")
    
    print("inputting the code")
    delay(2)
    driver_1.find_element_by_xpath('//*[@id="verify-code-form"]/div[1]/div[1]/input').send_keys(link)
    delay(7)
    
    #finish
    driver_1.find_element_by_xpath('//*[@id="finish-button"]').click()
    print("")
    print("COMPLETE! just wait a bit ok, in case ur internet is like a snail")
    delay(15)

    driver_1.quit()
    driver_2.quit()
    #done


if how_many == 1:
    how_many = 0
else:
    pass

for i in range(how_many-1):
    auto()


auto()

print("")
print("Before:", before, "GB of Storage")
print("After:", before + after, "GB of Storage")
print("ENJOY BOSQU")
print("")
print(" by: racrbmr")
print(" github.com/racrbmr")
print("")
