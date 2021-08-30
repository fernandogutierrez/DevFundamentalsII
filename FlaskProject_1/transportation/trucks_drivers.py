from flask import (Flask, jsonify, request)

drivers = [
    {
        'id': 0,
        'name': 'Fernando',
        'last_name': 'Gutierrez',
        'license_number': '144589',
        'truck_id': 1
    },
    {
        'id': 1,
        'name': 'Javier',
        'last_name': 'Caceres',
        'license_number': '589636',
        'truck_id': 2
    },

]


trucks = [
    {
        'id': 0,
        'plate': 'TRUCKB',
        'type': 'Crane Truck',
        'color': 'Red',
        'height': '2.45 m',
        'volume': '86 cubic meters'
    },
    {
        'id': 1,
        'plate': 'ROO 8305',
        'type': 'Crane Truck',
        'color': 'Blue',
        'height': '2.20 m',
        'volume': '90 cubic meters'
    },
    {
        'id': 2,
        'plate': 'TRUCKB',
        'type': 'KA 14A 1478',
        'color': 'Orange',
        'height': '2.10 m',
        'volume': '92 cubic meters'
    }
]
app = Flask(__name__)
API_NAME = "/api/v1"


@app.route(f"{API_NAME}/trucks", methods=["GET"])
def truck_list():
    """
    truck_list --> Get the list of all trucks available
    Return:
        trucks(dict): list of trucks
    """
    return jsonify(trucks)


@app.route(f"{API_NAME}/trucks/<truck_id>", methods=["GET"])
def get_truck_by_id(truck_id):
    """
    get_truck_by_id --> Get a truck given an id
    Args:
        truck_id(int): The truck id to look for
    Return:
        truck(dict): A truck
    """

    for truck in trucks:
        if truck.get("id") == int(truck_id):
            return jsonify(truck)
    else:
        return {
            'error': 'Truck not found.',
            'status': 404
        }


@app.route(f"{API_NAME}/trucks", methods=["POST"])
def save_truck():
    """
    save_truck --> Save a given truck into a truck list.
    Return:
        message(dict): A dict that indicates that the truck was saved.
    """
    truck_json = request.json
    trucks.append(truck_json)
    return jsonify({
        'message': "The truck was saved.",
        'status': 200
    })


@app.route(f"{API_NAME}/trucks/<truck_id>", methods=["DELETE"])
def remove_truck(truck_id):
    """
    truck_id --> Remove a truck given an id.
    Args:
        truck_id(int): The truck id to remove.
    Return:
        result(dict): A dictionary that indicates if the truck was removed.
    """
    global trucks
    trucks = [truck for truck in trucks if truck.get("id") != int(truck_id)]
    return jsonify({
        'message': f"Truck with id {truck_id} was removed.",
        'status': 200
    })


@app.route(f"{API_NAME}/drivers", methods=["GET"])
def driver_list():
    """
    driver_list --> Get the list of all drivers available
    Return:
        drivers(dict): list of drivers
    """
    return jsonify(drivers)


@app.route(f"{API_NAME}/drivers/<driver_id>", methods=["GET"])
def get_driver_by_id(driver_id):
    """
    get_driver_by_id --> Get a driver given an id.
    Args:
        driver_id(int): The driver id to look for.
    Return:
        driver(dict): A driver.
    """
    for driver in drivers:
        if driver.get("id") == int(driver_id):
            return jsonify(driver)
    else:
        return {
            'error': 'Driver not found.',
            'status': 404
        }


@app.route(f"{API_NAME}/drivers", methods=["POST"])
def save_driver():
    """
    save_driver --> Save a given driver into the drivers list
    Return:
        truck(dict): A dict that indicates the driver was saved.
    """
    driver_json = request.json
    drivers.append(driver_json)
    return jsonify({
        'message': "The driver was saved.",
        'status': 200
    })


@app.route(f"{API_NAME}/drivers/<driver_id>", methods=["DELETE"])
def remove_driver(driver_id):
    """
    remove_driver --> Remove a driver given an id.
    Args:
        truck_id(int): The driver id to remove.
    Return:
        result(dict): A dictionary that indicates if the driver was removed.
    """
    global drivers
    drivers = [driver for driver in drivers if driver.get("id") != int(driver_id)]
    return jsonify({
        'message': f"Driver with id {driver_id} was removed.",
        'status': 200
    })


@app.route(f"{API_NAME}/driver/<driver_name_or_id>/truck", methods=["GET"])
def get_truck_of_driver(driver_name_or_id):
    """
    get_truck_of_driver --> Get a truck given a driver id or name.
    Args:
        driver_name_or_id(int): The driver name or id to look for.
    Return:
        driver(dict): A driver.
    """
    for driver in drivers:
        if str(driver.get("id")) == driver_name_or_id or driver.get("name") == driver_name_or_id:
            return get_truck_by_id(driver.get("truck_id"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001, use_reloader=True)
