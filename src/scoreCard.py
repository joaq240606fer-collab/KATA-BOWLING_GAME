

class ScoreCard:
    def __init__(self, pins=""):
        # store the raw pins string (e.g. "X9-...") and keep internal score buckets
        self.pins = pins
        self.scores = {}

    def add_score(self, category, score):
        if category in self.scores:
            self.scores[category] += score
        else:
            self.scores[category] = score

    def get_score(self, category):
        return self.scores.get(category, 0)

    def total_score(self):
        return sum(self.scores.values())

    
    