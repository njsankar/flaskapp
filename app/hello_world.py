from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = 'Hello DockerCon 2018!'
    return message

if __name__ == '__main__':
    print(hello_world())