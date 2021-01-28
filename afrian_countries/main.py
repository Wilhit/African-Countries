import turtle
import pandas

screen = turtle.Screen()
screen.title("African Countries Game")
image = "blank-outline-map-africa.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
#
# turtle.mainloop()
correct_count = 0


# print(answer)

data = pandas.read_csv("afrian_countries.csv")
states_names = data.country.to_list()
guessed_countries = []
while len(guessed_countries) < 50:
    answer = screen.textinput(title=f"{correct_count}/55 Countries Correct", prompt="What's another country's name?").title()
    print(answer)
    if answer == "Exit":
        missing_countries = []
        for country in states_names:
            if country not in guessed_countries:
                missing_countries.append(country)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break

    if answer in states_names:
        guessed_countries.append(answer)
        state_a = data[data.country == answer]
        print(answer)
        word = turtle.Turtle()
        word.up()
        word.hideturtle()
        word.goto(int(state_a.x), int(state_a.y))
        word.color("green")
        word.write(f"{answer}", align="center")
        correct_count += 1

#states to learn
