#This is where we will run the code for my animal

from Feelings.make_animal import Animal
from Feelings.positive_feelings import feeling_happy, feeling_excited
from Feelings.negative_feelings import feeling_sad

browbrow = Animal('BrowBrow', 10, 'cat')

browIsFeelingHappy = feeling_happy(browbrow.name, browbrow.animalType)
print(browIsFeelingHappy)

browIsFeelingExcited = feeling_excited(browbrow.name, browbrow.animalType)
print(browIsFeelingExcited)

browIsFeelingSad = feeling_sad(browbrow.name, browbrow.animalType)
print(browIsFeelingSad)

BrowBrowHungry = browbrow.hungry()
print(BrowBrowHungry)

HowFastBrowBrow = browbrow.runs()
print(HowFastBrowBrow)

print(browbrow.age)
