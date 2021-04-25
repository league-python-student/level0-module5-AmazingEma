"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    number = simpledialog.askinteger(None,"enter a number under 40")
    for i in range(2,20):
        if i is not number:
            if number % i == 0 :
                messagebox.showerror("","number is not prime")

            else:
                messagebox.showinfo("","Number is prime")
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
