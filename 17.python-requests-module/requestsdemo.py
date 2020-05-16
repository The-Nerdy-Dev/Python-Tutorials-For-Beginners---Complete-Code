
import requests
url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
print(response)
print(response.status_code)
todos = response.json()
print(todos)

for todo in todos:
  print("Todo created by User with Id: ", todo["userId"])
  print("Todo ID: ", todo["id"])
  print("Title of todo: ", todo["title"])
  print("Is completed ?", todo["completed"])
  print("----------------------------------------------")

