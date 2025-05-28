"""Name: Ambrea Williams
   
   Date: 05/28/2025
   
   Unit 1: Lab 1
   
   Description: This code receives a message from the user, prints the message in reverse, 
   and shows how many charaters were used in the message.
"""

#Receives the message from the user
chat_message =input("Enter message into the chat:")


#Output the message in reverse
print("Your message in reverse is:", chat_message[::-1])

#says the number of characters in the message using the len() function.
print(f"Number of characters: {len(chat_message)}")

