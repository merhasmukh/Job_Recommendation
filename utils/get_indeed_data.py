
# import module
import requests
from bs4 import BeautifulSoup

# user define function
# Scrape the data
# and get in string
def getdata(url):
    r = requests.get(url)
    return r.text

# Get Html code using parse
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    print("htmldata",htmldata)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # return html code
    return(soup)

# filter job data using
# find_all function
def job_data(soup):
    
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    for item in soup.find_all("a", class_="jobtitle turnstileLink"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return(result_1)

def company_data(soup):
  
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    result = ""
    for item in soup.find_all("div", class_="sjcl"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
  
    res = []
    for i in range(1, len(result_1)):
        if len(result_1[i]) > 1:
            res.append(result_1[i])
    return(res)

 