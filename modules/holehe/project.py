from modules.holehe.extensions import holehe_registry

# Import your transforms here
from transforms import GreetPerson

if __name__ == "__main__":
    holehe_registry.write_local_mtz(command="./venv/bin/python3")
