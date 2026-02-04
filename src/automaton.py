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
        # Recorremos la lista de caracteres originales
        for i, char in enumerate(self.rolls):
            # Sumamos el valor base del lanzamiento (ya procesado en _parse_rolls)
            total_score += self.roll_values[i]
            
            # REGLA DEL SPARE: Suma el siguiente lanzamiento
            if char == '/':
                if i + 1 < len(self.roll_values):
                    total_score += self.roll_values[i + 1]
            
            # REGLA DEL STRIKE: Suma los dos siguientes lanzamientos
            elif char == 'X':
                # Primer strike
                if i + 1 < len(self.roll_values):
                    total_score += self.roll_values[i + 1]
                # Segundo strike
                if i + 2 < len(self.roll_values):
                    total_score += self.roll_values[i + 2]
                    
        return total_score