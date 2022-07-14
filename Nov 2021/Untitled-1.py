"""
This is just a scratch file
"""

print()

def display_bird(bird):
    """ Display "bird" on the screen. """
    print("The bird is", bird)

display_bird("Duck")
display_bird("Duck")
display_bird("Duck")
display_bird("Goose")


def get_the_answer() -> int:
    """ Fint the answer to everything. """
    return 42

print(f"What is the answer to the meaning of life, the universe, and everything? {get_the_answer()}")


def add_stuff(x, y, z) -> int:
    return x + y + z

print("The sum is:", add_stuff(13, 135, 241))

print()