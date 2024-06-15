from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def ini():
    return render_template('ini.html')
@app.route('/validacion', methods=['POST','GET'])
def validacion():
    if request.method=='POST':
        if request.form['nom'] and request.form['cont']:
            return render_template('tio_paulo.html')
        else:
            return render_template('ini.html')
@app.route('/sydney')
def sydney():
    return render_template('sydney.html')
if __name__=='__main__':
    app.run(debug=True)