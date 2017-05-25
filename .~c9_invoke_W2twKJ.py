from flask import Flask, request, render_template, jsonify, json
import os
from modules import query

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    art = query.getArticleFromDB(1)
    print(art.getId())
    print(art.getUrl())
    return render_template("article.html", article = art) #, aConfigWeb = aConfigWeb, ProgTemp = database.TempToHeat)

@app.route('/updateart', methods=['POST',])
def updateart():
    ret_data = {"value": request.args.get('echoValue')}
    print(ret_data)
    return jsonify(ret_data)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)













