class MudPump:
    def __init__(self, liner_id, stroke_length, efficiency):
        self.liner_id = liner_id
        self.stroke_length = stroke_length
        self.efficiency = efficiency

    def __repr__(self):
        return '{}, {}, {}'.format(self.liner_id, self.stroke_length, self.efficiency)

mud_pump_one_efficiency_bbls = MudPump(7, 12, 0.95)
mud_pump_two_efficiency_bbls = MudPump(7, 12, 0.95)
mud_pump_three_efficiency_bbls = MudPump(7, 12, 0.95)

def pumpOutputTriplex(constant, liner_id, two, stroke_length, efficiency): # Import from Hydraulics Math
    pump_output_triplex = ((constant * (liner_id ** two) * stroke_length) * efficiency)
    return(pump_output_triplex)

mud_pump_one_output_bbls_per_stroke = pumpOutputTriplex(0.000243,7,2,12,0.95)
mud_pump_two_output_bbls_per_stroke = pumpOutputTriplex(0.000243,7,2,12,0.95)
mud_pump_three_output_bbls_per_stroke = pumpOutputTriplex(0.000243,7,2,12,0.95)

mud_pump_one_strokes_per_minute = 75
mud_pump_two_strokes_per_minute = 75
mud_pump_three_strokes_per_minute = 75

mud_pump_one_output_bbls_per_minute = mud_pump_one_output_bbls_per_stroke * mud_pump_one_strokes_per_minute
mud_pump_two_output_bbls_per_minute = mud_pump_two_output_bbls_per_stroke * mud_pump_two_strokes_per_minute
mud_pump_three_output_bbls_per_minute = mud_pump_three_output_bbls_per_stroke * mud_pump_three_strokes_per_minute

casing_id = 9.313
drill_pipe_od = 5

annular_capacity = (casing_id ** 2 - drill_pipe_od ** 2) / 1029.4

annular_velocity_ft_per_minute = (mud_pump_one_output_bbls_per_minute + mud_pump_two_output_bbls_per_minute + mud_pump_three_output_bbls_per_minute) / annular_capacity
print(annular_velocity)
