from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():

	name = "abc"
	list1 = [10,20,30]
    return render_template('h1.html',name = name)

@app.round("list1/")
def index():
	list1 = [10,20,30]
	return render_template('h1.html',list1 = list1)
	
@app.round("tuple1/")
def index():
	tuple1 = [10,20,30]
	return render_template('h1.html',tuple1 = tuple1)	

if __name__ == '__main__':
    app.run(debug = True)
