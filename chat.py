from flask import Flask
import os

# Create a Flask instance
app = Flask(__name__)

# Define a route for the 'ask' endpoint
@app.route('/ask')
def hello_world():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))  # Use PORT env var for cloud platforms like Render/Heroku
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False disables debug mode in production
