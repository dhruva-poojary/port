from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    if __name__ == '__main__':
    # Adding host='0.0.0.0' opens it to your local Wi-Fi network
    app.run(host='0.0.0.0', port=5000, debug=True)