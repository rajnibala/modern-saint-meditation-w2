from flask import Flask, render_template, jsonify 
from database import load_programs_from_db

app = Flask(__name__)

@app.route("/")
def hello_MSM():
    programs = load_programs_from_db()
    return render_template('Home.html', programs=programs, company_name='MSM')

@app.route("/api/Programs")
def list_Programs():
    programs = load_programs_from_db()  # Load programs here
    return jsonify(programs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
