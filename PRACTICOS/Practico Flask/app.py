from flask import Flask
import sqlalchemy
app=Flask(__name__)
@app.route('/')
def inicio():
    return 'app'
if __name__=='__main__':
    app.run()