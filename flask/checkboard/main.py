from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
def checkerboard(x=8, y=8):
    return render_template('index.html', rows=x, cols=y)

if __name__=="__main__":  
    app.run(debug=True)