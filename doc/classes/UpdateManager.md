# General
- Creates backup of old assay files and updates to new version
- Manages moving old assay files to backup folder and copies new assay files to folder where old assay files were located
- makes use of Log (doc/classes/Log.md), BackupFolderNameFactory (doc/classes/BackupFolderNameFactory.md), Folder (doc/classes/Folder) and File (doc/classes/File.md)
- needs `configparser.ConfigParser` object for creating instance
  - has paths to location where old assay files, new assay files are stored and where to create the backup folder in 


# Class Attributes
- update_log: `Log`
  - stores paths of `File` objects which raised Exceptions during assay file updating
- backup_log: `Log`
  - like update_log for Exceptions raised during backup
- backup_foler_name_gen: `BackupFolderNameFactory`
  - generates backup folder and path
  - for backing up old assay files


# Methods
- backup_files(self) -> `None`
  - uses instance of `Folder` class to move old assay files to backup location
- update_files(self) -> `None`
  - uses instnace of `Folder` class to copy new assay files to where old assay files were located
- run(self) -> `None`
  - combines backup_file() and update_files()



# Example
```py
>>> from update_assay_files import UpdateManager
>>> config_path = Path("./config.ini")
>>> config = ConfigParser()
>>> config.read(config_path)
>>> manager = UpdateManager(config)
>>> manager.run()
```