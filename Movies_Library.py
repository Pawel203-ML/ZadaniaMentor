class BaseInfo:
    def __init__(self, title, release_date, category, num_views):
        self.title = title
        self.release_date = release_date
        self.category = category
        self.num_views = num_views

    def Play(self):
        self.num_views += 1
        return f'Liczba wyswietlen: {self.num_views}'
    
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
        if int(self.num_odc) // 10 < 1:
            self.num_odc = '0' + self.num_odc
        if int(self.num_season) // 10 < 1:
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
    for movie in Movies_n_Series:
        if isinstance(movie, Movie) == True:
            print(movie)
    print('----')
def getSeries():
    for movie in Movies_n_Series:
        if isinstance(movie, Movie) == False:
            print(movie)
    print('----')


if __name__ == '__main__':

    for movie in Movies_n_Series:
        movie.Play()
    print('----')

    getMovie()
    getSeries()