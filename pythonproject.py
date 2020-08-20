print("Welcome to my game")
name= input("What is your name? ")
age = int(input("Enter your age? " ))
health = 10
print("YOu are starting with",health,"health")
if age >= 18:
    print("You are old enough to play! ")

    wants_to_play = input("Do you want to play?  ").lower()
    if wants_to_play == "yes":
        print("Lets play!.......")

        left_or_right = input("First Choice...Left or Right(left/right) ?").lower()
        if left_or_right == "left":
            ans = input("Nice,you followed the path and reached a lake.... DO you swim across or go around (across/around)?  ")
            
            if ans =="around":
                print("You went around and reached the other side of lake")

            elif ans == "across":
                print("You managed to get across ,but were bit by a fish and lost 5 health.")
                health -=5

            ans = input("You notice a house and a river.. which do you go for?  ")

            if ans =="house":
                print("you go to the house and are greeted by the owner...He doesnt like you and you loose 5 health")
                health -=5
                if health <=0:
                    print("You now has 0 health and you lost the game....")
                else:
                    print("You survived!........")
            else:

                print("You fell in river and lost")
        else:
            print("You fell down and lost ...")

    else:
        print("Cya...")

else:
    print("You aren't old enough to play .......")