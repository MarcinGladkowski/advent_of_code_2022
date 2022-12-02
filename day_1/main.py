from helper.main import read_data

print("Day 1 results:")
def sums(data: [str]):
    sanitized = [x.replace("\n", "") for x in data]

    sums = [0]
    for el in sanitized:
        if el != '':
            sums[len(sums) - 1] += int(el)
            continue

        sums.append(0)

    return sums


def sum_top_of_three(sums: [int]):
    sums.sort(reverse=True)
    return sum(sums[:3])


data = read_data('test_input.txt')
assert 24000 == max(sums(data))
assert 45000 == sum_top_of_three(sums(data))

aof_data = read_data('input.txt')
assert 70509 == max(sums(aof_data))
print(sum_top_of_three(sums(aof_data)))

