# General
- Handles operations (move / copy) of folder structures
- on instance creation
  - checks if path exists, if not existing raises Exception


# Class Attributes
- path: `str`
  - path to folder as `str`
- files: `List[File]`
  - storage for File objects (doc/classes/File.md)


# Methods
- move(self, destination: `str`, log: `Log`) -> None
  - calls move on each File object stored in self.files
  - also passes arguments along to move method of File object
- copy(self, destination: `str`, log: `Log`) -> None
  - calls copy on each File object stored in self.files
  - also passes arguments along to move method of File object
- _clean_folder_structure(self, path: `str`) -> None
  - removes all folder and files in path and in sub folders


# Properties
- is_empty -> bool
  - do files exist in this folder or sub folders



# Example
```py
>>> Folder(path='path/to/not/existing/folder')
# Traceback (most recent call last):
# ...
# Exception: Path "path/to/not/existing/folder" does not exist.

>>> f = Folder(path='path/to/existing/folder')
>>> f
# Folder(path='path/to/existing/folder')
```