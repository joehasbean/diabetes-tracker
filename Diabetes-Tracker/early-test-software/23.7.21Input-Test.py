import datetime
now = datetime.datetime.now()

# take three values from user
Exchanges = input("Exchanges: ")
Units = input("Units: ")
Blood = input("Blood Sugar: ")

# Display all values on screen
print('\n')
print('Diabetes Tracked')
print('Exchanges:', Exchanges, 'Units:', Units, 'Blood Sugar:', Blood)
print (now.strftime("%Y-%m-%d %H:%M:%S"))
