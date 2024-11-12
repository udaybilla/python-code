# pylint: disable=C0114,C0116,W0718

MY_LUCKY_NUMBER = 0
uday_list = [0, 1, 2, 3, "2"]

def luck_number(my_list):
    for i in my_list:
        if i % MY_LUCKY_NUMBER == 0:
            print("luck")
        else:
            print("no luck")

def main():
    try:
        luck_number(uday_list)
    except ZeroDivisionError as e:
        print("Cannot divide as it is not possible with the number in the list")
        print(f"error: {e}")
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    except TypeError as e:
        print(f"TypeError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("No matter what you are lucky")
        print("whats up buddy, how are you")
        print("test")

if __name__ == "__main__":
    main()
