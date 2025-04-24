# Демонстрационный Flask API-заглушка
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "AI SportClub Assistant is running."

if __name__ == "__main__":
    app.run(debug=True)
