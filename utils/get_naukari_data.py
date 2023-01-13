
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
# import jsonify

global position_url

def get_position_url_list(position,location) -> list:
    try:
        global position_url
        position_url=[]
        user_text=position.replace(" ","-")+"-jobs-in-"+location
        url = "https://www.naukri.com/"+user_text
        
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,features='html.parser')

    

        driver.close()
        results = soup.find(class_="list")
        # print(results)

        job_elems = results.find_all('article',class_='jobTuple')
        for i in job_elems:
            position_url.append(i.div.div.find("a",class_="title ellipsis")['href'])
        
        return position_url
    except Exception as e:
        return {"error":str(e)},500


def get_position_details(position_url) -> dict:
    try:
        position_name=''
        position_company=''
        position_exp=''
        position_salary=''
        position_location=''
        position_mode=''

        driver = webdriver.Chrome()

        driver.get(position_url)

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,features='html.parser')
    
        results = soup.find(class_="leftSec")

        job_elems = results.find_all('section',class_='jd-header')
        # print(job_elems)
        # print(len(job_elems))
        for i in job_elems:
            try:
                position_name=i.div.h1.text
            except:
                position_name='Not Available'
            finally:
                try:
                    position_company=i.div.div.a.text
                except:
                    position_company='Not Available'
                finally:
                    try:
                        position_exp=i.find("div",class_="exp").text
                    except:
                        position_exp='Not Available'
                    
                    finally:
                        try:
                            position_salary=i.find("div",class_="salary").text
                        except:
                            position_salary='Not Available'
                        finally:
                            try:

                                position_location=i.find("span",class_="location").text
                            except:
                                position_location='Not Available'
                            finally:
                                try:

                                    position_mode=i.find("div",class_="wfhmode").text
                                except:
                                    position_mode='Not Available'

            # print(i.div.h1.text)
            # print(i.div.div.a.text)
            # print(i.find("div",class_="exp").text)
            # print(i.find("div",class_="salary").text)
            # print(i.find("span",class_="location").text)
            # print(i.find("div",class_="wfhmode").text)
        return {"position_name":position_name,"position_company":position_company,"position_exp":position_exp,
                   "position_salary":position_salary,"position_location":position_location,"position_mode":position_mode }
        

    
    except Exception as e:
        return {"error":str(e)},500

    # for j in position_detail