from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Process user_message and return a response
    return jsonify({'response': 'Your response here'})

if __name__ == '__main__':
    app.run(debug=True)

