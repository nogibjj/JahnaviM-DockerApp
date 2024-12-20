from flask import (
    Flask,
    request,
    render_template_string,
)
from dotenv import load_dotenv
import random

load_dotenv()

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<body>
    <form method="POST" action="/">
        <label>Having a bum day? Let's make it better! Hit this button:</label>
        <button>Cheer Me Up!</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=["GET", "POST"])

def hello_world():
    cheer_up_phrases = [
        "Data never sleeps, but neither do breakthroughs—you're crushing it!",
        "You’re like a neural net—always learning and adapting!",
        "Remember, even NaN values are part of the dataset!",
        "Life’s a gradient descent—keep moving toward your optimum!",
        "Your hard work is the feature everyone notices!",
        "Keep calm and let the algorithm do the heavy lifting!",
        "Debugging life one line of code at a time—keep it up!",
        "Your data game is *outlier-level* impressive!",
        "You're a clustering champ—always finding your center!",
        "Master’s degree: Loading... 90% complete. You’ve got this!",
        "You’re the key to cracking the ultimate dataset: life!",
        "Machine learning? More like *mastered* learning!",
        "A few more semesters, and you’re the top variable in the model!",
        "Data wrangling = life wrangling. You’re doing both like a pro!",
        "Remember, correlation doesn’t imply exhaustion—rest up and conquer!"
    ]

    if request.method == "POST":
        return f"<h1>{random.choice(cheer_up_phrases)}</h1>"
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)