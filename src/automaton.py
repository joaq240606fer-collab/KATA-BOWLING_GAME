class Automaton:
    def __init__(self):
        self.score_card = None
        self.rolls = []     
        self.roll_values = [] 

    def set_input(self, score_card):
        self.score_card = score_card
        raw = (score_card.pins or "").strip()
        self.rolls = list(raw)
        self.roll_values = self._parse_rolls(self.rolls)

    def _parse_rolls(self, rolls):
        values = []
        for i, char in enumerate(rolls):
            if char.isdigit():
                values.append(int(char))
            elif char == '-':
                values.append(0)
            elif char == '/':
                
                values.append(10 - values[-1])
            elif char == 'X':
                values.append(10)
        return values

    def output(self):
      total_score = 0
      i= 0 
      for frame in range(10): # definimos un máximo de 10 frames
        if i >= len(self.roll_values):
            break # no mas lanzamientos disponibles

        if self.rolls[i] == 'X': #strike
            total_score += 10
            # añadimos bono a los siguientes dos lanzamientos
            if i+1 < len(self.roll_values):
                total_score += self.roll_values[i+1]
            if i+2 < len(self.roll_values):
                total_score += self.roll_values[i+2]
            i += 1 # strike consume un lanzamiento 
        else:
            # frame normal o spare
            first_roll = self.roll_values[i]
            second_roll = 0
            if i+1 < len(self.roll_values):
                second_roll = self.roll_values[i+1]
            frame_score = first_roll + second_roll
            total_score += frame_score

            if self.rolls[i+1] == '/' if i + 1 < len(self.rolls) else False: # spare
                # añadimos bono al siguiente lanzamiento
                if i+2 < len(self.roll_values):
                    total_score += self.roll_values[i+2]
            i += 2 # frame ocupa dos lanzamientos
      return total_score