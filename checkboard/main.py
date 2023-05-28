from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/4')
def halfCheckboard():
    return render_template('four.html')

@app.route('/<int:x>')
def rows(x):
    return render_template('row.html', x=x)

if __name__==('__main__'):
    app.run(debug=True)