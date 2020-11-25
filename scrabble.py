letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {key: value for key, value in zip(letters, points)}

#Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0

#Define a function called score_word that takes in a parameter word.
#Inside score_word, create a variable called point_total and set it to 0.
#create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.pop(letter, 0)
  return(point_total)

#Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Create a dictionary called player_to_words that maps players to a list of the words they have played.
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#Create an empty dictionary called player_to_points
player_to_point = {}

#Iterate through the items in player_to_words. Call each player player and each list of words words.
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_point[player] = player_points

print(player_to_point)


