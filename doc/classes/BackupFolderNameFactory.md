# General
- Handles generation of folder name for backup folder and its path


# Class Attributes
- version: `int`
- date_str: `str`
  - date of today in YYYY_MM_DD format


# Methods
- make(self, backup_root: `str`) -> `str`
  - for details see doc/functions/BackupFolderNameFactory - make.md


# Properties
- folder_name(cls) -> `str`
  - Concatinates version and date_str as `str` and returns it
  - e.g. 2022_05_15_v10
