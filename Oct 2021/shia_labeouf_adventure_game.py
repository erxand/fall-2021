"""
File: shia_labeouf_adventure_game.py
Author: Xander Hunt
Purpose: A choose-your-own-adventure game to prove understanding of if, elif, and else statements.
ATTENTION: If you don't recognize what this is from please watch the video/song by Rob Cantor about Shia Labeouf.
You can watch the three-minute performance at the link below.
www.youtube.com/watch?v=o0u4M6vppCI
"""

# Set up variables.
alive = True
response = "x"
conversation = False

# Decision #1
print("""You're walking in the woods
There's no one around and your phone is dead
Out of the corner of your eye you spot him
Shia LaBeouf

He's following you, about 30 feet back
He gets down on all fours and breaks into a sprint
He's gaining on you
Shia LaBeouf

You're looking for you car but you're all turned around
He's almost upon you now
And you can see there's blood on his face
My gosh, there's blood everywhere!
""")
response = input("What do you do: RUN, FIGHT, CRY?\n")
if response.lower() == "fight":
    print("\nYou are unarmed and Shia LaBeouf stabs you to death "
        + "with his knife.\nYOU DIED")
    alive = False
elif response.lower() == "run":
    print("""\nRunning for your life (from Shia LaBeouf)
He's brandishing a knife (it's Shia LaBeouf)
Lurking in the shadows
Hollywood superstar Shia LaBeouf

Living in the woods (Shia LaBeouf)
Killing for sport (Shia LaBeouf)
Eating all the bodies
Actual cannibal Shia LaBeouf

Now it's dark, and you seem to have lost him
But you're hopelessly lost yourself
Stranded with a murderer
You creep silently through the underbrush

Aha! In the distance
A small cottage with a light on""")
else:
    print("\nShia LaBeouf catches up to you and stabs you to death "
        + "with his knife.\nYOU DIED")
    alive = False

# Decision #2
if alive:
    response = input("What do you do? APPROACH, LEAVE, OTHER?\n")
    if response.lower() == "leave":
        print("\nYou get lost in the forest, until you're found by a bear "
            + "and eaten.\nYOU DIED")
        alive = False
    elif response.lower() == "approach":
        print("""\nHope! You move stealthily toward it
But your leg! Ah! It's caught in a bear trap!""")
    else:
        print("""\nYou turn around and see Shia Labeouf
He swings an axe at your face
YOU DIED""")
        alive = False

# Decision #3
if alive:
    response = input("What do you do? SCREAM, GNAW (off leg), FAINT?\n")
    if response.lower() == "scream":
        print("""\nYou scream, until you see him (Shia Labeouf)
He walks forward with a sharp axe and swings it at your neck
YOU DIED""")
        alive = False
    elif response.lower() == "gnaw":
        print("""\nGnawing off your leg (quiet, quiet)
Limping to the cottage (quiet, quiet)
Now you're on the doorstep
Sitting inside
Shia LaBeouf
        
Sharpening an axe (Shia LaBeouf)
But he doesn't hear you enter (Shia LaBeouf)""")
    else:
        print("""\nYou lay there until you pass out
You never wake up
YOU DIED""")
        alive = False

# Decision #4
if alive:
    response = input("What do you do? LEAVE, STRANGLE, TALK?\n")
    if response.lower() == "talk":
        conversation = True
    elif response.lower() == "strangle":
        print("""\nYou're sneaking up behind him
Strangling superstar
Shia LaBeouf

Fighting for your life with Shia LaBeouf
Wrestling a knife from Shia LaBeouf
Stab him in his kidney
Safe at last from Shia LaBeouf

You limp into the dark woods
Blood oozing from your stump leg
You've beaten Shia LaBeouf

Wait! He isn't dead (Shia surprise)
There's a gun to your head and death in his eyes
But you can do jiu-jitsu

Body slam superstar Shia LaBeouf
Legendary fight with Shia LaBeouf
Normal Tuesday night for Shia LaBeouf
You try to swing an axe at Shia LaBeouf

But blood is draining fast from your stump leg
He's dodging every swipe, he parries to the left
You counter to the right, you catch him in the neck
You're chopping his head now
You have just decapitated Shia LaBeouf

His head topples to the floor, expressionless
You fall to your knees and catch your breath
You're finally safe from Shia LaBeouf""")
    else:
        print("""\nYou decide to leave
As you open the door it creaks
He swiftly jumps up and cuts you down with the axe
YOU DIED""")
        alive = False

# Decision #4
if conversation:
    response = input("""What do you want to say? Pick a number:
1 - Let's fight to the death
2 - Why are you like this?
3 - Rock paper scissors, if I win you let me go\n""")
    if response == "2":
        conversation = False
        print("""He looks at you and rises with the axe
You realize you can't talk your way out

Fighting for your life with Shia LaBeouf
Wrestling a knife from Shia LaBeouf
Stab him in his kidney
Safe at last from Shia LaBeouf

You limp into the dark woods
Blood oozing from your stump leg
You've beaten Shia LaBeouf

Wait! He isn't dead (Shia surprise)
There's a gun to your head and death in his eyes
But you can do jiu-jitsu

Body slam superstar Shia LaBeouf
Legendary fight with Shia LaBeouf
Normal Tuesday night for Shia LaBeouf
You try to swing an axe at Shia LaBeouf

But blood is draining fast from your stump leg
He's dodging every swipe, he parries to the left
You counter to the right, you catch him in the neck
You're chopping his head now
You have just decapitated Shia LaBeouf

His head topples to the floor, expressionless
You fall to your knees and catch your breath
You're finally safe from Shia LaBeouf""")
    elif response == "1":
        conversation = False
        print("""He stands up and lunges at you

Fighting for your life with Shia LaBeouf
Wrestling a knife from Shia LaBeouf
Stab him in his kidney
Safe at last from Shia LaBeouf

You limp into the dark woods
Blood oozing from your stump leg
You've beaten Shia LaBeouf

Wait! He isn't dead (Shia surprise)
There's a gun to your head and death in his eyes
But you can do jiu-jitsu

Body slam superstar Shia LaBeouf
Legendary fight with Shia LaBeouf
Normal Tuesday night for Shia LaBeouf
You try to swing an axe at Shia LaBeouf

But blood is draining fast from your stump leg
He's dodging every swipe, he parries to the left
You counter to the right, you catch him in the neck
You're chopping his head now
You have just decapitated Shia LaBeouf

His head topples to the floor, expressionless
You fall to your knees and catch your breath
You're finally safe from Shia LaBeouf""")
    elif response == "3":
        print("""He holds his fist out on top of the other hand
He hits the other hand three times with his fist
He lifts his fist in the air one more time to form it into his throw
        """)
    else:
        conversation = False
        print("He hears you take a step, spins, and takes your head clean off"
            + "with the axe.\nYOU DIED")

# Decision #5
if conversation:
    response = input("What do you throw against him? ROCK, PAPER, SCISSORS?\n")
    print("Shia LaBeouf chose rock.")
    if response.lower() == "rock" or response.lower() == "paper":
        print("He nods. You turn and leave."
            + " Hopefully you don't bleed out as you try to find help.")
    else:
        print("You shudder, he picks up his axe and swiftly decapitates you.")
        print("YOU DIED")


print("\nEnd of game.")