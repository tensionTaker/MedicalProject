import abc

class MedicalDocParser():
    def __init__(self,text1):
        self.text = text1

    @abc.abstractmethod
    def parse(self):
        pass