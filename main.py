from flask import Flask

# === get necessaries from Flask ==========
from flask import render_template, jsonify, request

app = Flask(__name__)


# === SHOW screen from index ===============
@app.route("/", methods=['GET', 'POST'])
# PURPOSE: to show content in the URL: '/', which also means 'localhost:5000' as defaut
def show_screen():
    # PURPOSE: the frontend/UI application would be 'html' file
    # 'render_template': use the file as the UI/frontend of the app
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')
