# General
- copies file to destination path
- also creates folder if the folder specified in destination does not exist (also applies to folders further up the destination path)


# Arguments
- destination: `str`
  - path to folder to where this File should be copied
- log: `Log`
  - catches raised Exceptions and stores them


# Return
- None


# Example
```py
>>> import pathlib
>>> pathlib.Path('.').rglob('*')
# ['folder\file.txt']

>>> from update_assay_files import Log
>>> f = File('folder\file.txt', root='.')
>>> f.copy(destination='other_folder', log=Log())
>>> pathlib.Path('.').rglob('*')
# ['folder\file.txt', 'other_folder\file.txt']
```