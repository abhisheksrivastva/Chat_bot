from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load dialog flow from external JSON file
with open('dialog_flow.json') as f:
    dialog_flow = json.load(f)

def match_pattern(user_input, patterns):
    user_input = user_input.lower().strip()
    return any(pattern in user_input for pattern in patterns)

def get_response(user_input, current_state=None):
    user_input = user_input.lower().strip()

    if match_pattern(user_input, dialog_flow["greeting"]["patterns"]):
        return dialog_flow["greeting"]["responses"][0], "greeting"

    if match_pattern(user_input, dialog_flow["feeling_low"]["patterns"]):
        return dialog_flow["feeling_low"]["responses"][0], "feeling_low"

    if match_pattern(user_input, dialog_flow["what_to_do"]["patterns"]):
        return dialog_flow["what_to_do"]["responses"][0], "what_to_do"

    if current_state == "feeling_low" and match_pattern(user_input, dialog_flow["feeling_low"]["follow_up"]["patterns"]):
        return (
            dialog_flow["feeling_low"]["follow_up"]["responses"][0] + " " +
            dialog_flow["feeling_low"]["follow_up"]["suggestions"][0],
            "feeling_low_follow_up"
        )

    if current_state == "what_to_do":
        if "fun" in user_input:
            return dialog_flow["what_to_do"]["follow_up"]["fun"][0], "what_to_do_follow_up"
        elif "productive" in user_input:
            return dialog_flow["what_to_do"]["follow_up"]["productive"][0], "what_to_do_follow_up"
        elif "relaxing" in user_input:
            return dialog_flow["what_to_do"]["follow_up"]["relaxing"][0], "what_to_do_follow_up"

    return dialog_flow["default"]["responses"][0], None

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    current_state = data.get('state', None)
    response, new_state = get_response(user_input, current_state)
    return jsonify({'response': response, 'state': new_state})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
