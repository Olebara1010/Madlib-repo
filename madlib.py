#string concatenation(aka how to put strings together)
#Suppose we want to create a string that says "subscribe to____"
#youtuber="Maxi"

#A few ways to do it,is
#print('subscribe to ' +youtuber)
#print('subscribe to {}'.format (youtuber))
#print(f'subscribe to {youtuber}')

adj=input('Adjective: ')
verb1=input('verb: ')
verb2=input('verb: ')
famous_person=input("Famous person: ")


madlib= f'computer programming is so{adj}! it makes me so excited all the time because\ I love to{verb1}. Stya hydrated and {verb2} like you are {famous_person}!'

print (madlib)