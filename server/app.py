from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Get a cookie named 'user' if it exists, or set a default value if it doesn't
    user = request.cookies.get('user', 'Liverpool FC')
    return f'Hello, {user}!'

@app.route('/set_cookie/<username>')
def set_cookie(username):
    # Create a response object
    response = make_response(f'Setting cookie for {username}')
    
    # Set a cookie named 'user' with the provided username
    response.set_cookie('user', username)
    
    return response

@app.route('/clear_cookie')
def clear_cookie():
    # Create a response object to clear the 'user' cookie
    response = make_response('Cookie cleared')
    
    # Set the 'user' cookie with an empty value and an expiry date in the past to clear it
    response.set_cookie('user', '', expires=0)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
