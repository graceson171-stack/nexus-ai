
import json
documents = ["ML", "OS", "DBMS"]
with open("data/documents.json", "r") as file:
    documents = json.load(file)   
print("Documents Loaded: ")
for num, doc in enumerate(documents, start=1):
    print(f"{num}. {doc}")
