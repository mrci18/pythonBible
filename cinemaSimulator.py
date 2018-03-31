films = {
    "Finding Nemo": {"age": 3, "tickets": 5},
    "Get Out": {"age": 18, "tickets": 15},
    "The Avengers": {"age": 18, "tickets": 25}
}

while True:
   choice = input("What film would you like to watch?: ").strip().title()

   if choice in films:
       age = int(input("How old are you?").strip())
       if age >= films[choice]["age"]: #Check user age
           if films[choice]["tickets"] > 0:
               print("Enjoy the film")
               films[choice]["tickets"] = films[choice]["tickets"]-1
           else:
               print("There are no more tickets for this film")
       else:
           print("you are too young to watch the film")
           
   else: 
        print("We don't have that film")