import json
from flask import Flask, request, jsonify, abort
from api.util.random import generate_random_uuid
from truck_delivery_fernando.client_manager import ClientManager

# from api.views import client_api

API_NAME = "/api/v1"
app = Flask(__name__)


@app.route(f"{API_NAME}/client", methods=["POST"])
def save_client():
    client_params = json.dumps(request.json)
    id = generate_random_uuid()
    result = ClientManager().save_document(id, client_params)
    return {"status": "Success", "id": id} if result else {"status": "Failed"}


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


# app.add_url_rule("/clients", view_func=client_api.get_all_clients)
# app.add_url_rule("/clients", view_func=client_api.save_client, methods=["POST"])
# app.add_url_rule("/client/<client_id>", view_func=client_api.get_client_by_id)
# app.add_url_rule("/client/<client_id>", view_func=client_api.delete_client_by_id, methods=["DELETE"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=True)
