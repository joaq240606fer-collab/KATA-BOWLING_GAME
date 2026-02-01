from src.scoreCard import ScoreCard
def __init__(self):
        self.score_card = None
        self.rolls = []     
        self.roll_values = [] 

def set_input(self, score_card: ScoreCard):
        self.score_card = score_card
        raw  = (score_card.pins or "").strip()
        self.rolls = list(raw)
        self.roll_values = self._parse_rolls(self.rolls)

  