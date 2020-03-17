from flask import Flask, request, jsonify, render_template
import scraper as covid
import newsscraper as news
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route('/')
def hello_world():
    return render_template('covid.html')


@app.route('/getdata', methods=["GET"])
def getdata():
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    if request.method == "GET":
        state = request.args.get('state')
        pretty = request.args.get('pretty')
        if pretty is None:
            app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        elif pretty == "1":
            app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        if state is None:
            a = covid.covidscraper()
            return jsonify(a.getdata())
        else:
            a = covid.covidscraper(state=state)
            return jsonify(a.getdata())


@app.route('/news', methods=["GET"])
def getnews():
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    if request.method == "GET":
        pretty = request.args.get('pretty')
        if pretty is None:
            app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        elif pretty == "1":
            app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        b = news.newsscraper()
        return jsonify(b.getnews())


if __name__ == '__main__':
    app.run()
