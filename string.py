import pickle

# PROGRAM Serializing=Objects:
MyObject = ["a list", "containing", 5, "values including another list", ["inner", "list"]]

# Create a list
with open("pickled_list.p", "wb") as MyFile:
    pickle.dump(MyObject, MyFile)

# Load the object to the file
with open("pickled_list.p", "rb") as MyFile:
    MyNewObject = pickle.load(MyFile)

# Load the file into the object
print(MyNewObject)
assert MyNewObject == MyObject
# END.
