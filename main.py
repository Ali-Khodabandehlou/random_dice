import random

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
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|               |")
    print("\n|      |_|      |")
    print("\n|               |")
    print("\n| _ _ _ _ _ _ _ |")
	
    
def draw_two():
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|  |_|          |")
    print("\n|               |")
    print("\n|          |_|  |")
    print("\n| _ _ _ _ _ _ _ |")
    
	
def draw_three():
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|  |_|          |")
    print("\n|      |_|      |")
    print("\n|          |_|  |")
    print("\n| _ _ _ _ _ _ _ |")
    
	
def draw_four():
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|  |_|     |_|  |")
    print("\n|               |")
    print("\n|  |_|     |_|  |")
    print("\n| _ _ _ _ _ _ _ |")
    
	
def draw_five():
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|  |_|     |_|  |")
    print("\n|      |_|      |")
    print("\n|  |_|     |_|  |")
    print("\n| _ _ _ _ _ _ _ |")
    
	
def draw_six():
    print("\n_ _ _ _ _ _ _ _ _")
    print("\n|               |")
    print("\n|  |_|     |_|  |")
    print("\n|  |_|     |_|  |")
    print("\n|  |_|     |_|  |")
    print("\n| _ _ _ _ _ _ _ |")
    
	
def main():
    print("welcoe to the random dice simulator!")
    while True:
        num_of_dices = int(input("\nenter number of dices:"))
		
        for i in range(0, num_of_dices):
            draw_num(random.randint(1, 6))
			
        _continue = input("\ndo you want to roll again? (y/n)")
		
        if(_continue == "n"):
            print("\nWe had a great time :)\nWish to see you again!")
            input("press any key to exit")
            break;
    
    
if __name__ == "__main__":
    main()