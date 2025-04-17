import pandas as pd
import turtle
import state_appear

states = pd.read_csv('50_states.csv')
pop = state_appear.State()
screen = turtle.Screen()
screen.title('U.S. States game')
image = 'blank_states_img.gif'
screen.addshape('blank_states_img.gif')
screen.tracer(0)
turtle.shape(image)
screen.update()

correct_guess = 0
game = True
guessed_states = []
all_states = list(states['state'])  # or states.state.to_list()


while game:
    answer_state = screen.textinput(title=f'Guess the state {correct_guess}/50',
                                    prompt='What\'s another state\'s name? ').title()
    # if answer_state == 'Exit':
    #     states_to_learn = pd.DataFrame(sorted(list(set(all_states) - set(guessed_states))))
    #     states_to_learn.to_csv('states to learn.')
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn2')
        game = False
    for state in states['state']:
        if answer_state == state:
            pop.state_popup(state)
            correct_guess += 1
            guessed_states.append(state)
            screen.update()
    if correct_guess == 50:
        game = False
        pop.you_won()
        screen.exitonclick()
