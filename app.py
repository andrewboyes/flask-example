from flask import Flask, request
import json

app = Flask(__name__)

#decorator = @
@app.route("/")
def home():
    return "Flask app is up and running!", 200

@app.route("/get-json", methods=["GET"])
def get_json():
    python_dict = {
        "key1": "value1",
        "key2": "value2"
    }
    print("Get JSON endpoint invoked!")
    print('Key1:')
    print(python_dict["key1"])
    response = json.dumps(python_dict)
    return response, 200

@app.route("/post-json", methods=["POST"])
def post_json():
    request_data = request.json
    print(request_data)
    print(request_data["key"])
    return "Success", 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)