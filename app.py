from flask import Flask, jsonify, request
from flask_cors import cross_origin
import uuid

app = Flask(__name__)

users = {}
tokens = {}

@app.route('/oauth/token', methods = ['POST'])
@cross_origin()
def token():
  if not request.form.get('grant_type') == 'password':
    return jsonify({
      'error': 'unsupported_grant_type',
      'error_description': 'This server only supports the password grant type'
    }), 400

  user = users.get(request.form.get('username'))
  if not (user and user.get('password') == request.form['password']):
    return jsonify({
      'error': 'invalid_grant',
      'error_description': 'Invalid username or password'
    }), 400

  token     = uuid.uuid4().hex
  old_token = user.get('token')
  if old_token and tokens.has_key(old_token):
    del tokens[old_token]
  user['token'] = token
  tokens[token] = user['email']

  return jsonify({'access_token':token})


@app.route('/users.json', methods = ['POST'])
@cross_origin()
def add_user():
  email    = request.form.get('user[email]')
  password = request.form.get('user[password]')

  if not (email and password):
    return jsonify({'error': 'Missing user email or password'}), 401

  if users.has_key(email):
    return jsonify({'error': 'Email already registered'}), 401

  users[email] = {'email': email, 'password': password, token: None}

  return jsonify({}), 201


if __name__ == "__main__":
  app.run(port=3000)
