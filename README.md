# Flask Token auth

A minimal server implementation in Python for [EAK Simple Auth](https://github.com/digitalplaywright/eak-simple-auth).

## Install

I recommend using a pip and virtual env

    git clone https://github.com/biilmann/flask-token-auth.git
    virtualenv flask-token-auth
    cd flask-token-auth
    source bin/activate
    pip install flask
    pip install flask-cors

## Run

Just run app.py

    python app.py

## Not for production

This is not production software, just a small example of the simplest possible
Oauth2 token authentication service.

Users and tokens are only persisted in memory and will be wiped when the server
is restarted.

Only the very simple Oauth2 "Client Credentials" flow is supported and tokens
never expire.

## License

The MIT License (MIT)

Copyright (c) 2014 Mathias Biilmann Christensen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
