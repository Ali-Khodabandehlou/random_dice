import random

dices = ["\n","\n","\n","\n","\n","\n", "\n"]


def draw_num(i):
    switcher = {
            1: draw_one,
            2: draw_two,
            3: draw_three,
            4: draw_four,
            5: draw_five,
            6: draw_six,
    }
	
    func = switcher.get(i, lambda: print("err"))
    return func()

	
def draw_one():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |               | "
    dices[3] += " |      |_|      | "
    dices[4] += " |               | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         1         "
    
	
def draw_two():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |  |_|          | "
    dices[3] += " |               | "
    dices[4] += " |          |_|  | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         2         "
    
	
def draw_three():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |  |_|          | "
    dices[3] += " |      |_|      | "
    dices[4] += " |          |_|  | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         3         "
    
	
def draw_four():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |  |_|     |_|  | "
    dices[3] += " |               | "
    dices[4] += " |  |_|     |_|  | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         4         "
    
	
def draw_five():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |  |_|     |_|  | "
    dices[3] += " |      |_|      | "
    dices[4] += " |  |_|     |_|  | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         5         "
    
	
def draw_six():
    dices[0] += " _ _ _ _ _ _ _ _ _ "
    dices[1] += " |               | "
    dices[2] += " |  |_|     |_|  | "
    dices[3] += " |  |_|     |_|  | "
    dices[4] += " |  |_|     |_|  | "
    dices[5] += " | _ _ _ _ _ _ _ | "
    dices[6] += "         6         "
    
	
def main():
    print("welcoe to the random dice simulator!")

    while True:
        num_of_dices = int(input("\nenter number of dices:"))
        for i in range(0, num_of_dices):
            draw_num(random.randint(1, 6))
            
        for i in range(0, 7):
            print(dices[i])
            dices[i] = "\n"
            
        _continue = input("\ndo you want to roll again? (y/n)")
        if(_continue == "n"):
            print("\nWe had a great time :)\nWish to see you again!")
            input("press any key to exit")
            break;
    
    
if "__main__" in __name__:
    main()