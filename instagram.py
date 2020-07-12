from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
# Login with ID and password
    def login(self):
        self.browser.get('https://instagram.com/')
        sleep(5)
        # self.browser.find_element_by_partial_link_text('Log In').click()
        # sleep(5)
        self.browser.find_element_by_name('username').send_keys(self.username)
        sleep(3)
        self.browser.find_element_by_name('password').send_keys(self.password)
        sleep(3)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()#Login button
        sleep(7)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()#not now
        sleep(5)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()#not noow
        sleep(3)

    def get_following_list(self,user):
        
        self.goto_user(user)
        sleep(3)
        limit=int(self.browser.find_elements_by_class_name('g47SY')[2].text)//5
        sleep(1)
        self.browser.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(2)
        fBody  = self.browser.find_element_by_xpath("//div[@class='isgrP']")
        s=0
        while s<limit: # scroll 5 times
            
            sleep(1)
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            s+=1
        following =self.browser.find_elements_by_class_name('FPmhX')
        lst=[l.text for l in following]
        print('You are following : ',len(lst))
        return lst

    #go to the profile of the user    
    def goto_user(self,user):
        self.browser.get('https://instagram.com/'+ user)

# get the list of 
    def get_followers_list(self,user):
        
        self.goto_user(user)
        sleep(3)
        limit=int(self.browser.find_elements_by_class_name('g47SY')[1].text)//5
        sleep(1)
        self.browser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        sleep(3)
        fBody  = self.browser.find_element_by_xpath("//div[@class='isgrP']")
        s=0
        while s<limit: # scroll 5 times
            
            sleep(1)
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            
            s+=1
        following =self.browser.find_elements_by_class_name('FPmhX')
        lst=[l.text for l in following]
        print('Your Followers : ',len(lst))
        return lst


       

bot = Instagram('#USERNAME','#PASSWORD')
bot.login()
followers=bot.get_followers_list('USERNAME WHOSE FOLLOWERS LIST YOU WANT')
following=bot.get_following_list('USERNAME WHOLE FOLLOWING LIST YOU WANT')

dhokebazz=[person for person in following if person not in followers]
bot.browser.close()
print('the dhokebazz no:',len(dhokebazz))
print(dhokebazz)