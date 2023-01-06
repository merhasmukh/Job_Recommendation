from flask import Flask
from utils import get_indeed_data
app=Flask(__name__)


@app.route("/")
def home():
    job = "machine+learning+engineer"
    Location = "Ahmedabad"
    url = "https://in.indeed.com/jobs?q="+job+"&l="+Location
    print("URL",url)
    soup = get_indeed_data.html_code(url)
    # print("Soup",soup)
    # call job and company data
    # and store into it var
    job_res = get_indeed_data.job_data(soup)
    com_res = get_indeed_data.company_data(soup)
  
    # Traverse the both data
    temp = 0
    for i in range(1, len(job_res)):
        j = temp
        for j in range(temp, 2+temp):
            print("Company Name and Address : " + com_res[j])
  
        temp = j
        print("Job : " + job_res[i])
        print("-----------------------------")
    # return "hello"
    return job_res

if __name__=="__main__":
    app.run(debug=True)