def threefive(n: int = 100) -> None:
    """
    Prints numbers from 1 to n, replacing multiples of 3 with 'Three',
    multiples of 5 with 'Five', and multiples of both with 'ThreeFive'.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)


if __name__ == "__main__":
    threefive()
