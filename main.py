from tkinter import *
import tkinter.font as tkFont
import random
from questionTwo import questionsTwo
from questionOne import questionsOne
from questionThree import questionsThree

# Setting screen window
window = Tk()
width = 500
height = 500

window.title("Python Quiz Game")
window.resizable(0, 0)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_pos = int((screen_width / 2) - (width / 2))
y_pos = int((screen_height / 2) - (height / 2))
window.geometry(f'{width}x{height}+{x_pos}+{y_pos}')


# setting grid row column
columns = 5
for i in range(columns):
    window.columnconfigure(i, weight=1)

rows = 15
for i in range(rows):
    window.rowconfigure(i, weight=1)

center_column = 2

# make elements
title_label_font = tkFont.Font(size=30)
title_label = Label(
    window,
    text="Python Quiz App",
    font=title_label_font
)

subtitle_label_font = tkFont.Font(size=20)
subtitle_label = Label(
    window, 
    text="Choose quiz level:",
    font=subtitle_label_font
)

menu_button_one = Button(
    window,
    text="Easy Level",
    width=30,
    height=3,
    command=lambda: show_questions('easy')
)

menu_button_two = Button(
    window,
    text="Medium Level",
    width=30,
    height=3,
    command=lambda: show_questions('medium')
)

menu_button_three = Button(
    window,
    text="Hard Level",
    width=30,
    height=3,
    command=lambda: show_questions('hard')
)

feedback_label = Label (
    window,
    text='This is the feedback'
)

###### Placing Element

# title
title_label.grid(row=0, column=center_column)

# subtitle
subtitle_label.grid(row=1, column=center_column)

menu_button_one.grid(row=2, column=center_column)
menu_button_two.grid(row=3, column=center_column)
menu_button_three.grid(row=4, column=center_column)

############# placing element end


# list function
choice_btns = []
score = 0
current_question = 0

def show_questions(level):
    # string for configuration
    questions = ''
    titleStr = ''

    # check level
    if level == 'easy':
        questions = questionsOne
        titleStr = 'Easy Quiz'

    elif level == 'medium':
        questions = questionsTwo
        titleStr = 'Medium Quiz'

    elif level == 'hard':
        questions = questionsThree
        titleStr = 'Hard Quiz'

    # destroy menu button
    menu_button_one.grid_remove()
    menu_button_two.grid_remove()
    menu_button_three.grid_remove()

    if (current_question == 0):
        # make choices button
        for i in range(4):
            button = Button(
                window,
                width=50,
                height=2,
                command=lambda i=i: check_answer(i, questions)
            )
            button.grid(column=1, sticky='w', columnspan=2)
            subtitle_label.grid(row=1, column=1, columnspan=2, sticky='w')
            choice_btns.append(button)

    # Get the current question from the questions list
    question = questions[current_question]
    title_label.config(text=titleStr)
    title_label.grid(column=1, sticky='w', columnspan=2)

    fontObj = tkFont.Font(size=10)
    subtitle_label.config(text=question['Question'], font=fontObj)
    
    global next_button
    next_button = Button (
        window,
        text='Next ->',
        width=20,
        height=3,
        state='disabled',
        command=lambda: next_question(level, questions)
    )

    # next button configuration
    next_button.grid(row=6, column=1, columnspan=2, sticky='w')
    next_button.config(state='disabled')
    
    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal", background='#fff') 


def next_question(mode, questions):
    global current_question
    current_question += 1

    feedback_label.grid_remove()
    global textRandomStr
    textRandomStr = ''

    if current_question < len(questions):
        show_questions(mode)
    else:
        show_result(questions)

rewards = [
    "Damn! You got it right. Keep it up Budy!",
    "I don't know you're smart! Let me see what you got!",
    "Do you want to be my Guru's brotheeeer",
    "You gotta be kidding me dude.",
    "You're my man dude. Proud of you man!"
]
discouragements = [
    "Ups! You have answered wrong. What a fool",
    "Ain't no way dude. Study more !",
    "Are you serious bruhh?. What the hell are you doin'",
    "That's not right. look again",
    "Close your eyes imma slap your face"
]

def check_answer(choice, questions):
    global score
    question = questions[current_question]
    selected_choice = choice_btns[choice].cget("text")

    fontObj = tkFont.Font(size=10)
    feedback_label.grid(row=9, column=1)
    
     # Check if the selected choice matches the correct answer
    if selected_choice == question["Answer"]:
        # Update the score and display it
        textRandomStr = random.choice(rewards)
        color = '#09d910'
        feedback_label.config(text=f'Correct! | {textRandomStr}', font=fontObj, foreground=color)
        choice_btns[choice].config(background=color)
        score += 1
    else:
        color = '#e60b07'
        textRandomStr = random.choice(discouragements)
        feedback_label.config(text=f'Incorrect! | {textRandomStr}', font=fontObj, foreground=color)
        choice_btns[choice].config(background=color)

    for button in choice_btns:
        button.config(state="disabled")
    next_button.config(state="normal")

def show_result(questions):
    title_label.config(text='Quiz Finished')
    subtitle_label.config(text='here is your result: ', font=tkFont.Font(size=15))

    global score_label
    score_label = Label(
        window,
        text=f'Score: {score}/{len(questions)}',
        font=tkFont.Font(size=20)
    )
    score_label.grid(row=3, column=1, columnspan=2, sticky='w')

    for i in range(4):
        choice_btns[i].destroy()

    next_button.config(text='Nice!', command=lambda: back_to_menu(next_button))

def back_to_menu(theButton):
    ###### Placing Element

    # title
    title_label.grid(row=0, column=center_column)
    title_label.config(text="Python Quiz App")

    # subtitle
    subtitle_label.grid(row=1, column=center_column)
    subtitle_label.config(text="Choose quiz level:")

    menu_button_one.grid(row=2, column=center_column)
    menu_button_two.grid(row=3, column=center_column)
    menu_button_three.grid(row=4, column=center_column)

    ############# placing element end
    score_label.grid_remove()
    theButton.grid_remove()
    








window.mainloop()