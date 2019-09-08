#!/usr/bin/env python3

# Импортируем системную библиотеку Python.
# Она используется для загрузки файла 'index.html' с сервера.
import urllib.request

# Эта переменная содержит запрос к 'http://localhost:1234/'.
# localhost указывает на то, что программа работает с локальным сервером.
fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' соответствует закодированному ответу сервера ('index.html').
# 'decodedContent' соответствует раскодированному ответу сервера (тут будет то, что мы хотим вывести на экран).
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Выводим содержимое файла, полученного с сервера ('index.html').
print(decodedContent)

# Закрываем соединение с сервером.
fp.close()
