from flask import Flask, request 
app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json
    return {"recommendations": ["Bali", "Switzerland"]}