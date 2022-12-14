import unittest
import main
from day_7.utils import filter_size, filter_directories

class CommandProcessorTestCase(unittest.TestCase):

    def test_add_file(self):
        main_dir = main.Dir('/')
        main.add_file('111 a.txt', main_dir)

        self.assertIsInstance(main_dir.children[0], main.File)
        self.assertEqual('a.txt', main_dir.children[0].name)
        self.assertEqual(111, main_dir.children[0].size)

    def test_add_file_while_listing(self):
        cmd = main.CommandProcessor()
        cmd.execute_commands(['$ ls', '120 test.txt'])

        self.assertEqual(1, len(cmd.current_dir.children))
        self.assertEqual(120, cmd.current_dir.children[0].size)
        self.assertEqual('test.txt', cmd.current_dir.children[0].name)

    def test_change_directory(self):
        cmd = main.CommandProcessor()
        cmd.execute_commands(['$ ls', 'dir a', '$ cd a'])

        self.assertEqual('a', cmd.current_dir.name)

    def test_change_directory_and_ls_files(self):
        cmd = main.CommandProcessor()
        cmd.execute_commands(['$ ls', 'dir a', '$ cd a', '$ ls', '123 test.txt', '456 test2.txt'])

        self.assertEqual('a', cmd.current_dir.name)
        self.assertEqual(2, len(cmd.current_dir.children))

    def test_change_directory_and_back_to_main_dir(self):
        cmd = main.CommandProcessor()
        cmd.execute_commands(['$ ls', 'dir a', '$ cd a', '$ ls', '123 test.txt', '456 test2.txt', '$ cd ..'])

        self.assertEqual('/', cmd.current_dir.name)
        self.assertEqual(1, len(cmd.current_dir.children))

    def test_on_contest_test_data(self):
        data = ['$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e',
                '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls',
                '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']
        cmd = main.CommandProcessor()
        cmd.execute_commands(data)

        self.assertEqual('d', cmd.current_dir.name)
        self.assertEqual(4, len(cmd.current_dir.children))

    def test_on_contest_test_data_sum_dirs_size(self):
        data = ['$ ls', 'dir a', 'dir b', '$ cd a', '$ ls', '100 a.txt', '200 b.txt', '$ cd ..']
        cmd = main.CommandProcessor()
        cmd.execute_commands(data)

        dirs = []

        self.assertEqual(600, sum(filter_size(filter_directories(cmd.main_dir, dirs))))


if __name__ == '__main__':
    unittest.main()
