import random
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS to allow the frontend to request data
CORS(app)

# The dictionary of distractions
distractions = {
    "food_thoughts": [
        "Are tacos a spiritual food? I feel like they could be.",
        "Suddenly thinking about the profound crunchiness of a good pickle.",
        "If you meditate long enough, can you taste snacks with your mind?",
        "I wonder if my sourdough starter needs me."
    ],
    "random_facts": [
        "A group of flamingos is called a 'flamboyance'. How cool is that?",
        "Did you know that bubble wrap was originally intended to be wallpaper?",
        "Squirrels forget where they hide most of their nuts. Relatable.",
        "The word 'meditation' sounds a bit weird if you say it too many times. Med-i-ta-tion. See?"
    ],
    "existential_questions": [
        "Do you think dolphins ever get anxiety? I bet they do.",
        "What if trees are meditating all the time and we just don't know it?",
        "Are we all just living in a simulation, and the loading screen is just... blinking?",
        "If I'm thinking about not thinking, am I still meditating?"
    ],
    "cringe_memories": [
        "Oh no, I just remembered that one embarrassing thing I did in 7th grade. Why now?!",
        "Remember that time I waved back at someone who wasn't waving at me? Yikes.",
        "My brain just decided to replay that awkward silence from a conversation three years ago."
    ]
}

@app.route("/get-distraction")
def get_distraction():
    """This endpoint picks and returns a random distraction."""
    category = random.choice(list(distractions.keys()))
    thought = random.choice(distractions[category])
    return jsonify(thought=thought) # Return the thought as JSON data

if __name__ == "__main__":
    # Runs the web server on http://127.0.0.1:5000
    app.run(debug=True)
