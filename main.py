from flask import Flask

# === get necessaries from Flask ==========
from flask import render_template, jsonify, request

app = Flask(__name__)
app.secret_key = 'khangdepzai'


# === SHOW screen from index ===============
@app.route("/create_account", methods=['GET', 'POST'])
# PURPOSE: to show content in the URL: '/', which also means 'localhost:5000' as defaut
def show_screen_create_account():
    # PURPOSE: the frontend/UI application would be 'html' file
    # 'render_template': use the file as the UI/frontend of the app
    return render_template('create_account.html')


@app.route("/login", methods=['GET', 'POST'])
def show_screen_login():
    return render_template('login.html')


@app.route("/homepage", methods=['GET', 'POST'])
def show_screen_homepage():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')
