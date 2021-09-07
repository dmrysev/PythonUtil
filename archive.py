import os
from typing import Iterable
import zipfile

def archive_dir(dir_path: str, output_archive_path: str) -> None:
    with zipfile.ZipFile(output_archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, _, files in os.walk(dir_path):
            for file in files:
                archive.write(os.path.join(root, file))

def archive_files(file_paths: Iterable[str], output_archive_path: str) -> None:
    with zipfile.ZipFile(output_archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for file_path in file_paths:
            archive.write(file_path)

