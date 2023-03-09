from flask import Flask
app = Flask(__name__)

#When the application runs it will take over your command line, you will not be able to type on it anymore because a server application (like flask) never stops running, it keeps waiting for "requests" forever.
#What does this means? 

@app.route('/todos', methods=['GET'])
def hello_world():
    return "<h1>Hello!</h1>" 


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)