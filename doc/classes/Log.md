# General
- Stores paths which raised Exception during move or copy operation

# Class Attributes
- log_list: `List[str]`


# Methods
- add(self, path: `str`) -> None
  - adds path to self.log_list
- print_log(self) -> None
  - prints concatinated `str` containing paths which raised Exceptions


# Properties
- log_msg -> `str`
  - formated `str` containing Exceptions



# Example
```py
>>> from update_assay_files import Log
>>> l = Log()
>>> l.print_log()
# No Errors occured

>>> l.add('path/unable/to/copy')
>>> l.add('path/with_error')
>>> l.print_log()
#     path/unable/to/copy
#     path/with_error
```