# General
- Handles operations on files (copy and move).
- raises Exception on instance creation if path to file is not existing


# Class Attributes
- path: `str`
  - path to file as `str`
- root: `str`
  - root path, needed to create path to file in new directory (for copy or move)


# Methods
- move(self, destination: `str`, log: `Log`) -> None
  - Moves file to destination if path to destination exists, else raises Exception
- copy(self, destination: `str`, log: `Log`) -> None
  - Like move but copies file instead




# Example
```py
>>> File(path='path/to/not/existing/file.txt', root='.')
# Traceback (most recent call last):
# ...
# Exception: Path "./test.txtpath/to/not/existing/file.txt" does not exist.

>>> f = File(path='./existing_file.txt', root='.')
>>> f
# File('./existing_file.txt')
```