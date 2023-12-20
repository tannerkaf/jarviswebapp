from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_speech/<string:speech_text>')
def process_speech(speech_text):
    # Simulate Jarvis response logic (replace this with your actual logic)
    jarvis_responses = [
        "I'm sorry, I didn't understand that.",
        "Tell me more about it.",
        "That's interesting.",
        "I'm here to assist you.",
        "Is there anything else I can help you with?",
        "I'm constantly learning.",
        "Thank you for chatting with me.",
        "Have a great day!",
        # Add more responses here
    ]

    jarvis_response = jarvis_responses.pop(0) if jarvis_responses else "I'm always here to help."
    return jsonify({'response': jarvis_response})

if __name__ == '__main__':
    app.run(debug=True)
