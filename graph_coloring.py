colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'BLACK']
states = ['ANDHRA', 'KARNATAKA', 'TAMILNADU', 'KERALA']
neighbors = {
    'ANDHRA': ['KARNATAKA', 'TAMILNADU'],
    'KARNATAKA': ['ANDHRA', 'TAMILNADU', 'KERALA'],
    'TAMILNADU': ['ANDHRA', 'KARNATAKA', 'KERALA'],
    'KERALA': ['KARNATAKA', 'TAMILNADU']
}
colors_of_states = {}

def promising(state, color):
    for neighbor_state in neighbors.get(state, []):
        if neighbor_state in colors_of_states and colors_of_states[neighbor_state] == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color
    return None  # No valid color found

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)

if __name__ == "__main__":
    main()
