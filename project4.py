# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
# start, middle and end

Characters = {'fireperson':'Jack', 'wife':'Jill'}
Special_Skills = {'skill1':'hear', 'skill2':'rescue', 'skill3':'save'}
Story1 = {'Beginning':f'{Characters["fireperson"]} is a fireman, and {Characters["fireperson"]} {Special_Skills["skill1"]}s word of a fire in the area.', 'Middle':f'{Characters["fireperson"]} suits up and rushes to the {Special_Skills["skill2"]}, putting out the fire in record time.', 'End':f'{Characters["fireperson"]} {Special_Skills["skill3"]}s the day and goes home to {Characters["wife"]}.'}

#2 - Print the entire dictionary

print(Story1)

#3 - Print the type of your dictionary

print(type(Story1))
#4 - Print only the keys

print(Story1.keys())
#4 - print only the values

print(Story1.values())
#5 - print the individual values using the keys (individually, lots of printi commands)

print(Story1['Beginning'])
print(Story1['Middle'])
print(Story1['End'])

#6 - Now let's add a new key:value pair.
Story1.update({'HeroHeight':'7ft'})