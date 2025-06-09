def is_even(num):
    if num % 2 == 0:
        print(f"the number {num} is even")
    elif num % 2 == 1:
        print(f"the number {num} is odd")
    else:
        print(f"{num} is cursed")

is_even(2)

is_even(3)

is_even(5.2)
