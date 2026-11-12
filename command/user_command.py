COMMAND_LIST= {"add","edit","delete","list","exit","average"}
def get_user_command()->str:

      while True:
          cmd = input("please enter your command:")
          cmd = cmd.lower()
          if cmd not in COMMAND_LIST:
             print(f"{cmd} is not a valid command")
          else:
              return cmd