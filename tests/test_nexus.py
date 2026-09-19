from src.nexus_cli import save_documents

documents = ["AI", "ML", "DBMS"]

save_documents(documents, "test_documents.json")

with open("test_documents.json", "r") as file:
    content = file.read()

assert "AI" in content
assert "ML" in content
assert "DBMS" in content

print("Test passed!")