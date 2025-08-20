def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    
    while True:
        # Get input and convert to lowercase
        user_input = input("You: ").lower()  
        
        # Check responses using if-elif
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break  # Exit the loop
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
