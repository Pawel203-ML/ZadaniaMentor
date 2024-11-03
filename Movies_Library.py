class BaseInfo:
    def __init__(self, title, release_date, category, num_views):
        self.title = title
        self.release_date = release_date
        self.category = category
        self.num_views = num_views

    def Play(self):
        self.num_views += 1
        return self.num_views

class Movie(BaseInfo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
    
    def __str__(self):
        return f'{self.title} ({self.release_date})'

class Series(BaseInfo):
    def __init__(self, num_odc, num_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_odc = num_odc
        self.num_season = num_season
    
    def __str__(self):
        if self.num_odc // 10 < 1:
            self.num_odc = '0' + self.num_odc
        if self.num_season // 10 < 1:
            self.num_season = '0' + self.num_season
        return f'{self.title} S{self.num_season}E{self.num_odc}'


Movies_n_Series = []