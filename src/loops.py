for i in range(5):
    print("NEXUS")
for i in range(1,21):
    if(i % 2 == 0):
        print(i)    

documents = [
    "Operating Systems",
    "Computer Networks",
    "Database Management Systems",
    "Machine Learning",
    "Artificial Intelligence"
]
for i in documents:
    print(i)
for num, doc in enumerate(documents,start = 1):
    print(f"Document {num}:{doc}")


choice = ""
while choice != "4":
    print("\nNEXUS")
    print("1. Search Documents")
    print("2. Add Document")
    print("3. Delete Document")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Searching Documents...")
    elif choice == "2":
        print("Adding Document...")
    elif choice == "3":
        print("Deleting Document...")   
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")