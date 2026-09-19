import json

def load_documents():
    with open("data/documents.json", "r") as file:
        return json.load(file)

def save_documents(documents, filename="data/documents.json"):
    with open(filename, "w") as file:
        json.dump(documents, file)

def add_document(documents):
    document = input("Enter the document name to add: ")
    documents.append(document)
    save_documents(documents)
    print(f"Document '{document}' added successfully")

def delete_document(documents):
    document = input("Enter the document name to delete: ")
    if document in documents:
        documents.remove(document)
        save_documents(documents)
        print(f"Document '{document}' deleted successfully.")
    else:
        print(f"Document '{document}' not found.")

def list_documents(documents):
    if len(documents) == 0:
        print("No documents available.")
    else:
        print("\nDocuments:")
        for num, doc in enumerate(documents, start=1):
            print(f"{num}. {doc}")

def search_documents(documents):
    query = input("Enter search term: ")
    if query.strip() == "":
        print("Search term cannot be empty.")
        return
    found = False
    for doc in documents:
        if query.lower() in doc.lower():
            print(f"Found: {doc}")
            found = True
    if not found:
        print("No documents found matching the search term.")

def main():
    documents = load_documents()

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
            search_documents(documents)
    
        elif choice == "2":
            add_document(documents)
    
        elif choice == "3":
            delete_document(documents)
  
        elif choice == "5":
            print("Exiting...")

        elif choice == "4":
            list_documents(documents)
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()