#Написать класс Boa, который при инициализации принимает длину, высоту,
#ширину прямоугольного параллелепипеда. В классе определен метод,
#который считает сколько в данном объекте поместится прямоугольных
#параллелепипедов 2х2х2.


#a - lengbt - длинна
#h - beigbt - высота
#z - widtb - ширина
class Box():
    def __init__(self, a, b, h):
        self.length = a
        self.width = b
        self.height = h
        self.sm_length = 2
        self.sm_width = 2 
        self.sm_height = 2 

    def smalls_in_big(self):
        V = (self.length * self.width) * self.height
        v = (self.sm_length * self.sm_width) * self.sm_height
        return V/v
        

parallelepiped = Box(12, 6, 10)

print("В большом прямоугольном параллелепипеде (12, 6, 10) \nпоместится ", parallelepiped.smalls_in_big(), "маленьких прямоугольных параллелепипедов (2, 2, 2)")
        

        