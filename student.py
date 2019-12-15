class Student():
    def __init__(self):
        self.student_dict = {}

    def add(self, key, value):
         self.student_dict[key] = value

    def get(self):
        return self.student_dict

    #def sort(self):
        
            



new = Student()
new.add(1, ['Аумбочкин А.А.', '123', 2, 3, 2, 3])
new.add(2, ['Бумбочкин А.А.', '23', 4, 5, 5, 4])
new.add(3, ['Вумбочкин А.А.', '13', 3, 3, 3, 3])
new.add(4, ['Гумбочкин А.А.', '3', 5, 5, 5, 5])
new.add(5, ['Думбочкин А.А.', '123', 2, 2, 2, 2])
new.add(6, ['Еумбочкин А.А.', '23', 2, 3, 2, 3])
new.add(7, ['Ёумбочкин А.А.', '13', 3, 3, 2, 2])
new.add(8, ['Хумбочкин А.А.', '3', 3, 2, 2, 3])
new.add(9, ['Шумбочкин А.А.', '13', 5, 5, 4, 4])
new.add(10, ['Тумбочкин А.А.', '3', 4, 4, 5, 5])
st_dict = new.get()
for k, v in st_dict.items():
    if v[2] and v[3] and v[4] and v[5] >= 4:
        print(*v[:2])


