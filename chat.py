from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route for the 'hello world' endpoint
@app.route('/ask')
def hello_world():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
