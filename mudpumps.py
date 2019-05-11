class MudPump:
    def __init__(self, liner_id, stroke_length, efficiency):
        self.liner_id = liner_id
        self.stroke_length = stroke_length
        self.efficiency = efficiency

    def __repr__(self):
        return '{}, {}, {}'.format(self.liner_id, self.stroke_length, self.efficiency)

mud_pump_one = MudPump(input('Liner ID: '), input('Stroke Length: '), input('Efficiency: '))
print(mud_pump_one)
