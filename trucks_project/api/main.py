import json
from flask import Flask, request, jsonify, abort
from api.util.random import generate_random_uuid
from truck_delivery_fernando.client_manager import ClientManager

API_NAME = "/api/v1"
app = Flask(__name__)


@app.route(f"{API_NAME}/client", methods=["POST"])
def save_client():
    client_params = json.dumps(request.json)
    id = generate_random_uuid()
    result = ClientManager().save_document(id, client_params)
    if not result:
        abort(400, "Bad Request, please review the parameters sent.")
    return {"status": "Success", "id": id}


@app.route(f"{API_NAME}/clients", methods=["GET"])
def get_all_clients():
    result = ClientManager().get_all()
    return jsonify(result)


@app.route(f"{API_NAME}/client/<client_id>", methods=["GET"])
def get_client_by_id(client_id):
    result = ClientManager().get_document(client_id)
    if result == '{}':
        abort(404, "Client not found!.")
    return jsonify(result)


@app.route(f"{API_NAME}/client/<client_id>", methods=["DELETE"])
def delete_client_by_id(client_id):
    result = ClientManager().delete(client_id)
    if result == 0:
        abort(404, "Client not found!.")
    return {"status": "Success", "message": f"Client id [ {client_id} ] deleted from DB."}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=True)
