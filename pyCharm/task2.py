#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    stroka_1 = set(input("Введите первую строку: "))
    stroka_2 = set(input("Введите вторую строку: "))

    obshie_simvoly = stroka_1.intersection(stroka_2)

    print(f"Общие символы: {obshie_simvoly}")