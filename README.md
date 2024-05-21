# Mini_python_zigzag

This Python script creates a moving zig-zag star pattern in the console. The stars move back and forth, creating a dynamic visual effect.

## Description

The script uses a loop to print a row of stars (`****`) that move from left to right and then back from right to left, creating a zig-zag pattern. The movement speed is controlled using the `time.sleep` function, and the script can be stopped gracefully using a keyboard interrupt (`Ctrl+C`).

## Prerequisites

- Python 3.x

## Usage

1. **Clone the Repository or Download the Script:**

    ```bash
    git clone https://github.com/ayush-agrawal001/Mini_python_zigzag.git
    ```

2. **Run the Script:**

    ```bash
    python zig_zag_star.py
    ```

3. **Stop the Script:**

    To stop the script, press `Ctrl+C`. The script handles this interruption and exits gracefully.

## Code Explanation

The main components of the script are as follows:

- **Imports:**

    ```python
    import time, sys
    ```

    These modules are used to control the timing of the movement and handle system exit on interruption.

- **Variables:**

    ```python
    space = 0
    indentation = True
    ```

    `space` controls the number of spaces before the stars, and `indentation` controls the direction of movement.

- **Infinite Loop:**

    ```python
    while True:
        print(" " * space, end="")
        print("****")
        time.sleep(0.1)
        
        if indentation:
            space += 1
            if space == 10:
                indentation = False
        else:
            space -= 1
            if space == 0:
                indentation = True
    ```

    The loop runs indefinitely, printing spaces followed by stars and adjusting the `space` variable to move the stars back and forth.

- **Exception Handling:**

    ```python
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit()
    ```

    This allows the script to be stopped with `Ctrl+C` and ensures it exits cleanly.

## Example Output
```
****
 ****
  ****
   ****
    ****
     ****
      ****
     ****
    ****
   ****
  ****
 ****
****
```


The pattern continues indefinitely, moving stars left and right.
