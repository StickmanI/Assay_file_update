# General
- Returns path to backup folder
- Generates name for backup folder that does not exist
  - if "2023_01_01_v1" exists creates "2023_01_01_v2"


# Arguments
- backup_root: `str`
  - path as to folder where Backup folder should be created


# Return
- path of backup_root/Backups/backup_folder_name as `str`


# Example
```py
>>> import pathlib
>>> pathlib.Path('.').rglob('*')
# []

>>> factory = BackupFolderNameFactory()
>>> factory.make('./root')
>>> pathlib.Path('.').rglob('*')
# ['root/Backups/2012_01_01_v1']
```