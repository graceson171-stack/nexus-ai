# documents = [
#     "Operating Systems",
#     "Computer Networks",
#     "Database Management Systems"
# ]

# print(documents)
# print(documents[1])
# print(documents[2])
# documents.append("Machine Learning")
# print(documents)
# documents.remove("Computer Networks")
# print(documents)
# print(len(documents))

documents = ["OS", "CN", "DBMS", "ML", "AI"]
print(documents)
documents.append("DSA")
print(documents)
documents.remove("CN")
print(documents)
print(len(documents))

for num, doc in enumerate(documents, start=1):
    print(f"{num}. {doc}")
