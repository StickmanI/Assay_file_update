# General
- Returns list of `File` objects at specified path and in sub-folders


# Arguments
- path: `str`
  - path as a string (UNIX or windows style does not matter)


# Return
- list of `File` objects
  - see ./doc/classes/File.md


# Example
```py
>>> import pathlib
>>> pathlib.Path('.').rglob('*')
# ['some/folder/', 'some_file.txt']

>>> _find_files_down_path('.')
# [File(some_file.txt)]
```