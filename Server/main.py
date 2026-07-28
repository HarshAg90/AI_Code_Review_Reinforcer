from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_data():
    # Optional: read query parameters sent by the client
    key1 = request.args.get("key1")
    key2 = request.args.get("key2")

    return jsonify({
        "status": "success",
        "message": "Request received successfully",
        "data": {
            "key1": key1,
            "key2": key2
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)

'''
changesssssssssssssssssssssssssssssss
changesssssssssssssssssssssssssssssss
changesssssssssssssssssssssssssssssss
'''