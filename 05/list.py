#!/usr/bin/env python
# -*- coding: utf-8 -*-

from benchmarker import Benchmarker
from collections import deque
from  array import array

def main():

    times = 1000000
    original = [i for i in range(10000)]

    with Benchmarker(times, width=20)as bm:
        a = list(original)
        b = array('i', original)
        c = deque(original)

        @bm('list')
        def _(bench):
            for i in bench:
                a.insert(0, 1)
                a.pop()

        @bm('array')
        def _(bench):
            for i in bench:
                b.insert(0, 1)
                b.pop()

        @bm('deque')
        def _(bench):
            for i in bench:
                c.append(1)
                c.popleft()

if __name__ == '__main__':
    main()
