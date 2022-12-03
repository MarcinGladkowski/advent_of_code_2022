TEST_FILE = 'test_input.txt'
FILE = 'input.txt'


def read_data(file: str):
    with open(file) as f:
        return f.readlines()


def sanitize(data: [str]):
    return [x.replace("\n", "") for x in data]
