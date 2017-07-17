from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('portfolio_root.html')

@app.route('/projects')
def projects():
    return render_template('portfolio_projects.html')

@app.route('/about')
def about():
    return render_template('portfolio_about.html')

app.run(debug = True)
