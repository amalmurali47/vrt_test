#!/usr/bin/env python3
import unittest
import sys


def main():
    tests = unittest.defaultTestLoader.discover('tests')
    return unittest.TextTestRunner().run(tests)


if __name__ == '__main__':
    if not main().wasSuccessful():
        sys.exit(1)
