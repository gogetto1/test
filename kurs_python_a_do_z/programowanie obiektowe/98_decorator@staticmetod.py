class Student:
    lista_studentów = []

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentów.append(self)

    @staticmethod
    def liczba_studentow():
        print("liczba studentów:", len(Student.lista_studentów))


student_1 = Student('Jan', 'Kowlki', 18)
student_2 = Student('Marek', 'Nowacki', 23)
student_3 = Student('Wieslaw', 'Paleta', 41)

Student.liczba_studentow()
