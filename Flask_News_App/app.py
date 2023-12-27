from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route("/")
def index():
    # Init
    newsapi = NewsApiClient(api_key='93603a0cab564e0b8a3e702330b907d3')
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='al-jazeera-english')
    articles = top_headlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news,desc,img)

    return render_template("index.html",context=mylist)



if __name__== "__main__":
    app.run(debug=True)
