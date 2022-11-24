
class Films():
    def __init__(self, title, year, type, repeated):
        self.title = title
        self.year = year
        self.type = type
        self.repeated = repeated
    
    def __str__(self):
        return f"{self.title} {self.year} {self.repeated}"

    def play(self):
        self.repeated += 1 



class Serials(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def serial(self):
        return f"{self.title} {self.year} {self.repeated} {self.episode} {self.season}"


film = Films(title='Bond', year=2020, type='Dramat', repeated=7)

serial = Serials(title='Bond', year=2020, type='Dramat', repeated=7, episode='E02', season='S01')
print(serial.serial())
serial.play()
print(serial.repeated)