

class ScoreCard:
    def __init__(self): 
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

    
    