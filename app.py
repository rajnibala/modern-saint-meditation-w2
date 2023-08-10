from flask import Flask, render_template
app = Flask(__name__)
programs = [
  {
    'id':1,
    'title' : 'Importence of Meditation'
    },
  {
    'id':2,
    'title' : 'Importence of Meditation'
  },
  {
   'id':3,
    'title' : 'Importence of Meditation' 
  }
]



@app.route("/")
def hello_world():
 return render_template('Home.html', programs=programs)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
