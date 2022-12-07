from helper.main import read_data, sanitize, TEST_FILE

test_data = sanitize(read_data(TEST_FILE))

print(test_data)