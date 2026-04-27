import yaml

def load_yaml(path):
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception(f"File not found: {path}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")