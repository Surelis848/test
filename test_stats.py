# import the test program we're created
from stats import StatsList

# import unit-test
import unittest


class TestValidInputs(unittest.TestCase):

    def setUp(self):
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    # END setUp

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)
        self.stats.append(3)
        self.assertEqual(self.stats.mean(), 2.5)
        self.stats.append(2)
        self.assertEqual(self.stats.mean(), 2.5)
    # END test_mean

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)
        self.stats.append(3)
        self.assertEqual(self.stats.median(), 3)

    # END test_median

    def test_mode(self):
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])
        self.stats.append(3)
        self.assertEqual(self.stats.mode(), [3])

    def test_smallest(self):
        self.assertEqual(self.stats.smallest(), [1])
    # END test_mode


if __name__ == "__main__":
    unittest.main()