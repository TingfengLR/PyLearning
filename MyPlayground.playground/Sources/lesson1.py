import random

def main(){
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    myNumber = random.randint(smaller, larger)
    count = 0
    while Ture:
    count += 1
    userNumber = int(input("Enter your guess:"))
    if userNumber < myNumber:
    print("Too small")
    elif userNumber > myNumber:
    print("Too large")
    else:
    print("You've got it in", count, "tries!")
    break
}

if _name_ == "_main_":
    main()
