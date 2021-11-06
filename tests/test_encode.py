#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/11/30 23:29
# FileName: test_encode.py

import pytest


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_mm(name):
    print(name)
