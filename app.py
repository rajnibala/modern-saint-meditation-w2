from flask import Flask, render_template, jsonify
from database import load_program_from_db


app = Flask(__name__)

@app.route("/")
def hello_MSM():
    program = load_program_from_db()
    return render_template('Home.html', program=program, company_name='MSM')

@app.route("/api/program")
def list_program():
    program = load_program_from_db()  # Load programs from the database
    return jsonify(program)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
