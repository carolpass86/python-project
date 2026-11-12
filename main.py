
from command.user_command import get_user_command
from command.command_processor import process_command
from store.cvs_store import load_data
def main():

    try:
        student_data = load_data()
    except:
       print("error happened")
       return

    while True:
      command = get_user_command()
      if command == "exit":
          break
      process_command(command,student_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
