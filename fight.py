'''
Fight class to represent a single boxing fight.
'''
class Fight:
    def __init__(self, fight_id, fighter1, fighter2):
        self.fight_id = fight_id
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.outcome = None
    def set_outcome(self, outcome):
        self.outcome = outcome
    def get_outcome(self):
        return self.outcome