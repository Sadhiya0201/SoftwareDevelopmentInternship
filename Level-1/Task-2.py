# number_pattern.py

def number_pyramid(n):
    print("\nPattern 1: Number Pyramid")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def inverted_pyramid(n):
    print("\nPattern 2: Inverted Number Pyramid")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def right_aligned_pyramid(n):
    print("\nPattern 3: Right-Aligned Number Pyramid")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")  # spaces
        for j in range(1, i + 1):
            print(j, end="")
        print()

def main():
    print("Number Pattern Generator - Task 2")
    n = int(input("Enter the number of rows: "))

    number_pyramid(n)
    inverted_pyramid(n)
    right_aligned_pyramid(n)

if __name__ == "__main__":
    main()
