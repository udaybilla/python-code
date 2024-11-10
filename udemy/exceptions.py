my_lucky_number = 0
uday_list=[0,1,2,3,'2']

def luck_number(my_list):
  for i in my_list:
    if i % my_lucky_number == 0:
      print("luck")
    else:
      print("no luck")

def main():
  try:
    luck_number(uday_list)
  except ZeroDivisionError as e:
    print("Cannot divide as it is not possible with the number in the list")
    print(f"error: {e}")
  except Exception as e: 
    # This will catch any other exceptions 
    print("An error occurred:", str(e))
  finally: 
    print("No matter what you are lucky")

if __name__ == "__main__":
  main()