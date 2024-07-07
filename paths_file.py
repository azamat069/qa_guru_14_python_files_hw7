import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
RESOURCE_DIR = os.path.join(CURRENT_DIR, "resource")
FILES_DIR = os.path.join(CURRENT_DIR, 'files')
ARCHIVE_FILE = os.path.join(RESOURCE_DIR, 'archive.zip')
