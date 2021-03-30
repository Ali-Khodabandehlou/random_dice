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
        if num_of_dices <= 0:
            print("\nplease enter a number bigger than 1!\n")
            continue;
    
        if num_of_dices <= 5:
            for i in range(0, num_of_dices):
                draw_num(random.randint(1, 6))
                
            for i in range(0, 7):
                print(dices[i])
                dices[i] = "\n"

        elif num_of_dices > 4:
            bigger_dices = []
            
            for i in range(0, num_of_dices):
                draw_num(random.randint(1, 6))
                if (i + 1) % 4 == 0:
                    for j in range(0, 7):
                        bigger_dices.append(dices[j])
                        dices[j] = "\n"
            
            for i in range(0, len(bigger_dices)):
                print(bigger_dices[i])
            bigger_dices.clear()
            
            for i in range(0, 7):
                if dices[i] != "\n":
                    print(dices[i])
                    dices[i] = "\n"
            
        else:
            print("\nplease enter a number bigger than 1!\n")
            continue;
        
        _continue = input("\ndo you want to roll again? (y/n)")
        if(_continue == "n"):
            print("\nWe had a great time :)\nWish to see you again!\n")
            input("press any key to exit")
            break;
    
    
if "__main__" in __name__:
    main()
