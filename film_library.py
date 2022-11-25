import random

class Films():
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

class Serials(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.episode}E{self.season}"


class Move_Datadase():
    def __init__(self):
        self.movie_database = []

    def database(self,film_serial): 
        self.movie_database.append(film_serial)

    def get_movies(self):
        films_list = []
        for movie in self.movie_database:
            if isinstance(movie, Serials) == False:
                films_list.append(movie)
        return films_list
        
    def get_serial(self):
        serials_list = []
        for serial in self.movie_database:
            if isinstance(serial, Serials) == True:
                serials_list.append(serial)
        return serials_list   

# Cos mi nie do końca działa ta funkcja
    def search(self, title):
        self.title = title
        if self.title == self.movie_database:
            print (f'Pozycja {self.title} w kolekcji')
        else:
            print (f'Pozycji {self.title} brak w kolekcji')

    def generate_views(self, quantity):
        x = 0
        while x < quantity:
            x += 1
            print(random.choice(self.movie_database))

    def top_titles(self, toptitle, quantity):
        self.toptitle = toptitle
        for i in range (0, quantity):
            if isinstance(toptitle, Serials) == True:
               print(f"Top film to: {toptitle}")
            else:
                print(f"Top serial to: {toptitle}")
                        
      

film = Films(title='Bond', year=2020, type='Dramat', repeated=7)
film1 = Films(title='Rocky', year=2020, type='Dramat', repeated=7)
serial = Serials(title='Gra o Tron', year=2011, type='Fantasy', repeated=7, episode=2, season=1)
serial1 = Serials(title='Narcos', year=2011, type='Fantasy', repeated=7, episode=2, season=1)

collection = Move_Datadase()
x = collection.database(film)
x = collection.database(film1)
x = collection.database(serial)
x = collection.database(serial1)
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
collection.search('Rocky')

print('')
print("RANDOM CHOICE")
collection.generate_views(10)

print('')
print("TOP TITLES")
(collection.top_titles('Gra o Tron', 5))




