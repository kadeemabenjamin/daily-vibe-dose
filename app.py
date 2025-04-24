from flask import Flask, render_template
import random

app = Flask(__name__)

# List of positive daily messages
messages = [
    "You are capable of amazing things.",
    "Keep going, you're doing great!",
    "Today is a new opportunity to grow.",
    "Believe in your potential.",
    "Your mindset shapes your future."
]

@app.route("/")
def home():
    vibe = random.choice(messages)
    return render_template("index.html", vibe=vibe)

if __name__ == "__main__":
    app.run(debug=True)
