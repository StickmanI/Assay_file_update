# General
- Creates folder or file specified in path
- Also creates parent folders if they do not exist


# Arguments
- path: `str`
  - path as a string (UNIX or windows style does not matter)
  - can be path to a file or a folder
  - silently overrides file or folder (last part of path)


# Return
- returns `None`


# Example
```py
>>> from pathlib import Path
>>> Path('.').rglob('*')
# []

>>> _create_if_not_exist('some/file.txt')
>>> Path('.').rglob('*')
# ['some/file.txt']
```