# General
- Copies files in self.files to destination path
- calls copy method on each File object in self.files


# Arguments
- destination: `str`
  - path to folder to where this File should be moved
- log: `Log`
  - catches raised Exceptions and stores them


# Return
- None


# Example
```py
>>> import pathlib
>>> pathlib.Path('.').rglob('*')
# ['folder\file.txt', 'folder\second_folder\with_file.txt']

>>> from update_assay_files import Log
>>> f = Folder('folder', root='.')
>>> f.copy(destination='other_folder', log=Log())
>>> pathlib.Path('.').rglob('*')
# ['folder\file.txt', 'folder\second_folder\with_file.txt', 'other_folder\file.txt', 'other_folder\second_folder\with_file.txt']
```