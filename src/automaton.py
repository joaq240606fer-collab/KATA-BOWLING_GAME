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
        # Por ahora, convertimos cada caracter numérico a su valor entero
        # Si el pin es '-', se trata como un 0
        values = []
        for char in rolls:
            if char.isdigit():
                values.append(int(char))
            elif char == '-':
                values.append(0)
            # Nota: Dejamos el soporte para 'X' y '/' para los siguientes tests
        return values

    def output(self):
        # Para este test de tiros regulares, basta con sumar los valores
        return sum(self.roll_values)