from flask import Flask
from utils import get_naukari_data

app=Flask(__name__)


@app.route("/")
def main(postion,loc):
    url_list=get_naukari_data.get_position_url_list(position=postion,location=loc)
    for i in range(2):
        print(get_naukari_data.get_position_details(url_list[i]))

   

if __name__=="__main__":

    pos=input("enter your position: ")
    loc=input("enter your location: ")
    main(pos,loc)
    app.run()