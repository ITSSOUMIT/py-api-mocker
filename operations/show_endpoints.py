import json

def show_endpoints():
  print("\n")
  try:
    with open("endpoints.json", "r") as file:
      existing_data = json.load(file)

    if existing_data:
      print("Existing endpoints:")
      for data in existing_data:
        print(f"=> {data['http_method']} {data['endpoint']}")
    else:
      print("No existing endpoints.")
  except FileNotFoundError:
    print("⁉️  No existing endpoints.")