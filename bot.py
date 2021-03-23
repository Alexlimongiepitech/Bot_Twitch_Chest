from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
# ALED

class twitchBot():
    def __init__(self, username, password):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome("chromedriver")
        self.browser.set_window_size(930, 862)
        self.username = username
        self.password = password
        self.url = "https://www.twitch.tv/channel_you_want_bot"
        self.list_message_in_chat = open("message.txt", "r").readlines()
        print(len(self.list_message_in_chat))
        # for line in self.list_message_in_chat:
        #     print(line)

    def bot(self):
        print("go to twitch")
        self.browser.get('https://www.twitch.tv/')
        time.sleep(5)
        print("sleep(5)")

        print("click on button sig_in")
        self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button')[0].click()
        print("sleep(5)")
        time.sleep(5)

        username = self.browser.find_elements_by_xpath('//*[@id="login-username"]')[0]
        password = self.browser.find_elements_by_xpath('//*[@id="password-input"]')[0]

        print("put username")
        username.send_keys(self.username)
        print("put password")
        password.send_keys(self.password)
        print("sleep(2)")
        time.sleep(2)
        print("click on button connected")
        self.browser.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button')[0].click()
        print("put code")
        print("sleep(50)")
        time.sleep(50)
        try:
            # print("in try")
            self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/button')[0].click()
            print("cookie band accept")
        except NoSuchElementException:
            print("cookie band not found")
        print("sleep(5)")
        time.sleep(5)

        self.browser.get(self.url)
        print("go to channel")
        print("sleep(10)")
        time.sleep(10)

        #   print("send space on player")
        #   # suivie = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[1]/div[1]/div/div[1]/div[1]/a/div/div[1]/div[2]')
        #   # action = webdriver.common.action_chains.ActionChains(self.browser)
        #   # action.move_to_element_with_offset(suivie, 0, 397)
        #   # action.click()
        #   # action.perform()
        #   self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]/div[1]/button')[0].send_keys(Keys.SPACE)
        #   print("sleep(10)")
        #   time.sleep(10)
        #   print("click for studio mode")
        #   self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[7]/div/div/div[2]/div[2]/div[3]')[0].click()
        #   print("sleep(10)")
        #   time.sleep(10)
        #   print("send space on player")
        #   self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[7]/div/div/div[2]/div[1]/div[1]/button')[0].send_keys(Keys.SPACE)
        #   # self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/div/div/button/figure/svg')[0].click()

        while (1):
            if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[3]/div')) == 0):
                print("Not in live, retry in 1h")
                time.sleep(3600)
            try:
                # print("in try")
                # print("sleep(20)")
                if (self.browser.current_url != self.url):
                    self.browser.get(self.url)                    
                time.sleep(50)
                randNum = random.randint(0, 10)
                # randNum = 0
                print(randNum)
                if (randNum == 0):
                    print("play / pause")
                    second_click = False
                    action = webdriver.common.action_chains.ActionChains(self.browser)
                    lecteur_video = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/video')[0]
                    for i in range(1000):
                        # print("in for : ", i)
                        # print("button central", self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/button'))
                        # /html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/div/div/button
                        # print("button bas", self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/button'))
                        button_pause_bas = '/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/button'
                        button_pause_bas_bis = '/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]/div[1]/button'
                        button_pause_central = '/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/button'
                        button_pause_central_bis = '/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/div/div/button'
                        # time.sleep(2)
                        # print(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/button'))
                        if (len(self.browser.find_elements_by_xpath(button_pause_bas)) > 0 and second_click == False): # click sur le button pour pause
                            second_click = True
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_bas)[0].send_keys(Keys.SPACE)
                            print("pause : ", bool(second_click))
                        if (len(self.browser.find_elements_by_xpath(button_pause_bas_bis)) > 0 and second_click == False): # click sur le button pour pause bis
                            second_click = True
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_bas_bis)[0].send_keys(Keys.SPACE)
                            print("pause : ", bool(second_click))
                        if (len(self.browser.find_elements_by_xpath(button_pause_central)) > 0 and second_click == True): # click sur le button pour unpause
                            second_click = False
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_central)[0].send_keys(Keys.SPACE)
                            print("play : ", bool(second_click))
                            break
                        if (len(self.browser.find_elements_by_xpath(button_pause_central_bis)) > 0 and second_click == True): # click sur le button pour unpause bis
                            second_click = False
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_central_bis)[0].send_keys(Keys.SPACE)
                            print("play : ", bool(second_click))
                            break
                        if (len(self.browser.find_elements_by_xpath(button_pause_central)) > 0 and second_click == False): # si deja en pause 
                            second_click = False
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_central)[0].send_keys(Keys.SPACE)
                            print("play : ", bool(second_click))
                            break
                        if (len(self.browser.find_elements_by_xpath(button_pause_central_bis)) > 0 and second_click == False): # si deja en pause bis
                            second_click = False
                            action.move_to_element(lecteur_video).perform()
                            self.browser.find_elements_by_xpath(button_pause_central_bis)[0].send_keys(Keys.SPACE)
                            print("play : ", bool(second_click))
                            break
                if (randNum == 1):
                    if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div/div/button')) > 0): # follow button
                        follow_button = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div/div/button')[0]
                        # if you follow chanel
                        if (follow_button.get_attribute("class") == 'tw-align-items-center tw-align-middle tw-border-bottom-left-radius-medium tw-border-bottom-right-radius-medium tw-border-top-left-radius-medium tw-border-top-right-radius-medium tw-core-button tw-core-button--primary tw-full-width tw-inline-flex tw-interactive tw-justify-content-center tw-overflow-hidden tw-relative'):
                            follow_button.click()
                            time.sleep(10)
                    if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]/div/div/textarea')) > 0):
                        print("textarea")
                        tchat = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]/div/div/textarea')[0]
                    if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[6]/div[2]/div[1]/div/div[2]/div/div/textarea')) > 0):
                        print("textarea bis")
                        tchat = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[6]/div[2]/div[1]/div/div[2]/div/div/textarea')[0]
                    elif (len(self.browser.find_elements_by_xpath('html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]/div/div')) > 0):
                        print("chat-input__textarea")
                        tchat = self.browser.find_elements_by_xpath('html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]/div/div')[0]
                    elif (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]')) > 0):
                        print("tw-block tw-border-radius-large tw-pd-0")
                        tchat = self.browser.find_elements_by_xpath('html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[1]/div/div[2]')[0]
                    # print(tchat)
                    tchat.click()
                    if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[6]/div[1]/div/div[2]/div[2]/button')) > 0):
                        # bis
                        self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[6]/div[1]/div/div[2]/div[2]/button')[0].click()
                        time.sleep(2)
                    if (len(self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[1]/div/div[2]/div[2]/button')) > 0):
                        self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[1]/div/div[2]/div[2]/button')[0].click()
                        time.sleep(2)
                    nb_for_rand_message = random.randint(0, len(self.list_message_in_chat))
                    tchat.send_keys(self.list_message_in_chat[nb_for_rand_message])
                    print("message send in chat : ", self.list_message_in_chat[nb_for_rand_message])
                    tchat.send_keys(Keys.ENTER)
                    time.sleep(5)
                    if (len(self.browser.find_elements_by_class_name('chat-line__status')) > 0):
                        for nb_message in range(0, len(self.browser.find_elements_by_class_name('chat-line__status'))):
                            print(len(self.browser.find_elements_by_class_name('chat-line__status')))
                            status_message = self.browser.find_elements_by_class_name('chat-line__status')[nb_message].text
                            print(status_message)
                            # This room is in 10 minutes followers-only mode. Follow esl_csgo_fr to join the community!
                            if ("This room is in " in status_message):
                                if (" minutes followers-only mode. Follow " in status_message):
                                    if (" to join the community!" in status_message):
                                        # print("---------")
                                        # print(status_message.split(" ")[4])
                                        # print(int(status_message.split(" ")[4]))
                                        print("status message : ", status_message)
                                        time.sleep(int(status_message.split(" ")[4]))
                            break
                if (randNum == 7 or randNum == 8 or randNum == 9 or randNum == 10):
                    button_coffre = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button')
                    button_coffre_bis = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button')
                    if (len(button_coffre) > 0):
                        time.sleep(random.randint(0, 50))
                        print("click on coffre")
                        button_coffre[0].click()
                    if (len(button_coffre_bis) > 0):
                        time.sleep(random.randint(0, 50))
                        print("click on coffre")
                        button_coffre_bis[0].click()
            except NoSuchElementException:
                print("in except")
                continue

        # while (1):
        #     try:
        #         print("in try") # probleme trouve pas le coffre
        #         # button_coffre = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[7]/div/div/div[2]/div[2]/div[3]')
        #         # masque_button = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/button')
        #         # print(masque_button)
        #         # para_button = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/button')
        #         # print(para_button)
        #         button_coffre = self.browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button')
        #         # action = webdriver.common.action_chains.ActionChains(self.browser)
        #         # action.move_to_element_with_offset(button_coffre, 168, 39)
        #         # print("sleep(20)")
        #         time.sleep(20)
        #         randNum = random.randint(0, 3)
        #         print(randNum)
        #         if (randNum == 3):
        #             if (len(button_coffre) > 0):
        #                 button_coffre[0].click()
        #             # action.click()
        #             # action.perform()
        #         # print(button_coffre)
        #         # button_coffre.click()
        #     except NoSuchElementException:
        #         print("in except")
        #         continue
                
        # if (self.browser.find_elements_by_xpath('/div/button/span')[0].size() != 0)
        # # button_coffre = self.browser.find_elements_by_xpath('/div/button/span')[0]
        # print("put button_coffre in var")
        # while (1):
        #     while (button_coffre.size() != 0):
        #         time.sleep(100)
        #         if (random.randint(0, 3) == 2):
        #             button_coffre.click()

if __name__ == "__main__":
    twitchBot("your_username", "your_password").bot()
    # driver = webdriver.Chrome("chromedriver")
    # driver.get("http://www.google.com")
    # time.sleep(2)
    # el=driver.find_elements_by_xpath('//*[@id="gbw"]/div[2]/div/div[1]/div[1]')[0]

    # action = webdriver.common.action_chains.ActionChains(driver)
    # action.move_to_element_with_offset(el, 50, 50)
    # action.click()
    # action.perform()