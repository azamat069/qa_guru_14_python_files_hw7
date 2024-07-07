import shutil
import time
import pytest
import os
from zipfile import ZipFile
from paths_file import *


@pytest.fixture(scope="session", autouse=True)
def preconditions():
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    files = ['month.csv', 'import_empl_xlsx.xlsx', 'test_pdf_file.pdf']
    zip_path = os.path.join(RESOURCE_DIR, 'archive.zip')
    with ZipFile(zip_path, 'a') as myzip:
        for i in files:
            file_path = os.path.join(FILES_DIR, i)
            myzip.write(file_path, os.path.basename(file_path))

    yield
    shutil.rmtree(RESOURCE_DIR)








