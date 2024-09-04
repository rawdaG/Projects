print("Welcome to my first game!")
name  = input("What is your name? ")
age = int(input("What is your age? "))

hearts = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", hearts, "hearts")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nicely done, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across": 
                print("You manged to get across, but you were bit by a fish and lost 2 hearts. ")
                hearts -= 2

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by an old lady... She tries to eat you and you lose 2 hearts. But you manage to escape. ")
                hearts -= 2
            elif ans == "river":
                print("You go to the river and find a boat. You sail away and reach the other side safely.")
                
        else:
            print("You fell down and lost... ")
            hearts = 0

        if hearts > 0:
            print("Congratulations, you survived! You have", hearts, "hearts left.")
        else:
            print("Sorry, you lost all your hearts. Game over!")
        
    else:
        print("Aww, hopefully next time!")

else:
    print("You are not old enough to play...")