from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "q nhi ho rhi hai padhai"


app.run(host="0.0.0.0", port=5000)


