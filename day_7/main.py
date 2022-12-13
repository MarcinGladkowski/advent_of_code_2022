from __future__ import annotations
import re

from helper.main import read_data, sanitize, TEST_FILE

test_data = sanitize(read_data(TEST_FILE))


print(test_data)


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return "(file)"


class Dir:
    def __init__(self, name: str, parent: Dir = None) -> None:
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0

    def add(self, node: Dir | File) -> None:
        self.children.append(node)
        self.size += node.size

    def find(self, name: str):
        for node in self.children:
            if node.name == name:
                return node

    def __str__(self) -> str:
        return "(dir)"


"""
System commands starts with $
"""


def add_dir(io: str, node: Dir):
    name = io.replace('dir', '').strip()
    node.add(Dir(name, node))
    return node


def add_file(io: str, node: Dir):
    split = io.split(' ')
    return node.add(File(split[1], int(split[0])))


class CommandProcessor:
    __list = 'ls'
    __change_directory = 'cd'

    def __init__(self) -> None:
        self.current_command: str | None
        self.main_dir = Dir('/', True)
        self.current_dir = self.main_dir

    def change_command(self, io: str):
        if self._is_cmd_command(io):
            self.current_command = self._sanitize_command(io)

    def _sanitize_command(self, io: str):
        return io.replace('$', ' ').strip()

    def execute_commands(self, commands: list):
        for io in commands:
            self.execute(io)

    def execute(self, io: str):

        self.change_command(io)
        if self._sanitize_command(io) == self.__list:
            return

        if self.is_list_command():
            self._add_elements(io)
            return

        if self.is_change_directory():
            self._change_directory(self.current_command)
            return

    def is_list_command(self):
        return self.current_command == self.__list

    def is_change_directory(self):
        return self.current_command.startswith(self.__change_directory)

    def _is_cmd_command(self, command: str):
        return command.startswith('$')

    def _add_elements(self, io: str):
        """
        Add files and directories while listing 'ls'

        :param io:
        :return:
        """
        add_dir(io, self.current_dir) if io.startswith('dir') else add_file(io, self.current_dir)

    def _change_directory(self, io: str):
        _, direction = io.split(' ')
        """
        Recognize direction 
        :param io:
        :return:
        """

        # direction it's a dir name
        if direction != '..':
            self.current_dir = self.current_dir.find(direction)

        if direction == '..':
            self.current_dir = self.current_dir.parent


data = ['$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e',
        '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls',
        '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']
cmd = CommandProcessor()
cmd.execute_commands(data)


def count_less_than(dir, sum):

    if dir is None:
        return sum

    print(dir.name, dir.size)
    sum += dir.size

    if isinstance(dir, Dir):

        if len(dir.children) == 0:
            return sum

        for i in dir.children:
            count_less_than(i, sum)


sum = count_less_than(cmd.main_dir, 0)

print(sum)
def print_elements(el, nested):
    nested += "\t"
    if isinstance(el, Dir):
        for i in el.children:
            print(nested, str(i), i.name, i.size)
            print_elements(i, nested)


print_elements(cmd.main_dir, "")
