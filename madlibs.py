
################################################################################################################
##### Implementing Madlibs, taking user input for different parts of speech, and using string concatenation ####
################################################################################################################

# #String Concatenation

# youtuber = 'markiplier'

# # a few ways do concatenate stirngs are:
# print('Subscribe to ' + youtuber)
# print('Subscribe to {}'.format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective : ")
verb1 = input("Verb : ")
verb2 = input ("Another verb : ")
famous_person = input ("Famous Person : ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated \and {verb2} like you are {famous_person}"

print('\n \n', madlib)