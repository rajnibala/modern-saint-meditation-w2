from flask import Flask, render_template, jsonify
app = Flask(__name__)
PROGRAMS = [
  {
    'id': 1,
    'title': 'Program1',
    'Package': 'Bengaluru, India',
    'Fees': 'Rs. 5,000'
  },
  {
    'id': 2,
    'title': 'Program2',
    'Package': 'Delhi, India',
    'Fees': 'Rs. 1500'
  },
  {
    'id': 3,
    'title': 'Program3',
    'Package': 'Remote'
  },
  {
    'id': 4,
    'title': 'Programs4',
    'Package': 'San Francisco, USA',
    'Fees': '1500'
  }
]

@app.route("/")
def hello_MSM():
    return render_template('Home.html',Programs=PROGRAMS, company_name='MSM')

@app.route("/api/Programs")
def list_Programs():
    return jsonify(PROGRAMS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
