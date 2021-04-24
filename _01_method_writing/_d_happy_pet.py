"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    pet = simpledialog.askstring("", "Will you adopt a fish, dog, rabbit, or a stickbug?")
    global petHappiness
    petHappiness = 0




    def feed():
        global petHappiness
        petHappiness += 15
        messagebox.showinfo("","your pet is liking you more and more")
    def walk():
       if pet == "fish":
           global petHappiness
           petHappiness -= 10
           messagebox.showinfo("","Why in the world did you try to walk you fish?! Its dead now")
           pass
       elif pet == "dog":
           global petHappiness
           petHappiness += 20
           messagebox.showinfo("","your puppy tangles herself in her leash, then jumps up and licks your face")
       elif pet == "rabbit":
           messagebox.showinfo("","Your rabbit is indiffernt")
       else:
           messagebox.showinfo("","You lost your stickbug in the surrounding foliage. you're a horrible pet owner")
           pass
    def play():
        if pet == "fish":
            global petHappiness
            petHappiness += 5
            messagebox.showinfo("","You cant do much with a fish. It swims lazily around your finger")
        elif pet == "dog":
            global petHappiness
            petHappiness += 30
            messagebox.showinfo("","your puppy is restless as you throw her toy out and yell FETCH")
        elif pet == "rabbit":
            global petHappiness
            petHappiness += 20
            messagebox.showinfo("","its happy")
        else:
            global petHappiness
            petHappiness += 10
            messagebox.showinfo("","Stickbugs are BOOOOOOOOOORINGGGGG")
    while(petHappiness < 100):
        q = simpledialog.askstring("","do you want to take your pet for a walk, feed it, or play with it?")
        if q == "walk":
            walk()
        elif q == "feed it":
            feed()
        else:
            play()

    messagebox.showinfo("","your pet LOOOOOOOVES you")


    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
