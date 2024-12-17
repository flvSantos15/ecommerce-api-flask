from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello world'

# debug is only used in develop enviroment
if __name__ == "__main__":
  app.run(debug=True)