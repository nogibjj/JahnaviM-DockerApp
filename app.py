from flask import (
    Flask,
    request,
    render_template_string,
)
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Request Form</title>
</head>
<body>
    <h1>Enter Your Details</h1>
    <form method="POST" action="/">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="genre">Genre:</label>
        <input type="text" id="genre" name="genre" required><br><br>
        <label for="mood">Mood:</label>
        <input type="text" id="mood" name="mood" required><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=["GET", "POST"])

def hello_world():
    if request.method == "POST":
        return f"<h1>Hello World!</h1>"
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)