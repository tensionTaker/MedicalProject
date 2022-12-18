from Backend.src.PrescriptionParser import PrescriptionParser

import pytest

@pytest.fixture()
def doc1():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks -
    Lialda - take 2 pill everyday for 1 month
    Refill: 3 times
    '''
    return PrescriptionParser(document_text)

def test_doc1(doc1):
    assert doc1.parse() == {'patient_name': 'Marta Sharapova', 'patient_address': '9 tennis court, new Russia, DC',
                            'patient_medicines': 'Prednisone 20 mg\n    Lialda 2.4 gram',
                            'patient_directions': 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks -\n    Lialda - take 2 pill everyday for 1 month',
                            'patient_getRefill': '3'}
