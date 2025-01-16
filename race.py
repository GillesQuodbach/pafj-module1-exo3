import random

def race_mode(mode,replay_game):

    start_horse_number = random.randint(12,21)
    horses_list = list(range(1,start_horse_number))
    final = list()

    match mode:
        case "tiercé":
            horses_number = 3
        case "quarté":
            horses_number = 4
        case "quinté":
            horses_number = 5
        case "stop":
            replay_game = True
            print("Au revoir!")
            return replay_game
        case _:
            print("Merci de choisir un type de course valide")
            return replay_game

    for _ in range(horses_number):
        random_index = random.randint(0, len(horses_list) - 1)
        random_horse = horses_list[random_index]
        horses_list.remove(random_horse)
        final.append(random_horse)
    print(f"Type de la course = {mode}")
    print(f"Cheveaux au départ = {start_horse_number}")
    print(f"Arrivée du {mode} : {final}")
    return replay_game



is_game_over = False
while not is_game_over:
    user_input = input("Quel mode de course voulez vous (tiercé/quarté/quinté ou stop) ?").lower()
    race_mode(user_input,is_game_over)