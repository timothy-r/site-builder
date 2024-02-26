"""
    test module
"""
import unittest

from tests.linked_file_test import LinkedFileTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    runner.run(suite)