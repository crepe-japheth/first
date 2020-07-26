print("my first game")
name = input("what is your name? ")
age = int(input("what is your age? "))
health = 10

if age >= 18:
    print("hello! ", name, "your are  ", age, "years old ")
    play = input("do you wanna play this game? yes or no (yes/no) ").lower()
    if play == "yes":
        print("lets get started...")
        print("you started with ", health)
        way_to_go = input("which side do you want to go?  right or left (left/right) ").lower()
        if way_to_go == "left":
            ans = input("you follow the right path.... would you like to go across or around (across/around) ")
            if ans == "across":
                print("you win the game... congs")
            else:
                print("you have got injury while walking around... you lose a game")    
        if way_to_go == "right":
            ans = input("you follow the right path... would you like to go across of the river or house (river/house) ")
            if ans == "river":
                print("you hit by fish and it eat you.... so you lost")
            else:
                print("you entered the house, you greeted by the owner and he doesn't like you, you gotta go out..... sorry youu lose a game ")        
    else:
        print("good  bye...") 
else:
    print("your are under 18, not allowed to play this game. just get out here")    