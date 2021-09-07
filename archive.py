import os
import zipfile

def archive_dir(dir_path: str, output_archive_path: str):
    with zipfile.ZipFile(output_archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
    for root, _, files in os.walk(dir_path):
        for file in files:
            archive.write(os.path.join(root, file))