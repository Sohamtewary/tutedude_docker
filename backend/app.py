from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS is required so your frontend browser can communicate with this API
CORS(app)

@app.route('/api/submit', methods=['POST'])
def handle_submit():
    # Handles both JSON and standard HTML Form submissions
    data = request.form if request.form else request.get_json()
    
    username = data.get('username', 'Anonymous')
    email = data.get('email', 'No Email Provided')
    
    # Process the data (Example response)
    return jsonify({
        "status": "Success",
        "message": f"Data received for {username}",
        "preview": {
            "username": username,
            "email": email
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)