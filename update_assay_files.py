from configparser import ConfigParser
from datetime import datetime
from pathlib import Path
from shutil import copy2, move, rmtree
from typing import List, Callable, Any

# icon from https://iconarchive.com/show/farm-fresh-icons-by-fatcow/update-icon.html


def _check_path_exists(path: str) -> None:
    """
    Checks if a path exists or not.
    
    For more details see doc/functions/check_path_exists.md
    """
    if not Path(path).exists():
        raise Exception(f'Path "{path}" does not exist.')
    return None


def _create_if_not_exist(path: str) -> None:
    """
    Creates folder specified in path.

    For more details see ./doc/functions/create_folder_if_not_exist.md
    """
    p = Path(path)
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
    return None


def _find_files_down_path(path: str) -> List["File"]:
    """
    Returns list of files at specified path and in sub-folders.

    """
    files = [File(str(p), str(path)) for p in Path(path).rglob("*") if p.is_file()]
    return files


def _log_exception(log: "Log", operation: Callable, *args: Any) -> None:
    """
    Executes operation with arguments and sends error messages to log.

    For more details see ./doc/functions/log_exception.md"""
    try:
        operation(*args)
    except:
        error_msg = f'could not copy "{args[0]}" to "{args[1]}"'
        log.add(error_msg)
    return None


def exit_program() -> None:
    input('enter any key to exit\n')
    return None


class BackupFolderNameFactory:
    """
    Handles generation of folder name for backup folder and its path.

    For more details see ./doc/classes/BackupFolderNameFactory.md
    """
    version = 1
    date_str = datetime.today().strftime("%Y_%m_%d")

    @property
    def folder_name(cls) -> str:
        """Concatinates version and date_str as `str` and returns it."""
        return f"{cls.date_str}_v{cls.version}"

    def make(self, backup_root: str) -> str:
        """
        Returns path to backup folder.

        For more details see doc/functions/BackupFolderNameFactory - make.md"""
        path = Path(backup_root).joinpath("Backups", self.folder_name)
        while path.exists():
            self.version += 1
            path = Path(backup_root).joinpath("Backups", self.folder_name)
        return str(path.relative_to(backup_root))


class File:
    def __init__(self, path: str, root: str) -> None:
        _check_path_exists(path)
        _check_path_exists(root)
        self.path = path
        self.root = root
        return None

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return f'File({self.path})'

    def move(self, destination: str, log: "Log") -> None:
        """
        Moves file to destination if path to destination exists, else raises Exception

        For more detail see doc/functions/File - move.md
        """
        _create_if_not_exist(destination)
        
        relative_path = Path(self.path).relative_to(Path(self.root))
        full_destination_path = Path(destination).joinpath(relative_path)
        
        full_destination_path.parent.mkdir(parents=True, exist_ok=True)
        _log_exception(log, move, self.path, full_destination_path)
        return None

    def copy(self, destination: str, log: "Log") -> None:
        """
        Like move but copies file instead.

        For more detail see doc/functions/File - copy.md"""
        _create_if_not_exist(destination)
        relative_path = Path(self.path).relative_to(Path(self.root))
        full_destination_path = Path(destination).joinpath(relative_path)
        full_destination_path.parent.mkdir(parents=True, exist_ok=True)
        
        _log_exception(log, copy2, self.path, full_destination_path)
        return None


class Folder:
    """
    Handles operations (move / copy) of folder structures.

    For more details see doc/classes/Folder.md
    """
    def __init__(self, path: str) -> None:
        _check_path_exists(path)
        self.path = path
        self.files = _find_files_down_path(path)
        return None

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return f'Folder({self.path})'

    @property
    def is_empty(self) -> bool:
        return not bool(_find_files_down_path(self.path))

    def _clean_folder_structure(self, path: str) -> None:
        _check_path_exists(path)
        rmtree(path)
        Path(self.path).mkdir(parents=True, exist_ok=True)
        return None

    def move(self, destination: str, log: "Log") -> None:
        """
        Moves file in self.files to destination path.

        For more detail see doc/functions/Folder - move.md
        """
        for file in self.files:
            file.move(destination, log)
        self._clean_folder_structure(self.path)
        return None

    def copy(self, destination: str, log: "Log") -> None:
        """
        Copies file in self.files to destination path.

        For more detail see doc/functions/Folder - copy.md
        """
        for file in self.files:
            file.copy(destination, log)
        return None


class Log:
    """
    Stores paths which raised Exception during move or copy operation.

    For more details see doc/classes/Log.md
    """
    def __init__(self) -> None:
        self.log_list = list()
        return None

    @property
    def log_msg(self) -> str:
        return "\t\n".join(self.log_list)

    def add(self, path: str) -> None:
        self.log_list.append(path)
        return None

    def print_log(self) -> None:
        if len(self.log_list) == 0:
            print("No Errors occured\n")
        else:
            print(self.log_msg)
        return None


class UpdateManager:
    """
    Creates backup of old assay files and updates to new version.

    For more detail see doc/classes/UpdateManager.md
    """
    update_log = Log()
    backup_log = Log()
    backup_folder_name_gen = BackupFolderNameFactory()

    def __init__(self, config_obj: ConfigParser) -> None:
        self.path_old_files = config_obj.get("Paths", "loc_files")
        self.path_backup = config_obj.get("Paths", "loc_backup")
        self.path_updates = config_obj.get("Paths", "loc_updates")

        self.old_files_folder = Folder(self.path_old_files)
        self.updates_folder = Folder(self.path_updates)

        _check_path_exists(self.path_backup)
        return None

    def backup_files(self) -> None:
        """uses instance of Folder class to move old assay files to backup location."""
        backup_folder_name = self.backup_folder_name_gen.make(self.path_backup)
        backup_to = Path(self.path_backup).joinpath(backup_folder_name)
        self.old_files_folder.move(str(backup_to), self.backup_log)
        print('Backup old files.')
        self.backup_log.print_log()
        return None

    def update_files(self) -> None:
        """uses instnace of Folder class to copy new assay files to where old assay files were located."""
        self.updates_folder.copy(self.path_old_files, self.update_log)
        print('Updating assay files.')
        self.backup_log.print_log()
        return None

    def run(self) -> None:
        """combines backup_file() and update_files()."""
        if self.updates_folder.is_empty:
            print('No Updates available.')
        elif self.old_files_folder.is_empty:
            self.update_files()
        else:
            self.backup_files()
            self.update_files()

        print('Done')
        return None


if __name__ == "__main__":
    config_path = Path("./config.ini")
    if config_path.exists():
        config = ConfigParser()
        config.read(config_path)

        manager = UpdateManager(config)
        manager.run()
    else:
        print(f'path to configuration file "{config_path}" does not exist \n')

    exit_program()