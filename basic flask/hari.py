from flask import Flask,render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {"maths":80,"c++":50,"java":40}
    return render_template('tmp.html',result=dict)

if __name__=="__main__":
    app.run(debug=True)
