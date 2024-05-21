import time, sys

# Initialize the space counter and the indentation direction
space = 0
indentation = True

try:
    # Infinite loop to create the zig-zag pattern
    while True:
        # Print spaces followed by stars to create indentation
        print(" " * space, end="")
        print("****")
        # Pause for a short time to make the movement visible
        time.sleep(0.1)
        
        # Adjust the space counter to move the stars
        if indentation:
            space += 1
            # Reverse direction when reaching the rightmost position
            if space == 10:
                indentation = False
        else:
            space -= 1
            # Reverse direction when reaching the leftmost position
            if space == 0:
                indentation = True

except KeyboardInterrupt:
    # Handle the interruption gracefully and exit
    print("Interrupted")
    sys.exit()
