from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      fname = request.form['filename']
      f.save(fname)
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)