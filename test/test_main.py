from src.main import hello_world
import unittest


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertNotEqual(hello_world().find('Red'), -1)

if __name__ == '__main__':
    unittest.main()