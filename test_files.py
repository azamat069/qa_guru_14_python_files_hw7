from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook
import csv
from paths_file import *


def test_csv_file():
    with ZipFile(ARCHIVE_FILE, 'r') as zip_file:
        with zip_file.open('month.csv', 'r') as file:
            csv_file = file.read().decode(encoding='utf-8')
            content = list(csv.reader(csv_file.splitlines(), delimiter=';'))
            first_row = content[0]
            assert 'Name,Abbreviation,Numeric,Numeric-2' in first_row
            print('test csv finished')


def test_xlsx_file():
    with ZipFile(ARCHIVE_FILE, 'r') as zip_file:
        with zip_file.open('import_empl_xlsx.xlsx', 'r') as file:
            workbook = load_workbook(file).active
            assert workbook['B2'].value == 'Иванова'
            assert workbook['G6'].value == 'ekalashnikov@company.ru'
            print('test xlsx finished')


def test_pdf_file():
    with ZipFile(ARCHIVE_FILE, 'r') as zip_file:
        with zip_file.open('test_pdf_file.pdf', 'r') as file:
            reader = PdfReader(file)
            assert len(reader.pages) == 1
            assert 'Тестовый PDF-документ' in reader.pages[0].extract_text()
