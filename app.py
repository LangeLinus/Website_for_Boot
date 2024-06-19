from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/in_Boot')
def in_Boot():
    return render_template('in_Boot.html')

@app.route('/joining')
def joining():
    return render_template('joining.html')

@app.route('/playground')
def playground():
    return render_template('playground.html')


if __name__ == '__main__':
    app.run(debug=True)

