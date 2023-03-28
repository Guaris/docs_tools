import os
import re
import yaml

def extract_description(lua_content):
    description_regex = r"description\s*=\s*\[\[(.+?)\]\]"
    match = re.search(description_regex, lua_content, re.DOTALL)
    return match.group(1).strip() if match else None

directory = os.getcwd()
yaml_file_path = "descriptions.yaml"


if not os.path.exists(yaml_file_path):
    with open(yaml_file_path, "w") as yaml_file:
        yaml_file.write("")


with open(yaml_file_path, "r") as yaml_file:
    yaml_content = yaml.safe_load(yaml_file) or {}


for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)


    if os.path.isfile(file_path) and file_name.endswith(".lua"):

        with open(file_path, "r") as lua_file:
            lua_content = lua_file.read()


        description = extract_description(lua_content)

        if description:

            filename = os.path.splitext(file_name)[0]
            yaml_content[filename] = [{"description": description}]
        else:

            print(f"No description found in {file_name}")


with open(yaml_file_path, "w") as yaml_file:
    yaml.dump(yaml_content, yaml_file, default_flow_style=False)
    #with open(yaml_file_path, "w") as yaml_file:
    #yaml.dump(yaml_content, yaml_file, default_flow_style=False, width=float('inf'), allow_unicode=True)