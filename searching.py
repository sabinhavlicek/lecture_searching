import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    # načtení povolených klíčů
    with open("sequential.json", "r") as file:
        allowed_key = json.load(file)
    # ověření, zda je zadaný klíč v těch povolených
    if field not in allowed_key:
        return None
    with open(file_name, "r") as file_2:
        data = json.load(file_2)
    return data.get(field)

def pattern_search(sequence, pattern):

def main():
    #pass
    #volání fce read_data
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

if __name__ == '__main__':
    main()