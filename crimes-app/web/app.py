from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route('/')
def root():
	return status()

@app.route('/status')
def status():
	return render_template("status.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
