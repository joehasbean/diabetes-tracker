import datetime
now = datetime.datetime.now()

# take three values from user
Exchanges = input("Exchanges: ")
Units = input("Units: ")
Blood = input("Blood Sugar: ")

# Display all values on screen

Answer=("\n" + "Diabetes Score Yippee!" + "\n" + 'Exchanges:', Exchanges, 'Units:', Units, 'Blood Sugar:', Blood)
print(Answer)