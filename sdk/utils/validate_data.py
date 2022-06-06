# Schema validation
from typing import Tuple


def validate_by_schema(data_schema: dict, data_to_validate: dict) -> Tuple[dict, dict]:
    """
    Required fields in the schema:
    - required
    - type

    - default is optional and only used if required is false


    Example Schema::

    >>>   schema = {"fieldOne": {"type": dict, "required": True},
    >>>    "fieldTwo": {"type": str, "required": True},
    >>>    "fieldThree": {"type": str, "default": "someUser", "required": False}}

    :param data_schema:
    :type data_schema:
    :param data_to_validate:
    :type data_to_validate:
    :return:
    :rtype:
    """
    validated_data = {}
    errors = {}
    for key, value in data_schema.items():
        if data_schema[key]["required"]:

            if key in data_to_validate:
                if type(data_to_validate[key]) == data_schema[key]["type"]:
                    validated_data[key] = data_to_validate[key]
                else:
                    errors[key] = f"Field should be of type '{data_schema[key]['type']}'"
            else:
                errors[key] = "Field is required"
        else:
            if key in data_to_validate:
                if type(data_to_validate[key]) == data_schema[key]["type"]:
                    validated_data[key] = data_to_validate[key]
                else:
                    errors[key] = f"Field should be of type '{data_schema[key]['type']}'"
            else:
                if "default" in data_schema[key]:
                    validated_data[key] = data_schema[key]["default"]
                else:
                    validated_data[key] = None
    return errors, validated_data
