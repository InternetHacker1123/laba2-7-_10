#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    inp = input("Введите строку: ")
    glasnye = {'у', 'е', 'ы', 'а',
            'о', 'э', 'я', 'и', 'ю', 
            'e','y','u','i','o','a',}
    
    cnt = 0

    for b in inp:
        if b.lower() in glasnye:
            cnt += 1
    
    print(f"Количество гласных букв в строке: {cnt}")