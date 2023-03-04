# discover -s  tests -p "*_test.py"
# find all test which consist with word_test.py

# in folder tests

# from unittest import TestCase, main
# from main import square
#
# class MathAction(TestCase):
#
#     def test_square_number(self):
#         self.assertEqual(square(3), 9)
#
# if __name__=="__main__":
#     main()

# where our test class must inherit from class TestCase , function main() start tests


# -------------------------             pylint          -----------------
# pylint --generate-rcfile >.pylintrc      for settings pylint

#  coverage run --source=app -m pytest tests/