from flask import Flask
#import datas - obs !

app = Flask(__name__)

@app.route('/')
def hello1():  
    return ' Hello World !'    # ->  funciona - ok 

@app.route('/')
def hello():
    result = """
    <html>
        <header>
            <title> This is Title</title>
        </header>
    <body><h1>Hello World</h1><a href='www.google.com'>
      </body>

    </html>"""

    return result    

if __name__ == '__main__':
    app.run()      # app.run(debug=True)  







