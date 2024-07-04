from flask import Flask, render_template, jsonify

app = Flask(__name__)

USERS = [{
    'id': 1,
    'name': 'User1',
    'email': 'User1@example.com',
    'password': 'secret1',
    'project': 'project 1'
}, {
    'id': 2,
    'name': 'User2',
    'email': 'User2@example.com',
    'password': 'secret2',
    'project': 'project 2'
}, {
    'id': 3,
    'name': 'User3',
    'email': 'User3@example.com',
    'password': 'secret3',
    'project': 'project 3'
}, {
    'id': 4,
    'name': 'User4',
    'email': 'User3@example.com',
    'password': 'secret4',
    'project': 'project 4'
}, 
    {
        'id': 5,
        'name': 'User5',
        'email': 'User5@example.com',
        'password': 'secret5',
        'project': 'project 5'}
]


@app.route('/')
def home():
    return render_template('home.html', users=USERS)

@app.route('/api/users')
def user_data():
    return jsonify(USERS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
