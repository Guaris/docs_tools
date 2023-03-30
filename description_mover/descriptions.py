import json
import re


def insert_description(schema, json_data, parent_keys=None):
    if parent_keys is None:
        parent_keys = []

    for field in json_data["fields"]:
        for key, value in field.items():
            current_keys = parent_keys + [key]

            if "fields" in value:
                schema = insert_description(schema, value, current_keys)

            if "description" in value:
                search_pattern = f"{key} = {{"
                formatted_description = value["description"].replace("\n", "\\n").replace('"', '\\"')
                replace_pattern = f'{key} = {{ description = "{formatted_description}", '

                if search_pattern in schema:
                    schema = schema.replace(search_pattern, replace_pattern)
                else:
                    nested_key_pattern = " = {"
                    nested_search_pattern = nested_key_pattern.join(current_keys) + " = {"
                    nested_replace_pattern = nested_key_pattern.join(current_keys) + " = { description = \"" + formatted_description + "\", "

                    if re.search(re.escape(nested_search_pattern), schema):
                        schema = re.sub(re.escape(nested_search_pattern), nested_replace_pattern, schema)
                    else:
                        print(f"Couldn't insert description for nested field '{key}' in the schema:\n{formatted_description}\n")

            if "elements" in value and "fields" in value["elements"]:
                schema = insert_description(schema, value["elements"], current_keys)

    return schema


with open("acme.lua", "r") as f:
    lua_schema = f.read()

with open("acme.json", "r") as f:
    json_data = json.load(f)

updated_schema = insert_description(lua_schema, json_data)

with open("updated_schema.lua", "w") as f:
    f.write(updated_schema)