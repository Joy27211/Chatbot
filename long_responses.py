import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"

R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

R_HELP = "You can contact our college on Tel. No. '244 7189' or through this mail-id 'royalcollegedbl@ymail.com'"

R_ADDRESS = "Royal college is located at Ground floor of Gautam Labdhi Apartment, Savarkar Road, Dombivli East"

R_LOCATION = "https://www.google.com/maps/place/Dombivli+Yuvak+Education+Trust+Royal+College+of+Commerce+%26+" \
             "Science/@19.2023104,73.0900005,15z/data=!4m5!3m4!1s0x0:0xe8c6de6837a1c6b1!8m2!3d19.2023104!4d73.0900005"

R_COURSES = "Royal College provides courses like\n     BCom\n     BMS\n     BAF\n     BSc IT\n     BMM"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry, couldn't get you",
                "What does that mean?"][
        random.randrange(4)]
    return response
