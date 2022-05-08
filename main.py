import json
import requests
from flask import request,render_template,Flask, url_for

app = Flask(__name__)


api_key_list = ["90cdd48823dd4508943512eca03110ec","e9980fbb7ab142e092b142fdcab23862"]
for api in api_key_list:
          
          api_link = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey={api}"

          r = requests.get(api_link)
          if r.status_code == 200:
               break

def data_modifier(article_list):
     for x in article_list:
          date = x['publishedAt']
          x['publishedAt'] = date_changer(date)
          if x['urlToImage'] == None:
               # print("no")
               x['urlToImage'] = 'https://res.cloudinary.com/dzf5noyqz/image/upload/v1651941941/NewsBite/noImage_tiznad.png'
          if x['description'] == None:
               article_list.remove(x)
          # if len(x['title']) <= 97 :
          #      x['title'] = x['title'] + (97 - len(x['title']))*" "
     return article_list

def date_changer(date_str):
     date_str = date_str[0:-1]
     # date_str = date_str.replace(":"," : ")
     date_str = date_str.replace("-","/")
     
     date_time = date_str.split("T")
     
               
     return date_time[1] + " " + date_time[0]
     
@app.route("/",methods = ["POST","GET"])
def home():
     if request.method == "POST":
          name = request.form["search"]
          
          api_link = f"https://newsapi.org/v2/everything?q={name}&language=en&pageSize=100&apiKey={api}"
          r = requests.get(api_link)
          

          data = json.loads(r.content)
          
          main_data = data["articles"]
          all_news = data_modifier(main_data)

          return render_template("index.html",all_news = all_news)
         
          
     for api in api_key_list:
          
          api_link = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey={api}"

          r = requests.get(api_link)
          if r.status_code == 200:
               break
     data = json.loads(r.content)
     if data['status'] != 'error':
          main_data = data["articles"]
          all_news = data_modifier(main_data)
          return render_template("index.html",all_news = all_news)
     else:
          return render_template('error.html')
@app.route("/top_news/<string:name>")                 
def headline(name): 
     
          if name == "top-headlines":
               api_link = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey={api}"
          else:          
               api_link = f"https://newsapi.org/v2/top-headlines?country=in&category={name}&pageSize=100&apiKey={api}"
          r = requests.get(api_link)
     
          data = json.loads(r.content)
     
          main_data = data["articles"]
          all_news = data_modifier(main_data)
         
          return render_template("index.html",all_news = all_news)
