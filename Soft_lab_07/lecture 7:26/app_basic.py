from flask import Flask                # 1. Import Flask

app = Flask(__name__)                  # 2. Create the app

@app.route("/hello")                   # 3. Route (URL)
def hello():                           # 4. View function (Python code)
    return "Hello, class cs699!"       # 5. Response

if __name__ == "__main__":
    app.run(debug=True) 