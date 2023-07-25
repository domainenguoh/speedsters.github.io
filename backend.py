from flask import Flask

app = Flask(__name__)

@app.route('/api')
def get_data_from_backend():
    return 'Hello from the Backend!'

if __name__ == '__main__':
    app.run(debug=True)
