import math


def print_lyrics():
    """Print the lyrics of a song."""
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    print("I cut down trees, I skip and jump.")
    print("I like to press wildflowers.")


print_lyrics()


def print_twice(string):
    print(string)
    print(string)


print_twice("Dennis Moore, ")
line = "Dennis Moore, "
print_twice(line)


def repeat(word, n):
    print(word * n)


spam = "Spam, "
repeat(spam, 4)


def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)


first_two_lines()


def last_three_lines():
    repeat(spam, 2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)


last_three_lines()


def print_verse():
    first_two_lines()
    last_three_lines()


print_verse()
for i in range(2):
    print(i)


for i in range(2):
    print("Verse", i)
    print_verse()
    print()


def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()


def cat_twice(part1, part2):
    """Concatenate two strings and print them twice."""
    cat = part1 + part2
    print_twice(cat)


line1 = "Always look on the "
line2 = "bright side of life. "
cat_twice(line1, line2)


# Exercise 3.1
def repeat(word, n):
    """Print a word n times.

    Args:
        word: The string to repeat
        n: Number of times to repeat
    """
    for i in range(n):
        print(word, end="")
    print()  # Add final newline


def repeat(word, n):
    """Print a word n times.

    Args:
        word: The string to repeat
        n: Number of times to repeat
    """
    print(word * n)


def nth_prime(n):
    """Calculate the nth prime number using Sieve of Eratosthenes.

    Args:
        n: Position of the prime number to find (1 gives first prime)

    Returns:
        The nth prime number

    Raises:
        ValueError: If n < 1
    """
    if n < 1:
        raise ValueError("n must be positive")

    # Use a generous upper bound for the nth prime
    if n < 6:
        # Handle small values directly
        first_primes = [2, 3, 5, 7, 11]
        return first_primes[n - 1]

    # Upper bound for nth prime based on number theory
    upper_bound = int(n * (math.log(n) + math.log(math.log(n))))

    # Create Sieve array
    sieve = [True] * (upper_bound + 1)
    sieve[0] = sieve[1] = False

    # Apply Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(upper_bound)) + 1):
        if sieve[i]:
            for j in range(i * i, upper_bound + 1, i):
                sieve[j] = False

    # Count primes until we reach nth
    count = 0
    for i in range(2, upper_bound + 1):
        if sieve[i]:
            count += 1
            if count == n:
                return i

    return None  # Should never reach here given our upper bound


# Example usage:
print(nth_prime(1))  # 2
print(nth_prime(10))  # 29
print(nth_prime(100))  # 541
print(nth_prime(1_000))
print(nth_prime(10_000))  # 104729
print(nth_prime(100_000))  # 1299720


# write a function named print_right that takes a string named text
# as a parmeter and prints the string with enough leading spaces that
# the last letter of hte string is in the 40th column of the display
# hint: use the len function, the string concatenaiton operator (+),
# and the string repetition operator (*)
def print_right(text):
    """Print the text right-aligned in a field of 40 characters."""
    # Calculate the number of leading spaces needed
    spaces_needed = 40 - len(text)
    if spaces_needed < 0:
        spaces_needed = 0  # Don't allow negative spaces
    # Print the text with leading spaces
    print(" " * spaces_needed + text)


print_right("Monty")
print_right("Python's")
print_right("Flying Circus")


# Write a functoin called "triangle" that takes a a string and
# an integer and draws a triangle with the given height, made up
# of copies of the string. Here's an example of a triangle with five levels
# using the string 'L':
# triangle('L', 5)
# L
# LL
# LLL
# LLLL
# LLLLL
def triangle(string, height):
    """Draw a triangle of a given height using the specified string."""
    for i in range(1, height + 1):
        print(string * i)


# Example usage
triangle("L", 5)


def rectangle(string, width, height):
    """Draw a rectangle of a given width and height using the specified string."""
    for i in range(height):
        print(string * width)


# Example usage
print("Exmaple Usage:")

# Write a function called "rectangle" that takes a string and two integers
# and draws a rectangle with the given width and height, made up
# of copies of the string. Here's an example of a rectangle with width 5
# and height 3 using the string 'L':
rectangle("L", 5, 3)
# The song "99 Bottles of Beer" starts with this verse:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
# Then the second verse is the same, except that it starts with 98
# bottles and ends with 97. The song continues - for a very long time -
# until there are 0 bottles of beer. Write a function called bottle_verse
# that takes a number as a parameter and displays the verse that starts
# with the given number of bottles.
# Hint: consider starting with a function that can print the first,
# second, or last line of the verse, and then use it to write
# bottle_verse. Use this function call to display the first verse:
# bottle_verse(99)


def bottle_verse(bottles):
    """Display the verse for a given number of bottles."""
    if bottles > 2:
        print(
            str(bottles)
            + " bottles of beer on the wall\n"
            + str(bottles)
            + " bottles of beer."
        )

        print(
            "Take one down, pass it around\n"
            + str(bottles - 1)
            + " bottles of beer on the wall."
        )
    elif bottles == 2:
        print("2 bottles of beer on the wall\n" + "2 bottles of beer.")
        print("Take one down, pass it around\n" + "1 bottle of beer on the wall.")
    elif bottles == 1:
        print("1 bottle of beer on the wall\n" + "1 bottle of beer.")
        print(
            "Take one down, pass it around\n" + "No more bottles of beer on the wall."
        )

    print()


# Example usage
bottle_verse(99)
for n in range(99, 0, -1):
    bottle_verse(n)
