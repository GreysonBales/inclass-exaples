# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("Whos the invitee? ")
num_people = input("How many people?")
training_time = input("Time of training?")
# [ ] create an integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 10
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
print(str.format("{} is coming in for class and is bringing {} people, training will take {} minutes and you need to be at the class {} early"
                 , owner, num_people, training_time, min_early"))

