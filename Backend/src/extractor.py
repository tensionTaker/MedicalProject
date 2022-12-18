import pytesseract
import utility
from pdf2image import convert_from_path

from Backend.src.PrescriptionParser import PrescriptionParser
from Backend.src.PatientDetailParser import PatientDetails


POPPLER_PATH = r'c:\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'


def extractor(file_path, file_type):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    textDocument=''
    for page in pages:
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        textDocument = '\n' + text
        break
    if  file_type == 'medicalPrescription':
         pp = PrescriptionParser(textDocument)
         return pp.parse()
    elif file_type == 'medicalDetails':
         pp = PatientDetails(textDocument)
         return pp.parse()
    else:
        raise Exception(f"Invalid file format")

if __name__ == '__main__':
    extract = extractor('../resources/medicalPrescription/pre_2.pdf','medicalprescription')
    print(extract)

