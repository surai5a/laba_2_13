#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mod1 import func1


if __name__ == "__main__":
    a = int(input("a? "))
    b = int(input("b? "))
    test = func1(a, b)
    print(test())
