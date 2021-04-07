from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


print("")
print("--- Treasure Referral BOT ---")
print("")

before = int(input("how much is ur storage now?(GB): "))
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

    tmpr_email = "https://getnada.com"

    driver_1.get(treasure)
    driver_2.get(tmpr_email)


    first_names=('John','Andy','Joe','Yancy', 'Christa', 'Merola', 'Henry', 'Allissa', 'Gaultiero', 'Annabela', 'Che', 'Adele', 'Fern', 'Brittan', 'Nicolas', 'Sorcha', 'Kristyn', 'Eugenio', 'Janella', 'Westbrook', 'Moritz', 'Dyann Gwyneth', 'Lucita', 'Catriona', 'Tanney', 'Ellis', 'Diane', 'Lynnet', 'Stephen', 'Wren', 'Vivyanne', 'Jessalyn', 'Orelee', 'Mariele', 'Elwin', 'Joseito', 'Dorris', 'Abbie', 'Therine', 'Dud', 'Karine', 'Howey', 'Arther', 'Borden', 'Rosalie', 'Northrup', 'Todd', 'Mick', 'Evin', 'Burton', 'Patric', 'Henri', 'Cora', 'Darrelle', 'Maren', 'Claiborn', 'Gran', 'Caprice', 'Mélissandre', 'Marie-josée', 'Mélinda', 'Maïwenn', 'Aurélie', 'Maëly', 'Alizée', 'Laurélie', 'Crééz', 'Kallisté', 'Kallisté', 'Mahélie', 'Renée', 'Pò', 'Anaëlle', 'Andréanne', 'Ophélie', 'Nadège', 'Cunégonde', 'Göran', 'Vérane', 'Salomé', 'Rébecca', 'Méline', 'Mélys', 'Bénédicte', 'Maëly', 'Illustrée', 'Mårten' 'Örjan', 'Estève', 'Yóu', 'Ruì', 'Jú', 'Vénus', 'Geneviève', 'Gwenaëlle', 'Océanne', 'Bérangère', 'Maïlis', 'Cléa', 'Illustrée', 'Françoise', 'Océanne', 'Marie-noël', 'Nuó', 'Bénédicte', 'Aí', 'Béatrice', 'Naéva', 'Lucrèce', 'Mélissandre', 'Fèi', 'Annotés', 'Amélie')

    last_names=('Johnson','Smith','Williams''Overil', 'Landre', 'Isacoff', 'Hasluck', 'Janusz', 'Swaddle', 'Zanioletti', 'Schelle', 'Dyers', 'Yitzhakof', 'Spore', 'Kerman', 'Isaq', 'Svanetti', 'Baudi', 'Withrington', 'Wiszniewski', 'Gounot', 'Biggadike', 'Sone', 'Josey', 'Collumbine', 'Croke', 'Smalls', 'Buse', 'Geall', 'Beardsall', 'Auty', 'Jordin', 'Lowless', 'Greenlees', 'Moorey', 'Pady', 'Newton', 'Watts', 'Hurley', 'Jordin', 'Connerry', 'Careswell', 'Stratley', 'Knappitt', 'Prosek', 'Twyford', 'Sherwell', 'Hounihan', 'Cribbins', 'Crookes', 'Kelling', 'Nayer', 'Greatbatch', 'Verdun', 'Treagust', 'Manilow', 'Edgett', 'Negus', 'Ashbe', 'Prene', 'Leipnik', 'Smoote', 'Andreotti', 'Normanvell', 'Glasscott', 'Primak', 'Cartmell', 'Wais', 'Ironmonger', 'Santhouse', 'Hatley', 'Ellyatt', 'Reimer', 'Troop', 'Graves', 'Muston', 'Blizard', 'Bore', 'Wolfers', 'Kelledy', 'Dautry', 'Drayton', 'Culbert', 'Seamans', 'Tissington', 'Kilgannon', 'Urwen', 'Cawston', 'Pimlott', 'Broodes', 'Brame', 'Dallicoat', 'Nelles', 'Frenzl', 'Allabush', 'Hexham', 'Minichi', 'McCreery', 'Jonin', 'Knight', 'Horlick', 'Dencs', 'Grindell', 'Yakebowitch', 'Dorow', 'Keave', 'Flack', 'Cracie', 'Harower', 'Gornar', 'Gillan', 'Gyrgorwicx', 'Seymer', 'Deex', 'Blackston', 'Buffery', 'Begin', 'Glasser', 'Probin', 'Whalebelly', 'Shoppee', 'Simonetto', 'Maleck', 'Kiln', 'Wigan', 'Rakes', 'Foker', 'Goodall', 'Greson')

    passwds = ('4ebE1NdOdJ^_oA2*Usr', 'PvJ^_oA2*m44s', 'Xb*RJ^_oA24tEA', 'Sk*aJ^_oA2aoTmeQNxj', 'jI*dJrJ^_oA2nk', 'Vd*eJ^_oA262kFSwX', 'Rk*J^_oA2SK1ks', 'GU*ZFSJ^_oA2XGF0sea', 'O2*2PJ^_oA2YQySys', 'dl*jI3lJ^_oA2sRKT', 'om*wFsHHaSJC', 'uj*A5J^_oA2a6yV', 'vI*aQJ^_oA2Ub8s', 'Hd*J^_oA2ChPVa', 'Gy*UFLJJ^_oA2SusUVU', 'TT*MskJ^_oA2jOjJ^_oA2k0c', 'J^_oA26k*kJ^_oA2ork', '7H*RDHJ^_oA2v9cAIo', '69*m2blJ^_oA2PuAY', 'nN*J^_oA2HMJ^_oA2XWAzb', 'J2*9SJ^_oA2CQaVSkc1', '60*xVGjQPAJ^_oA2uNl', '4T*J^_oA2mgpivs', '8u*1wJ^_oA29RRmN', 'dC*yJ^_oA2hh3', 'pR*J^_oA2WoL4mlK7G', 'Rk*GkJ^_oA2w21', 'AG*SZoxANt', '97*6J^_oA2knvLq7r', 'uJ*JDk6RJ^_oA2eGYhW', 'Te*1J^_oA2NlXY', 'Uf*alJ^_oA2rHnQ86', 'zA*9jnJ^_oA21F5', '5d*J^_oA2Cb7eW', 'BYJ^_oA2*DEJ^_oA21E', 'aj*J^_oA2oJJ^_oA2271e', 'jN*0QeESJ^_oA2ITP', '1J*MJ^_oA2DKeRxs', 'tE*dbOJ^_oA2bw2U', 'rcJ^_oA2*lJ^_oA2msl', 'Wn*TGJ^_oA2Z4', 'K5*5YAJ^_oA26hx', 'x7*dwJ^_oA29eRxlm', 'H1*MJ^_oA2WRuv5', 'cJ^_oA2g*Ynhc518DU', 'rHJ^_oA2*9w6uJph', 'Op*wBqJ^_oA2o7', 'Fy*mJ^_oA2iJ^_oA2sYk', 'uL*lONXJ^_oA2Rlzypu', 'UcJ^_oA2*XMsyKiyV5d', 'WT*k6yKgmeJ^_oA26L', 'j9*9bJ^_oA2YVQZ2P', 'ijJ^_oA2*iTJ^_oA2mh', 'y1*351YJ^_oA28Vu2lN', 'WNJ^_oA2*cvvJ^_oA2pV', 'l3*QlJ^_oA2XtU4aYKn', 'q7*J^_oA2sTgCMtKAh', '8z*KfhOJ^_oA21U', 'SJ^_oA2A*J^_oA2jWiJ^_oA2Au', 'ew*J^_oA2NvCty4lwG', 'b1*skJ^_oA2jrJ^_oA2Qd', '9R*tJ^_oA2LJ^_oA2CG6', 'mP*J^_oA2BrCD37r1H', 'rS*or6MJ^_oA22bIsV', 'KJ^_oA2*ymuekc', 'FX*86J^_oA20AN7', 'wj*J^_oA2cgV3u', '7gJ^_oA2*GbNOdfvPhw', 'JQ*9cBJ^_oA26', '6h*WdoJ^_oA2WCf8GQS', 'FN*jeqcJ^_oA2xfsy6U', 'PD*0iMJ^_oA2lHvkP', 'YT*8XJ^_oA2rdxYiTXM', '6A*ENmyUJ^_oA2fPb', '7k*8J^_oA2pCCB5Pyu', 'Mg*J^_oA2m9p3e', 'D7*NJ^_oA2duCUlAYNi', 'tb*7dqOJ^_oA2mFFw', '2N*YJ^_oA2STODJP', 'iI*AyBJ^_oA2EHvD', 'rS*Og8PJ^_oA2xi', 'lu*GUJJ^_oA20dy2', 'kcJ^_oA2*OJ^_oA2jKZJ^_oA2J', 'On*J^_oA20RWCwuep', 'oV*J^_oA2eyJ^_oA24J^_oA2V', 'J^_oA2wM*J^_oA2gJJ^_oA2L1', '90*MJ^_oA2iHZLA1', 'nP*M1Q7J^_oA2CKZk', 'YW*FJ^_oA2wQ6eFfFe', 'PX*eJ^_oA2l4oDe', 'qO*mpmJ^_oA2Bia6QRo', 'J^_oA2DS*J^_oA2DJKG4E', 'b21i^&d6*lBO', 'Xplk0g^&k6*Im7M', 'uot^&J6*5fSz', 'F5HXWby^&A6*LCG', 'JHofwPc^&i6*m', 'y8df^&t6*a', 'maT3zug3^&i6*qAo', '2tdGY^&R6*cSWF', '^&K6*1gW4t', 'kg5^&u6*Xc08h', 'ozW5^&06*ElipaM', '1PxELCR^&c6*I9', 'ddHXdOea^&s6*Xqs', '4lcL7^&N6*w0XAUL', '^&46*9VWjBhDxYk', 'SdMCTn^&S6*q', 'fnkt^&V6*wg9', 'EFl5c^&V6*eEYayy', 'NX^&w6*lOHVIFxs', 'PkDUpPw^&S6*bK', '4Hk^&F6*As4tmGC', 'lAeg^&G6*KH', 'FGswH^&o6*1tymt5', 'IJw^&x6*FwwSB2', 'LHkbc3^&s6*Bwg', 'YC^&X6*XfprS6Vt', 'Q9^&96*Evu', '2lhkEtb^&36*t', 'sIIqm8V^&H6*St8I', 'Pr^&b6*ovq', '7gUh^&t6*3', 'LQz^&p6*Qq3rwp', 'qRdh^&96*siR2IW', 'tE^&k6*6mm5', 'DT^&v6*FaygqPZ', 'q28QnOh^&A6*59C', 'kuQ^&w6*jyfX9H', 't9n^&M6*HaGKkce', 'AKq^&s6*lo', 'vYBpy^&A6*RYIr', 'c7gnA^&l6*2HWER', 'Ys^&B6*8JLhDKOh', 'GYum^&K6*i', 'VPC4rN2E^&66*TxQ', 'kkuSOg^&t6*BH', 'L^&L6*agIfITxP2', 'lu2w0m^&Z6*xRRZA', 'GkN^&l6*LT3YDiR')

    group = (random.choice(first_names)+" "+random.choice(last_names))
    pass_grp = random.choice(passwds)

    driver_1.maximize_window()
    driver_2.maximize_window()
    delay(4)
    print("Maximizing Window...")
    delay(2)
    
    print("getting tempr email cred")
    driver_2.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div/p/span[2]').click()
    delay(2)


    driver_1.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(Keys.CONTROL, "v")
    delay(2)
    
        
    driver_1.find_element_by_xpath('//*[@id="signup-button"]').click()
    print("registering...")
    delay(5)
    print("")
    print("patient ya bosquu, waiting for the email")
    delay(20)


    driver_2.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr/td[1]').click()
    delay(5)
    
    driver_2.switch_to.frame("the_message_iframe");
    link = driver_2.find_element_by_xpath('//*[@id="hs_cos_wrapper_module_16158863191553_"]/p[1]/span/strong').text
    print("get the activation code.")
    delay(2)
    driver_2.switch_to.default_content()
    
    print("inputting the code")
    delay(1)
    driver_1.find_element_by_xpath('//*[@id="verify-code-form"]/div[1]/div[1]/input').send_keys(link)
    delay(7)
    
    
    #name
    driver_1.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(group)
    print("some name...")
    delay(7)
    
    #passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-3"]').send_keys(pass_grp)
    print("some password...")
    delay(7)

    #confir-passwd
    driver_1.find_element_by_xpath('//*[@id="mat-input-4"]').send_keys(pass_grp)
    delay(7)

    #uncheckbox
    driver_1.find_element_by_xpath('//*[@id="opt-in-checkbox"]/label/div').click()
    delay(7)

    #continu
    driver_1.find_element_by_xpath('//*[@id="continue-button"]').click()
    print("finishing...")
    delay(7)

    #yes_continue
    driver_1.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-alert-dialog/div[3]/button[2]').click()
    delay(15)

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