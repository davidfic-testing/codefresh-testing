from flask import Flask
from flask import jsonify
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return 'Flask Dockerized and Spinnaker and testing'

@app.route('/test')
def test():
    return 'this is a new test route'

@app.route('/third')
def third():
    return render_template('hello.html', name=name)

@app.route('/four')
def four():
    return jsonify('hello there')

@app.route('/five')
def five():
    return jsonify('number 5')

@app.route('/six')
def six():
    return jsonify('number 6')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
