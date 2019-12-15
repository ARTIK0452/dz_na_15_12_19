class HomeLibrary:
     
    def __init__(self):
        self.bookshelf = []
 
    def home_add(self, data):
        data = data.split()
        self.bookshelf.append(data)
 
    def search_author(self, author):
        for data in self.bookshelf:
            if ' '.join(data[:2]) == author:
                return ' '.join(data)
 
    def search_year(self, year):
        for data in self.bookshelf:
            if data[3].split(':')[1].strip() == year:
                return ' '.join(data)

    def search_janr(self, janr):
        for data in self.bookshelf:
            if data[3].split(':')[1].strip() == janr:
                return ' '.join(data)

if __name__ == '__main__':
 
    data = '''Мишель Ульбэк "Серотонин" год: 1999 жанр: роман
                Тамара Габриель "Уроборос" год: 2002 жанр:киберпанк
                Владимир Кощеев "Ультиматум" год: 1956 жанр:фантастика'''
 
    home = HomeLibrary()
    for line in data.split('\n'):
        home.home_add(line)
 
    print(home.search_author('Мишель Ульбэк'))
    #print(home.search_janr('фантастика'))