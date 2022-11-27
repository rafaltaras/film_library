import random

class Film():
    def __init__(self, title, year, type, repeated):
        self.title = title
        self.year = year
        self.type = type
        self.repeated = repeated
    
    def __str__(self):
        return f"{self.title} {self.year}"

    def __repr__(self):
        return f"{self.title} {self.year}"

    def play(self):
        self.repeated += 1 

class Serial(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.episode}E{self.season}"


class MoveDatadase():
    def __init__(self):
        self.movie_database = []

    def insert(self, entry): 
      self.movie_database.append(entry)

    def get_movies(self):
        films_list = []
        for movie in self.movie_database:
            if isinstance(movie, Serial) == False:
                films_list.append(movie)
        return films_list
        
    def get_serial(self):
        serials_list = []
        for serial in self.movie_database:
            if isinstance(serial, Serial) == True:
                serials_list.append(serial)
        return serials_list   

# Cos mi nie do końca działa ta funkcja
    def search(self, title):
        for entry in collection.movie_database:
            if entry.title == title:
                return entry

    def generate_views(self, quantity):
        x = 0
        while x < quantity:
            x += 1
            print(random.choice(self.movie_database))

    def top_titles(self, toptitle, quantity):
        self.toptitle = toptitle
        for i in range (0, quantity):
            if isinstance(toptitle, Serial) == True:
               print(f"Top film to: {toptitle}")
            else:
                print(f"Top serial to: {toptitle}")
                        
      

film = Film(title='Bond', year=2020, type='Dramat', repeated=7)
film1 = Film(title='Rocky', year=2020, type='Dramat', repeated=7)
serial = Serial(title='Gra o Tron', year=2011, type='Fantasy', repeated=7, episode=2, season=1)
serial1 = Serial(title='Narcos', year=2011, type='Fantasy', repeated=7, episode=2, season=1)

collection = MoveDatadase()
collection.insert(film)
collection.insert(film1)
collection.insert(serial)
collection.insert(serial1)
print('Baza filmów')
for i in collection.movie_database:
    print(i)

print('')
print("GET MOVIE")
y = collection.get_movies()
by_title = sorted(y, key=lambda movie: movie.title)
for i in by_title:
    print(i)

print('')
print("GET SERIALS")
y = collection.get_serial()
by_title = sorted(y, key=lambda movie: movie.title)
for i in by_title:
    print(i)

print('')
print("SEARCH")
entry = collection.search('Bond')
print(entry)

print('')
print("RANDOM CHOICE")
entry = collection.generate_views(10)
print(entry)

print('')
print("TOP TITLES")
(collection.top_titles('Gra o Tron', 5))




