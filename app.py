
import requests
import json
from flask import Flask, jsonify
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return "Bot power by superAI"

@app.route("/chatbot/<string:user_message>")
def bot_reply(user_message):
    data={"sender":"user_name","message":user_message}
    data = json.dumps(data)
    url = "http://localhost:5005/webhooks/rest/webhook"
    j = requests.post(url, data)
    msg = j.json()
    # msg = {"bot"+str(i):msg[i] for i in range(len(msg))}
    return jsonify(msg)

# run the application
if __name__ == "__main__":  
    app.run(debug=True)


