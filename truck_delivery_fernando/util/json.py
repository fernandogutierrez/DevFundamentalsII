import json


def validate_json(obj):
    try:
        json.loads(obj)
    except ValueError:
        return False
    except Exception:
        return False
    return True
