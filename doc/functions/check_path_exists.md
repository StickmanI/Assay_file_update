# General
- checks if a path exists or not
- raises Exeption if path does not exist
  - therefor terminating program


# Arguments
- path: `str`
  - path as a string (UNIX or windows style does not matter)
  - can be path to a file or a folder


# Return
- returns `None`


# Example
```py
>>> p = r'path/to/some/file'
>>> _check_path_exists(path=p)
# Traceback (most recent call last):
# ...
# Exception: Path 'path\to\some\file' does not exist.

>>> p = r'path/to/existing/file'
>>> _check_path_exists(path=p)
# None
```