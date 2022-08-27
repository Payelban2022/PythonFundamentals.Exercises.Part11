import enum,uuid


class AliveStatus(enum.Enum):
    Alive = 1
    Deceased = 0

class ZipCodeTrack(enum.Enum):
    JAVA = 0
    DATA = 1


class Person():
    def __init__(self,fname, lname, date_of_birth, alive: AliveStatus):
        self.first_name = fname
        self.last_name = lname
        self.dateofbirth = date_of_birth
        self.alive = alive

    def __str__(self):
        return (f"{self.first_name},{self.last_name},{self.dateofbirth},{self.alive}")
# Person1 = Person("Payel","Banerjee","01-12-1987","Alive")
# print(Person1)

    def update_first_name(self, new_fname):
        self.first_name = new_fname

    def update_last_name(self, new_lname):
        self.last_name = new_lname

    def update_dateofbirth(self,new_date_of_birth):
        self.dateofbirth = new_date_of_birth



