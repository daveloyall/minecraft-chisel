def main():
    # Create loop to allow user to continue jokes when selected
    counter1 = 0
    counter2 = 0
    while True:
        # Get input to direct user to another joke or to quit
        choice = input("ENTER HERE >>> ")
        if choice == '\\0':
            break

        if choice == '0':
            counter1 += 1
            print('zero', counter1)
            continue

        elif choice == '1':
            counter1 += 1
            print('one', counter1)
            continue

        elif choice == '\\n':
            counter1 = 0
            counter2 += 1
            print('newline', counter2)
            continue

        else:
            continue


if __name__ == "__main__":
    main()
