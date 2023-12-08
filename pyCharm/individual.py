#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    A = {'a', 'e', 'f', 'i'}
    B = {'a', 'b', 'k', 'n'}
    C = {'e', 'f', 'n', 'o', 'w', 'x'}
    D = {'a', 'd', 'e', 'o', 'p', 't', 'u'}

    an = u.difference(A)
    bn = u.difference(B)

    x = (A.union(B)).intersection(C)
    y = (an.intersection(bn).difference(C.union(D)))

    print(x)
    print(y)