import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_position_url_list(position,location) -> list:
    try:
        global position_url
        position_url=[]
        user_text=position.replace(" ","+")
        url2 = "https://www.indeed.com/"
        # url = "https://www.indeed.com/jobs?q={}&l={}".format(user_text,location)
        driver = webdriver.Chrome()
        driver.get(url2)

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,features='html.parser')

    

        driver.close()
        # print(soup)
        # print(url)
        results = soup.find(class_="jobsearch-Yosegi")
        print(results)
    except Exception as e:
        return {"error":"can't get urls list..."+str(e)}

get_position_url_list("machine learning","ahmedabad")