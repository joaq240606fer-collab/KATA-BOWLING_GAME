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
                # El valor de este lanzamiento es lo que falte para 10
                # Miramos el valor numérico del lanzamiento anterior
                values.append(10 - values[-1])
            elif char == 'X':
                values.append(10)
        return values

    def output(self):
        total_score = 0
        # Usamos self.rolls para saber qué "regla" aplicar (Spare o Strike)
        # Usamos self.roll_values para obtener los puntos
        for i, char in enumerate(self.rolls):
            # Sumamos el valor base del lanzamiento actual
            total_score += self.roll_values[i]
            
            # REGLA DEL SPARE:
            # Si es un spare, sumamos el valor del SIGUIENTE lanzamiento físico
            if char == '/':
                if i + 1 < len(self.roll_values):
                    total_score += self.roll_values[i + 1]
                    
        return total_score