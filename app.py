from flask import Flask, render_template, jsonify
#flask is better for portfolio which have less number of loads
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# UptimeRobot should ping this endpoint to keep the free Render instance awake
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
