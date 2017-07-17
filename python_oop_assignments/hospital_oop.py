#Hospital OOP Assignment

class Patient(object):

    def __init__(self, id_no,name, allergies, bed):
        bed = "none"
        self.bed = bed
        self.patient = [id_no,
                        name,
                        allergies,
                        bed]

#show_patient function is to see the patients
    def show_patient(self):
        print self.patient

#-------------------------------------------------

class Hospital(Patient):

    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.info = [hospital_name, capacity]
        self.capacity = capacity
        self.count = 0
        self.hospital_name = hospital_name

#hospital_info is to see the hospital general information
    def hospital_info(self):
        print self.info
        print self.patients

#add will add a patient to the list of patients, assign the patient a bed number, and print that the patient has been admitted
    def add(self,id_no,name, allergies, bed):
        super(Hospital, self).__init__(id_no,name, allergies, bed)
        self.bed_no = 1
        if len(self.patients) <= self.capacity:
            for i in range(len(self.patients)):
                if self.patients[i][3] != self.bed_no:
                    continue
                elif self.patients[i][3] == self.bed_no:
                    self.bed_no += 1
#The above is able to account for when a bed becomes open, but is unable to recognize if the bed after it is occupied...

            self.patient[3] = self.bed_no
            self.patients.append(self.patient)
            print self.patient[1], "has been admitted to", self.hospital_name, "and is in bed no.", self.patient[3]
        elif len(self.patients) > self.capacity:
            print "Hospital at capacity. Cannot complete admission."

#discharge will get rid of the patient from the list, change bed status to none, and print that the patient has been discharged
    def discharge(self,patient_id):
        for i in range(len(self.patients)-1):
            if self.patients[i][0] == patient_id:
                print self.patients[i][1], "has been discharged from bed no.", self.patients[i][3]
                self.patients[i][3] = "none"
                self.patients.pop(i)



suburban = Hospital("Suburban Hospital", 100)
suburban.add(1, "John", "Penicillin", "none")
suburban.add(2, "Tom", "Peanuts", "none")
suburban.add(3, "Isaac", "Bee stings", "none")
suburban.add(4, "Yasmeen", "No Allergies", "none")
suburban.discharge(2)
suburban.add(5, "Nancy", "Latex", "none")
suburban.add(6, "Alex", "Dust", "none")
suburban.hospital_info()
