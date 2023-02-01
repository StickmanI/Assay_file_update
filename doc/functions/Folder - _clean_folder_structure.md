# General
- Removes folder, sub folders and files specified by path


# Arguments
- path: `str`


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