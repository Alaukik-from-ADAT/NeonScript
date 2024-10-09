import sys

variables = {}

def interpret(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("say "):
            output = line[4:].strip('"')
            print(output)
        elif line.startswith("let "):
            parts = line.split()
            variables[parts[2]] = int(parts[4])
        elif " plus " in line:
            parts = line.split(" ")
            result = variables[parts[1]] + int(parts[3])
            print(f"{parts[1]} plus {parts[3]} = {result}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python neonscript.py <filename>")
    else:
        interpret(sys.argv[1])
