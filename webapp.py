"""
It's important to add two - utf-8 definitions to mysql my.cnf, one in [mysqld] second in [client] and ensure utf-8 coding in db
[mysqld]
character-set-server = utf8
[client]
default-character-set=utf8

"""

from flask import Flask, request, render_template, jsonify, json
import os
from modules import query, article

app = Flask(__name__)
app.debug = True

@app.route('/art/<id>')
def art(id):
    art = query.getArticleFromDB(id)
    print(art.getSourceSite());
    return render_template("article.html", article = art)


@app.route('/')
def index():
    artList = query.getArticlesFromDB("pending")
    return render_template("index.html", articleList = artList)



@app.route('/robot/api/<id>', methods = ['PUT'])
def update_item(id):
    art = article.Article()
    art = article.Article(id = request.json['artId'], title = request.json['artTitle'].encode('utf-8', 'ignore'), description = request.json['artDescr'].encode('utf-8', 'ignore'), url = request.json['artUrl'], imageUrl = request.json['artImgUrl'], imageCrop = request.json['artImgCrop'], tags = request.json['artTags'].encode('utf-8', 'ignore'), status = request.json['artStatus'])
    #return jsonify(art.getDictionary())
    if not request.json:
        print "bad json format"
        abort(400)
    else:
        query.updateArticleInDb(art)
        art = query.getArticleFromDB(art.getId())
        return jsonify(art.getDictionary())

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
