class Patient:

    def __init__(self, year, month, day, color, hour, release_reason):
        self.id = next(Patient.id)
        self.year = year
        self.month = month
        self.day = day
        self.color = color
        self.hour = hour
        self.release_reason = release_reason

    def id_patient():
        id = 0
        while True:
            yield id
            id+=1
    id = id_patient()

    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.id, self.year,
                                                   self.month, self.day,
                                                   self.color, self.hour,
                                                   self.release_reason)

class Report:

    def __init__(self):
        self.patients = []

    def __iter__(self):
        return iter(self.patients)

    def patients_by_color(self, color):
        return [p for p in self.patients if p.color == color]

class Reader:
    def file():
        with open("Report.txt","r") as file:
            for line in file:
                yield line

    line = file()

if __name__ == '__main__':

    reporte = Report()
    
    lines_read = 0
    while True:
        try:
            datos = next(Reader.line).split("\t")

        except StopIteration:
            print("End of file")
            break

        valores = ["year","month","day","color","hour","release_reason"]
        args = dict(zip(valores, datos))

        reporte.patients.append(Patient(**args))
        lines_read+=1

    print('{} lines read'.format(lines_read))

    for patient in reporte:
        print(patient)