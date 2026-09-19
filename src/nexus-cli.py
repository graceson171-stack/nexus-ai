import json
documents= []
with open("data/documents.json", "r") as file:
    documents = json.load(file)
choice =""
while choice!="5":
    print("\nNEXUS")
    print("1. Search Documents")
    print("2. Add Document")   
    print("3. Delete Document")
    print("4. List Documents")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Searching Documents...")
    elif choice == "2":
        document =input("Enter the document name to add: ")
        documents.append(document)
        with open("data/documents.json", "w") as file:
            json.dump(documents, file)
        print(f"Document '{document}' added successfully.")
    elif choice == "3":
        document = input("Enter the document name to delete: ")
        if document in documents:
            documents.remove(document)
            with open("data/documents.json", "w") as file:
                json.dump(documents, file)
            print(f"Document '{document}' deleted successfully.")
        else:
            print(f"Document '{document}' not found.")  
    elif choice == "5":
        print("Exiting...")
    elif choice == "4":
        if len(documents) == 0:
            print("No documents available.")
        else:
            print("\nDocuments:")
            for num, doc in enumerate(documents, start=1):
                print(f"{num}. {doc}")
    else:
        print("Invalid choice. Please try again.")