import unittest
import liststuff

class ListStuffTest(unittest.TestCase):
    def test_make_backwards_odd(self) -> None:
        nums = [1, 2, 3, 4, 5]
        self.assertEqual([1, 2, 3, 4, 5], nums)
        liststuff.make_backwards(nums)
        self.assertEqual([5, 3, 4, 2, 1], nums)

    def test_sort_1(self) -> None:
        nums = [45, 2, 0, 100, 15]
        self.assertEqual([45, 2, 0, 100, 15], nums)
        liststuff.selectsort(nums)
        self.assertEqual([0, 2, 15, 45, 100], nums)


if __name__ == '__main__':
    unittest.main()