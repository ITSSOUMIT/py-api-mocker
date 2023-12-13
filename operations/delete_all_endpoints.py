import os

def delete_all_endpoints():
  print("\n")
  try:
    os.remove("endpoints.json")
  except FileNotFoundError:
    pass
  print("✅ Deleted all endpoints")