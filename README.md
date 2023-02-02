# Description
A tool which automates the backing up of old files and updating to new ones. It moves old files to a backup folder and copies new files to the location where the old files were stored.

# Requirements
- a config.ini file with paths named
  - loc_files
  - loc_backup
  - loc_updates

# Execution control
- done in the `UpdateManager.run()` method
- folder at loc_files and loc_updates not empty --> does backup old files + copies new files
- folder at loc_files empty --> only copies new files (no backup done)
- folder at loc_updates empty --> prints message "No Updates available" and does no backup and/or updating

# How it works
- `UpdateManager` creates `Folder`-objects with the `loc_files` and `loc_updates` paths provided in `config.ini`
- each `Folder`-object creates `File`-objects for all paths leading to files that are in the folder or sub folders of the `Folder`-objects path
- `UpdateManager` calls move or copy methods of the `Folder`-objects
- `Folder`-objects then call move or copy on all the `File`-objects stored in the `Folder`-object
- `File`-objects take care of moving and copying the files and creating parent folders (if they don't exist)