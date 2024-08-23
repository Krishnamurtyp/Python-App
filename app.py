from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return 'Hello World! from Sravya, Akshitha, keerthi'

if __name__ == '__main__':
  app.run()