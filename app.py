from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square', methods=['POST'])
def square():
    try:
        number = request.form['number']
        squared_number = float(number) ** 2
        return jsonify({'result': squared_number})
    except ValueError:
        return jsonify({'error': 'Please enter a valid number'}), 400

if __name__ == '__main__':
    app.run(debug=True)
