class Classes:
    def __init__(self, id, token):
        self.id = id
        self.token = token
        self.alive = 1
        self.muted = 0
        self.alibi = 0

    def slay(self):
        self.alive = 0

    def mute(self):
        self.muted = 0

    def night_comming(self):
        if self.alive:
            self.muted = 0


class Doctor(Classes):
    def __init__(self, id, token):
        super().__init__()
        self.heal_per_night = 0

    def info(self):
        return 'Doc'

    def heal(self, other=None):
        if self.heal_per_night == 1:
            if other == None:
                self.alive = 1
            else:
                other.alive = 1


class Mafia(Classes):
    def __init__(self, id, token):
        super().__init__()

    def info(self):
        return 'Mafia'

    def kill(self, other):
        return other


class Gangster(Mafia):
    def __init__(self, id, token):
        super().__init__()
        self.kill_per_night = 0

    def info(self):
        return 'Gangster'

    def kill(self, other):
        if self.kill_per_night == 1:
            other.alive = 0


class Deffka(Classes):
    def mutesomebody(self, id):
        id.mute = 1
        id.alibi = 1

    def info(self):
        return 'Deffka'


class Policeman(Classes):
    def info(self):
        return 'Policeman'
    def check(self, id):
        if id.info() == 'Gangster' or id.info() == 'Mafia':
            return True
        else:
            return False
