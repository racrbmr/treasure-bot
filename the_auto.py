from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


print("")
print("--- Treasure Referral BOT ---")
print("")

before = int(input("berapakah storage kamu sekarang?(GB): "))
how_many = int(input("ingin nambah berapa kali?: "))

if how_many <= 0:
    print("Gak bisa, Minimal harus 1x")
    exit()
else:
    pass

print("")
print("bot ini akan mengulang proses selama", how_many, "kali atau penambahan storage", how_many * 10, "GB")
print("---- sangat disarankan tidak lebih dari 5x -----")
time.sleep(3)

after = how_many * 10


def auto():
    delay = time.sleep
    treasure = input("Input link referral treasure kamu: ")
    driver_1 = webdriver.Chrome(ChromeDriverManager().install())
    driver_2 = webdriver.Chrome(ChromeDriverManager().install())
    print("")
    print("sekarang chill aja, gausa gegabah otak atik. ok?")
    print("estimasi 1x proses = 5 menit")
    print("")
    delay(5)

    tmpr_email = "https://tempr.email"

    driver_1.get(treasure)
    driver_2.get(tmpr_email)


    first_names=('John','Andy','Joe','Yancy', 'Christa', 'Merola', 'Henry', 'Allissa', 'Gaultiero', 'Annabela', 'Che', 'Adele', 'Fern', 'Brittan', 'Nicolas', 'Sorcha', 'Kristyn', 'Eugenio', 'Janella', 'Westbrook', 'Moritz', 'Dyann Gwyneth', 'Lucita', 'Catriona', 'Tanney', 'Ellis', 'Diane', 'Lynnet', 'Stephen', 'Wren', 'Vivyanne', 'Jessalyn', 'Orelee', 'Mariele', 'Elwin', 'Joseito', 'Dorris', 'Abbie', 'Therine', 'Dud', 'Karine', 'Howey', 'Arther', 'Borden', 'Rosalie', 'Northrup', 'Todd', 'Mick', 'Evin', 'Burton', 'Patric', 'Henri', 'Cora', 'Darrelle', 'Maren', 'Claiborn', 'Gran', 'Caprice')

    last_names=('Johnson','Smith','Williams''Overil', 'Landre', 'Isacoff', 'Hasluck', 'Janusz', 'Swaddle', 'Zanioletti', 'Schelle', 'Dyers', 'Yitzhakof', 'Spore', 'Kerman', 'Isaq', 'Svanetti', 'Baudi', 'Withrington', 'Wiszniewski', 'Gounot', 'Biggadike', 'Sone', 'Josey', 'Collumbine', 'Croke', 'Smalls', 'Buse', 'Geall', 'Beardsall', 'Auty', 'Jordin', 'Lowless', 'Greenlees', 'Moorey', 'Pady', 'Newton', 'Watts', 'Hurley', 'Jordin', 'Connerry', 'Careswell', 'Stratley', 'Knappitt', 'Prosek', 'Twyford', 'Sherwell', 'Hounihan', 'Cribbins', 'Crookes', 'Kelling', 'Nayer', 'Greatbatch', 'Verdun', 'Treagust', 'Manilow', 'Edgett', 'Negus', 'Ashbe', 'Prene', 'Leipnik', 'Smoote', 'Andreotti', 'Normanvell', 'Glasscott', 'Primak', 'Cartmell', 'Wais', 'Ironmonger', 'Santhouse', 'Hatley', 'Ellyatt', 'Reimer', 'Troop', 'Graves', 'Muston', 'Blizard', 'Bore', 'Wolfers', 'Kelledy', 'Dautry')

    passwds = ('4ebE1NdOdJ^_oA2*Usr', 'PvJ^_oA2*m44s', 'Xb*RJ^_oA24tEA', 'Sk*aJ^_oA2aoTmeQNxj', 'jI*dJrJ^_oA2nk', 'Vd*eJ^_oA262kFSwX', 'Rk*J^_oA2SK1ks', 'GU*ZFSJ^_oA2XGF0sea', 'O2*2PJ^_oA2YQySys', 'dl*jI3lJ^_oA2sRKT', 'om*wFsHHaSJC', 'uj*A5J^_oA2a6yV', 'vI*aQJ^_oA2Ub8s', 'Hd*J^_oA2ChPVa', 'Gy*UFLJJ^_oA2SusUVU', 'TT*MskJ^_oA2jOjJ^_oA2k0c', 'J^_oA26k*kJ^_oA2ork', '7H*RDHJ^_oA2v9cAIo', '69*m2blJ^_oA2PuAY', 'nN*J^_oA2HMJ^_oA2XWAzb', 'J2*9SJ^_oA2CQaVSkc1', '60*xVGjQPAJ^_oA2uNl', '4T*J^_oA2mgpivs', '8u*1wJ^_oA29RRmN', 'dC*yJ^_oA2hh3', 'pR*J^_oA2WoL4mlK7G', 'Rk*GkJ^_oA2w21', 'AG*SZoxANt', '97*6J^_oA2knvLq7r', 'uJ*JDk6RJ^_oA2eGYhW', 'Te*1J^_oA2NlXY', 'Uf*alJ^_oA2rHnQ86', 'zA*9jnJ^_oA21F5', '5d*J^_oA2Cb7eW', 'BYJ^_oA2*DEJ^_oA21E', 'aj*J^_oA2oJJ^_oA2271e', 'jN*0QeESJ^_oA2ITP', '1J*MJ^_oA2DKeRxs', 'tE*dbOJ^_oA2bw2U', 'rcJ^_oA2*lJ^_oA2msl', 'Wn*TGJ^_oA2Z4', 'K5*5YAJ^_oA26hx', 'x7*dwJ^_oA29eRxlm', 'H1*MJ^_oA2WRuv5', 'cJ^_oA2g*Ynhc518DU', 'rHJ^_oA2*9w6uJph', 'Op*wBqJ^_oA2o7', 'Fy*mJ^_oA2iJ^_oA2sYk', 'uL*lONXJ^_oA2Rlzypu', 'UcJ^_oA2*XMsyKiyV5d', 'WT*k6yKgmeJ^_oA26L', 'j9*9bJ^_oA2YVQZ2P', 'ijJ^_oA2*iTJ^_oA2mh', 'y1*351YJ^_oA28Vu2lN', 'WNJ^_oA2*cvvJ^_oA2pV', 'l3*QlJ^_oA2XtU4aYKn', 'q7*J^_oA2sTgCMtKAh', '8z*KfhOJ^_oA21U', 'SJ^_oA2A*J^_oA2jWiJ^_oA2Au', 'ew*J^_oA2NvCty4lwG', 'b1*skJ^_oA2jrJ^_oA2Qd', '9R*tJ^_oA2LJ^_oA2CG6', 'mP*J^_oA2BrCD37r1H', 'rS*or6MJ^_oA22bIsV', 'KJ^_oA2*ymuekc', 'FX*86J^_oA20AN7', 'wj*J^_oA2cgV3u', '7gJ^_oA2*GbNOdfvPhw', 'JQ*9cBJ^_oA26', '6h*WdoJ^_oA2WCf8GQS', 'FN*jeqcJ^_oA2xfsy6U', 'PD*0iMJ^_oA2lHvkP', 'YT*8XJ^_oA2rdxYiTXM', '6A*ENmyUJ^_oA2fPb', '7k*8J^_oA2pCCB5Pyu', 'Mg*J^_oA2m9p3e', 'D7*NJ^_oA2duCUlAYNi', 'tb*7dqOJ^_oA2mFFw', '2N*YJ^_oA2STODJP', 'iI*AyBJ^_oA2EHvD', 'rS*Og8PJ^_oA2xi', 'lu*GUJJ^_oA20dy2', 'kcJ^_oA2*OJ^_oA2jKZJ^_oA2J', 'On*J^_oA20RWCwuep', 'oV*J^_oA2eyJ^_oA24J^_oA2V', 'J^_oA2wM*J^_oA2gJJ^_oA2L1', '90*MJ^_oA2iHZLA1', 'nP*M1Q7J^_oA2CKZk', 'YW*FJ^_oA2wQ6eFfFe', 'PX*eJ^_oA2l4oDe', 'qO*mpmJ^_oA2Bia6QRo', 'J^_oA2DS*J^_oA2DJKG4E')

    group = (random.choice(first_names)+" "+random.choice(last_names))
    pass_grp = random.choice(passwds)

    driver_1.maximize_window()
    driver_2.maximize_window()
    delay(4)

    generate_email = driver_2.find_element_by_xpath('//*[@id="Login"]/div/form/table/tbody/tr[1]/td[2]/a/img').click()
    delay(1)
    go = driver_2.find_element_by_xpath('//*[@id="Login"]/div/form/table/tbody/tr[4]/td[2]/input').click()
    delay(4)
    copy_email = driver_2.find_element_by_xpath('//*[@id="InboxWrapper"]/div[1]/strong[1]').text
    delay(2)


    driver_1.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(copy_email)
    delay(2)

    driver_1.find_element_by_xpath('//*[@id="signup-button"]').click()
    print("")
    print("sabar ya bosquu, lagi nunggu email masuk")
    delay(150)

    

    driver_2.find_element_by_xpath('//*[@id="MenuInbox"]/div/nav/ul/li[1]/a').click()
    delay(5)
    

    driver_2.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[2]/form/div[2]/div/div[4]/a').click()
    delay(7)

    driver_2.find_element_by_xpath('//*[@id="ContentWithMenu"]/div/div/a[1]').click()
    delay(7)

    link = driver_2.find_element_by_xpath('//*[@id="MessageContent"]/div/a').text
    delay(6)


    driver_1.get(link)

    #name
    driver_1.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(group)
    delay(7)

    #passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(pass_grp)
    delay(7)

    #confir-passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-3"]').send_keys(pass_grp)
    delay(7)

    #uncheckbox
    driver_1.find_element_by_xpath('//*[@id="opt-in-checkbox"]/label/div').click()
    delay(7)

    #continu
    driver_1.find_element_by_xpath('//*[@id="continue-button"]').click()
    delay(7)

    #yes_continue
    driver_1.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/app-alert-dialog/div[3]/button[2]').click()
    delay(15)

    #finish
    driver_1.find_element_by_xpath('//*[@id="finish-button"]').click()
    print("")
    print("iya ini sudah selesai, lagi nungguin loading kalo internet lu kek siput")
    delay(25)

    driver_1.quit()
    driver_2.quit()
    #selesai sampe sini


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
print("COMPLETED BOSQU")
print("")
print(" by: racrbmr")
print(" github.com/racrbmr")
print("")