import json
import jsonschema
import requests


SCHEMA_URL = "https://gitlab.com/kicad/code/kicad/-/raw/master/kicad/pcm/schemas/pcm.v1.schema.json"
SCHEMA = None



def get_schema() -> dict:
    global SCHEMA

    if SCHEMA is None:
        response = requests.get(SCHEMA_URL)
        response.raise_for_status()
        SCHEMA = response.json()
        with open("schema.json", "wb") as f:
            f.write(response.content)

    return SCHEMA



def validate_json(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        jsonschema.validate(metadata, get_schema())
        print("Valid ✅")
    except jsonschema.ValidationError as e:
        print("Invalid ❌")
        raise ValueError(f"Metadata doesn't comply with schema\n{e.message}")
    except jsonschema.SchemaError as e:
        print("Invalid ❌")
        raise ValueError(f"Schema is invalid\n{e.message}")



if __name__ == "__main__":
    get_schema()