from faker import Faker
fake = Faker()

class BaseInfo:
    def __init__(self, title, release_date, category, num_views):
        self.title = title
        self.release_date = release_date
        self.category = category
        self.num_views = num_views

    @property
    def Play(self):
        self.num_views += 1
        return self.num_views
    
    @Play.setter
    def Play(self,value):
        self.num_views += value
            
    def __str__(self):
        return f'{self.title} ({self.release_date})'

class Movie(BaseInfo):
    pass

class Series(BaseInfo):
    def __init__(self, num_odc, num_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_odc = num_odc
        self.num_season = num_season
    
    def __str__(self):
        if len(self.num_odc) == 1:
            self.num_odc = '0' + self.num_odc
        if len(self.num_season) == 1:
            self.num_season = '0' + self.num_season
        return f'{self.title} S{self.num_season}E{self.num_odc}'


Movies_n_Series = []

Movies_n_Series.append(Movie(title = 'Mroczne ścieżki', release_date = '20 marca 2023', category = 'Thriller, Mystery', num_views = 0))
Movies_n_Series.append(Series(title = 'Zaginione Opowieści', release_date = '20 lutego 2022', category = 'Fantasy, Przygodowy', num_views = 0, num_odc = '3', num_season = '1'))
Movies_n_Series.append(Movie(title = 'Miasto przyszłości', release_date = '5 lipca 2022', category = 'Sci-Fi, Akcja', num_views = 0))
Movies_n_Series.append(Series(title = 'Sekrety Rodziny', release_date = '28 września 2023', category = 'Dramat, Obyczajowy', num_views = 0, num_odc = '7', num_season = '1'))
Movies_n_Series.append(Movie(title = 'Sekrety przeszłości', release_date = '14 listopada 2021', category = 'Dramat, Historyczny', num_views = 0))
Movies_n_Series.append(Series(title = 'Miasto Cieni', release_date = '15 maja 2022', category = 'Thriller, Kryminał', num_views = 0, num_odc = '5', num_season = '1'))

def getMovie():
    print('--Filmy--')
    for movie in Movies_n_Series:
        if isinstance(movie, Movie) == True:
            print(movie)
def getSeries():
    print('--Seriale--')
    for movie in Movies_n_Series:
        if isinstance(movie, Movie) == False:
            print(movie)

def search():
    searching_again = True
    while searching_again:
        searching = input('Podaj nazwe filmu lub serialu: ')
        for movies_series in Movies_n_Series:
            if movies_series.title == searching:
                print(movies_series)
                break
            elif movies_series.title != searching and movies_series == Movies_n_Series[-1]:
                print('Film nie został znaleziony')
        searching_again = input('Czy chcesz kontynuowac T/N: ')
        if searching_again.upper()  == 'N':
            searching_again = False   

def generate_views():
    number = fake.random_int(1, 101)
    element = fake.random_int(0, len(Movies_n_Series) - 1)
    Movies_n_Series[element].Play = number

def auto_generate_views():
    for i in range(10):
        generate_views()

def top_titles(content_type):

    top_title = ('', 0)
    name = ''
    for element in Movies_n_Series:
        if isinstance(element, content_type) == True:
            top_title = (element.title, element.num_views)
    if content_type == Series:
        name = 'serial'
    else:
        name = 'film'
    print(f'Njabardziej ogladany {name} to {top_title}')
    

if __name__ == '__main__':

    '''getMovie()
    getSeries()
    search()'''
    auto_generate_views()
    while True:
        user = input('Wybierz czy chcesz zobaczyc najbardziej odwarzany film czy serial (S/M): ')
        if user.upper() == 'S':
            top_titles(Series)
        elif user.upper() == 'M':
            top_titles(Movie)
        else:
            print('Podana wartosc nie jest zgodna z kluczem, sprobuj jeszcze raz')
            continue
        user = input('Czy chcesz kopntynuowac? T/N: ')
        if user.upper() == 'N':
            break
