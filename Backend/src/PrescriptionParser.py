import re

from  Backend.src.geniric_parser import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
    def parse(self):
        return {
            'patient_name':self.get_field('patient_name'),
            'patient_address':self.get_field('patient_address'),
            'patient_medicines':self.get_field('patient_medicines'),
            'patient_directions':self.get_field('patient_directions'),
            'patient_getRefill':self.get_field('patient_getRefill')
        }
    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    # def get_address(self):
    #     pattern = 'Address:(.*)\n'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    # def get_medicines(self):
    #     pattern = 'Address[^\n](.*)Directions'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match) > 0:
    #         return match[0].strip()
    # def get_Directions(self):
    #     pattern = 'Directions:(.*)Refill'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match) > 0:
    #         return match[0].strip()
    # def get_Refill(self):
    #     pattern = 'Refill:(.*)times'
    #     match = re.findall(pattern, self.text)
    #     if len(match) > 0:
    #         return match[0].strip()
    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'patient_medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'patient_directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'patient_getRefill': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }
        patient_object = pattern_dict[field_name]
        match = re.findall(patient_object['pattern'], self.text, patient_object['flags'])
        if len(match) > 0:
            return match[0].strip()


if __name__ == '__main__':
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
    pp = PrescriptionParser(document_text)
    print(pp.parse())