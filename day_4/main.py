from __future__ import annotations
from helper.main import read_data, sanitize, FILE, TEST_FILE

print("Day 4")

test_data = sanitize(read_data(TEST_FILE))
data = sanitize(read_data(FILE))


def overlaps(data: [str]):
    counter = 0
    for e in data:
        range_1 = SectionRange.create_from_str(e.split(",")[0])
        range_2 = SectionRange.create_from_str(e.split(",")[1])

        if range_1.is_overlapped(range_2) or range_2.is_overlapped(range_1):
            counter += 1
            continue

    return counter


class SectionRange:
    def __init__(self, start: int, end: int):
        self.end = end
        self.start = start

    def is_overlapped(self, range: SectionRange):
        """
        Necessary to import from __future__ import annotations for Range typing
        @see https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
        :param range:
        :return:
        """
        return range.start >= self.start and range.end <= self.end

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    @classmethod
    def create_from_str(cls, input_range: str):
        return cls(int(input_range.split('-')[0]), int(input_range.split('-')[1]))


assert (SectionRange(2, 8)).is_overlapped(SectionRange(3, 7))
assert 2 == SectionRange.create_from_str('2-4').start
assert 4 == SectionRange.create_from_str('2-4').end
assert 2 == overlaps(test_data)

print(overlaps(data))
assert 538 == overlaps(data)
