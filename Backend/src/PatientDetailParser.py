import re

from Backend.src.geniric_parser import MedicalDocParser

class PatientDetails(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self, text)
    def parse(self):
        return {
            'patient_name':self.get_field('patient_name'),
            'patient_phNumber':self.get_field('patient_phNumber'),
            'patient_hepatitisStatus':self.get_field('patient_hepatitisStatus'),
            'patient_medicalHistory':self.get_field('patient_medicalHistory')

        }
    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Patient Information Birth Date(.*)(January|February|March|April|May|June|July|August|September|October|November|December)', 'flags': re.DOTALL},
            'patient_phNumber': {'pattern': 'Patient Information.*(\(\d{3}\) \d{3}-\d{4}) Weight', 'flags': re.DOTALL},
            'patient_hepatitisStatus': {'pattern': 'Have you had the Hepatitis B vaccination\?(.*)List', 'flags': re.DOTALL},
            'patient_medicalHistory': {'pattern': 'List any Medical Problems.*:(.*)\n', 'flags': re.DOTALL},
        }
        patient_object = pattern_dict[field_name]
        match = re.search(patient_object['pattern'], self.text, patient_object['flags'])
        return match.groups()[0].strip()

if __name__ == '__main__':
    doctext = '''47/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Case of Emergency
m _ eee ee
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History

Chicken Pox (Varicella):

IMMUNE IMMUNE
Have you had the Hepatitis B vaccination?

No
List any Medical Problems (asthma, seizures, headaches):

Migraine
'''
    doctext1 = '''Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

- eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A


7?
v

17/12/2020'''
    pp = PatientDetails(doctext1)
    print(pp.parse())
