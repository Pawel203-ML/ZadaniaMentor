from faker import Faker
fake = Faker()

from datetime import date
time = date.today()

Movies_n_Series = []
SeriesList = []

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

def getMovie(library):
    print('--Filmy--')
    for movie in library:
        if isinstance(movie, Movie) == True:
            print(movie)
def getSeries():
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
        if isinstance(element, content_type) == True and top_title[1] == 0:
            top_title = (element.title, element.num_views)
        elif isinstance(element, content_type) == True and element.num_views > top_title[1]:
            top_title = (element.title, element.num_views)
    return top_title
    
def  top_titles_inputUser():
    while True:
        user = input('Wybierz czy chcesz zobaczyc najbardziej odwarzany film czy serial (S/M): ')
        if user.upper() == 'S':
            print(f'Najpopularniejszy serial to {top_titles(Series)}')
        elif user.upper() == 'M':
            print(f'Najpopularniejszy film to {top_titles(Movie)}')
        else:
            print('Podana wartosc nie jest zgodna z kluczem, sprobuj jeszcze raz')
            continue
        user = input('Czy chcesz kontynuowac? T/N: ')
        if user.upper() == 'N':
            break

def AddingEpisodes(name, year, kind, num_episode, num_season, num_plays):
    #musi byc dodane odcinki dla kazdego serialu
    for i in range(1,int(num_season) + 1):
        for j in range(1,int(num_episode) + 1):
            SeriesList.append(Series(title = name, release_date = year, category = kind, num_views = num_plays, num_odc = str(j), num_season = str(i)))

def AddingEpisodesLaunching(library):
    for element in library:
        if isinstance(element, Series):
            AddingEpisodes(element.title, element.release_date, element.category, element.num_odc, element.num_season, 0)
    





if __name__ == '__main__':

    print('---Biblioteka filmow---')

    Movies_n_Series.append(Movie(title = 'Mroczne ścieżki', release_date = '20 marca 2023', category = 'Thriller, Mystery', num_views = 0))
    Movies_n_Series.append(Series(title = 'Zaginione Opowieści', release_date = '20 lutego 2022', category = 'Fantasy, Przygodowy', num_views = 0, num_odc = '15', num_season = '12'))
    Movies_n_Series.append(Movie(title = 'Miasto przyszłości', release_date = '5 lipca 2022', category = 'Sci-Fi, Akcja', num_views = 0))
    Movies_n_Series.append(Series(title = 'Sekrety Rodziny', release_date = '28 września 2023', category = 'Dramat, Obyczajowy', num_views = 0, num_odc = '8', num_season = '4'))
    Movies_n_Series.append(Movie(title = 'Sekrety przeszłości', release_date = '14 listopada 2021', category = 'Dramat, Historyczny', num_views = 0))
    Movies_n_Series.append(Series(title = 'Miasto Cieni', release_date = '15 maja 2022', category = 'Thriller, Kryminał', num_views = 0, num_odc = '28', num_season = '15'))

    auto_generate_views()
    print(f'Najpopularniejsze filmy i seriale dnia {time}: \n Film: {top_titles(Movie)} \n Serial: {top_titles(Series)}')
    sorted_elements = sorted(Movies_n_Series, key= lambda element: element.num_views)
    print('--Top 3--')
    print(sorted_elements[-1], '--', sorted_elements[-1].num_views)
    print(sorted_elements[-2], '--', sorted_elements[-2].num_views)
    print(sorted_elements[-3], '--', sorted_elements[-3].num_views)

    AddingEpisodesLaunching(Movies_n_Series)
    print('--Wybierz serial do obejrzenia--')
    
