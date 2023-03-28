import json


def insert_description(schema, json_data):
    for field in json_data["fields"]:
        for key, value in field.items():
            if "fields" in value:
                schema = insert_description(schema, value)
            elif "description" in value:
                search_pattern = f"{key} = {{"
                formatted_description = value["description"].replace("\n", "\\n").replace('"', '\\"')
                replace_pattern = f'{key} = {{ "description": "{formatted_description}", '
                schema = schema.replace(search_pattern, replace_pattern)
            else:
                print(f"Field '{key}' does not have a description.")

            if "elements" in value:
                if "fields" in value["elements"]:
                    schema = insert_description(schema, value["elements"])

    return schema


with open("datadog.lua", "r") as f:
    lua_schema = f.read()

with open("datadog.json", "r") as f:
    json_data = json.load(f)

updated_schema = insert_description(lua_schema, json_data)

with open("updated_schema.lua", "w") as f:
    f.write(updated_schema)

print("Updated schema has been written to 'updated_schema.lua'")