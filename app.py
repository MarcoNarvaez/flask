from app import Flask

app = Flask(__name__)

@app.route('/')

def principal():
    return "<h1>hola,buenos dias</h1>"

if __name__ == '__main__':
    app.run()