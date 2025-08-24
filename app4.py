from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Simple HTML page with a button
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Flask Button Demo</title>
</head>
<body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
  <h1 id="message">Hello, world!</h1>
  <button onclick="pressButton()">Press Me</button>

  <script>
    function pressButton() {
      fetch("/button").then(response => response.json()).then(data => {
        const msg = document.getElementById("message")
        msg.innerText = data.message;

        //Remove the message after 3 seconds
        setTimeout(() => {
        msg.innerText = "";
        }, 3000);
      });
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/button")
def button():
    # This runs when the button is pressed
    return jsonify(message="You pressed the button!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

# adding a comment for tracking

# adding a second comment for tracking