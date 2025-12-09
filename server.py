from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
  return f'<h1>OMG!!</h1>'

@app.route('/name')
def name():
  return f'<1>Satayu Boonmuang</h1>'

# if __name__ == '__main__':
#   app.run(debug=True)