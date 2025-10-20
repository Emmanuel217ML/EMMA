
command=""
while True:
    command=input("> ").lower()
    if command== "start":
        print("car have started and ready yo go")
    elif command== "stop":
        print("car has stopped")
    elif command== "help":
        print(''' 
start-type start: to start the car. 
stop-type stop : to stop the car.
quit-type quit : to quit the game and dont think of playing       
        
        ''')
    elif command == "quit":
        break
    else:
        print(" i don't understand the input")
