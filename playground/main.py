from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return 'nothing to see here!'

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:x>')
def playx(x):
    return render_template('playx.html', times=x)

if __name__=="__main__":
    app.run(debug=True)