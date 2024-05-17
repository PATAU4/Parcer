from typing import Counter
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='/Users/aleksandrtulakov/Documents/ban_y_lisogo/chromedriver/chromedriver')

lst_text_economic = []
lst_text_political = []

def get_economic():
    url = 'https://news.mail.ru/economics/'
    try:
        driver.get( url = url ) 
        
        for click in range(33):
            button_click = driver.find_element( By.XPATH, "/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[4]/div/div/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 450):
            if number_of_tag == 298 or number_of_tag == 299 or number_of_tag == 300 or number_of_tag == 416 or number_of_tag == 439:
                print("SKIP EMPTY DATA")
                continue
            find_tag_by_xpath  = driver.find_element( By.XPATH, f'/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[4]/div/div/div[1]/div[{number_of_tag}]/span[2]/span')
            lst_text_economic.append(find_tag_by_xpath.text)
        print(len(lst_text_economic))
        print(lst_text_economic)
        
    except Exception as Ex:
        print(Ex)

def politic():
    url = "https://news.mail.ru/politics/"
    try:
        driver.get( url = url ) 
        
        for click in range(33):
            button_click = driver.find_element( By.XPATH, "/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 450):
            if number_of_tag == 442:
                print("SKIP EMPTY DATA")
                continue
            find_tag_by_xpath  = driver.find_element( By.XPATH, f'/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_political.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_political))
        print(lst_text_political)                                             
        
    except Exception as Ex:
        print(Ex)
    
    
# politic()
    
    
    
lst_text_social = []
    
def get_social():
    url = 'https://news.mail.ru/society/'
    try:
        driver.get( url = url ) 
        
        for click in range(33):
            button_click = driver.find_element( By.XPATH, "/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 450):
            if number_of_tag == 161 or number_of_tag == 176 or number_of_tag == 276 or number_of_tag == 348 or number_of_tag == 421 or number_of_tag == 438:
                print("SKIP EMPTY DATA")
                continue
            find_tag_by_xpath  = driver.find_element( By.XPATH, f'/html/body/div[5]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_social.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_social))
        print(lst_text_social)                                             
        
    except Exception as Ex:
        print(Ex)
    
    
# get_social()
    
    
    
lst_text_weather = []
    
def get_sience():
    url = 'https://sience.mail.ru/news/'
    try:
        driver.get( url = url ) 
        
        for click in range(33):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div[1]/div[3]/div/div/div/div/div/div/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 450):
            if number_of_tag == 441:
                print("SKIP EMPTY DATA")
                continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_weather.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_weather))
        print(lst_text_weather)                                             
        
    except Exception as Ex:
        print(Ex)
    
# get_sience()
    
    
    
lst_text_sports = []
def get_footbal_news():
    url = 'https://sportmail.ru/football-foreign/'
    try:
        driver.get( url = url ) 
        
        for click in range(6):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 90):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_sports.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_sports))                                       
        
    except Exception as Ex:
        print(Ex)
        
def get_hockey_news():
    url = 'https://sportmail.ru/hockey-khl/'
    try:
        driver.get( url = url ) 
        
        for click in range(6):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 90):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_sports.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_sports))                                       
        
    except Exception as Ex:
        print(Ex)       
def get_figure_skating_news():
    url = 'https://sportmail.ru/figure-skating/'
    try:
        driver.get( url = url ) 
        
        for click in range(6):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 90):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_sports.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_sports))                                       
        
    except Exception as Ex:
        print(Ex)      
def get_biathlon_news():
    url = 'https://sportmail.ru/biathlon/'
    try:
        driver.get( url = url ) 
        
        for click in range(6):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 90):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_sports.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_sports))                                       
        
    except Exception as Ex:
        print(Ex)
def get_mma_news():
    url = 'https://sportmail.ru/mma/'
    try:
        driver.get( url = url ) 
        
        for click in range(6):
            button_click = driver.find_element( By.XPATH, "/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/button/span")
            button_click.click()
            time.sleep(1)
        
        
        for number_of_tag in range(2, 90):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[7]/div[2]/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div[{number_of_tag}]/span[2]/span' )
            lst_text_sports.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_sports))                                       
        
    except Exception as Ex:
        print(Ex)
   
   




lst_text_culture = []
def get_cultural_news():
    url = 'https://news.mail.ru/landing/russian_culture/'
    try:
        driver.get( url = url ) 
        
        for click in range(5):
            button_click = driver.find_element( By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[3]/button")
            button_click.click()
            time.sleep(5)
                                                        
        
        for number_of_tag in range(1, 108):
            # if number_of_tag == 441:
            #     print("SKIP EMPTY DATA")
            #     continue
            find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[{number_of_tag}]/div/div/div/a' )
            lst_text_culture.append(find_tag_by_xpath.text)                          
                                
        
        print(len(lst_text_culture))                                       
        
        
        
    except Exception as Ex:
        print(Ex)



lst_text_culture_2 = []
def get_cultural_news_2():
    for number_of_page in range(2,24):
        print(number_of_page)
        url = f'https://www.culture.ru/news?sort=-publishDate&page={number_of_page}&limit=24'
        try:
            driver.get( url = url )  
            
            for number_of_tag in range(1, 25):
                find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[3]/main/div/article/div[4]/div/section/div[2]/div/div[{number_of_tag}]/div/div[2]/div[1]/div/div/div[1]/div/a' )
                lst_text_culture_2.append(find_tag_by_xpath.text)        
                
            for number_of_tag in range(1, 25):
                find_tag_by_xpath = driver.find_element( By.XPATH, f'/html/body/div[5]/main/div/article/div[4]/div/section/div[2]/div/div[{number_of_tag}]/div/div[2]/div[1]/div/div/div[1]/div/a' )
                lst_text_culture_2.append(find_tag_by_xpath.text)    
            
            
        except Exception as Ex:
            print(Ex)
      
        
        
                
# get_footbal_news()    
# get_hockey_news()
# get_figure_skating_news()
# get_biathlon_news()
# get_mma_news()
# print(len(lst_text_sports))     
# print(lst_text_sports)  
# get_cultural_news_2()















# print(lst_text_sports) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # find_sign_in.click()
    # time.sleep(1)
    # for x in find_sign_in:
    #     print (x.text)
    # data_input1  = driver.find_element_by_tag_name('input')
    # choose1  = driver.find_element( By.XPATH,'/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[1]/div/div[2]/input')
    # choose1.send_keys( name )
    # time.sleep(1)
    # choose2  = driver.find_element( By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input' )
    # choose2.send_keys( passo )
    # time.sleep(1)
    # button = driver.find_element( By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div' )
    # button.click()
    # time.sleep(25)
    # driver.get( url = url_channel ) 
    # time.sleep(1)
    # for i in range(5):
    #     time.sleep(5)
    #     if counter == 0:
    #         data_input1 = driver.find_element_by_tag_name('textarea')
    #         # choose  = driver.find_element( By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div/textarea' )
    #         data_input1.send_keys( 'Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad' + Keys.ENTER )
    #         time.sleep(7)
    #         counter += 1
    #     else:
    #         data_input0  = driver.find_element_by_tag_name('input')
    #         data_input0.click()
    #         data_input1 = driver.find_element_by_tag_name('textarea')
    #         data_input1.send_keys( 'Basedge' + Keys.ENTER )
    #         time.sleep(7)