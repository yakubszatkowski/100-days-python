from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    extra = request.args.get('extra')
    extra2 = request.args.get('extra2')
    if extra:
        user_data['extra'] = extra
    if extra2:
        user_data['extra2'] = extra2

    return jsonify(user_data)


@app.route('/create-user', methods=['POST'])
def create_user():
    # if request.method == 'post':  # this is used when having multiple methods
    data = request.get_json()
    return jsonify(data)


@app.route('/adv-create-user', methods=['POST'])
def advanced_create_user():
    data = {
        'user_id': request.args.get('user_id'),
        'name': request.args.get('name', 'None'),
        'email': request.args.get('email', 'None')
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
