import time
import os
from rich.progress import track
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from operations.register_endpoint import register_endpoint
from operations.delete_all_endpoints import delete_all_endpoints
from operations.show_endpoints import show_endpoints

def progressBar():
    print("\n")
    for i in track(range(100), description="⏰ Booting up application ..."):
        time.sleep(0.01)
    print("✅ Application booted successfully")


def main_menu():
  print("\n")
  questions = [{
    "type": "list",
    "message": "Choose operation :",
    "choices": [
      "Register endpoint",
      "Show endpoints",
      "Delete all endpoints",
      Separator(),
      "RUN SERVER",
      Separator(),
      "Exit"
    ],
    "default": None,
  }]

  result = prompt(questions)
  return result[0]


def operate(option):
  func = option.lower().replace(" ", "_")
  globals().get(func)()


if __name__ == "__main__":
  # clear screen
  os.system('cls' if os.name == 'nt' else 'clear')

  # progress bar
  progressBar()

  # actual application
  while True:
    option = main_menu()
    if option == "Exit":
      print("✅ Application terminated successfully")
      exit()
    else:
      operate(option)