import requests
import yaml

class GlobalDictClass():
    def __init__(self):
        self.dict = {}

    def set(self, key, value):
        self.dict[key] = value

    def add_dict(self, new_dict):
        self.dict.update(new_dict)


    def get(self, key):
        if key not in self.dict:
            return None
        return self.dict[key]




class UrlConstants:

    def __init__(self):
        self.PREFIX = "http://localhost:8081"

        self.REGISTER_URL = self.PREFIX + "/user/register"

        self.LOGIN_URL = self.PREFIX + "/user/login"

        self.PATIENT_URL = self.PREFIX + "/patient"


        self.ALL_PATIENT_URL = self.PREFIX + "/patient/getAllPatient"

        self.SCAN_GET_BY_PatientID_URL = self.PREFIX + "/scan/getByPatientId"

        self.SCAN_URL = self.PREFIX + "/scan"

        self.SCAN_UPDATE_WITH_FILE_URL = self.PREFIX + "/scan/updateWithFile"

        self.SCAN_INFO_WITH_URL_URL = self.PREFIX + "/scan/getInfoAndUrl"



    def update_prefix(self, prefix):
        for key in self.__dict__.keys():
            if key.endswith("_URL"):
                self.__dict__[key] = prefix + self.__dict__[key][len(self.PREFIX):]

        self.PREFIX = prefix




urlConstants = UrlConstants()
GlobalDict = GlobalDictClass()
Session = requests.Session()