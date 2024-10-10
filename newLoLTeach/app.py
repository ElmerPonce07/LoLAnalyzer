from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = OPENAPIKEY

app = Flask(__name__)

system_message = {
    "role": "system",
    "content": "YOUR NAME IS SUMMONER'S ORACLE. YOU ARE A CHARACTER IN THE LEAGUE OF LEGENDS UNIVERSE THAT HELPS SUMMONERS IMPROVE THEIR GAMEPLAY. ASK FOR THEIR RANK, ROLE, AND MAIN CHAMP BEFORE STARTING."
}

messages = [system_message]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    if user_input.lower() in ["quit", "exit", "bye"]:
        return jsonify({"response": "Exiting the chatbot. Goodbye!"})

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        oracle_response = response['choices'][0]['message']['content'].strip()
        messages.append({"role": "assistant", "content": oracle_response})

        return jsonify({"response": oracle_response})

    except Exception as e:
        return jsonify({"response": "Error occurred: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)
