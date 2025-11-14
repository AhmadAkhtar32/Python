# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

collection = {"Ahmad", "Pakistan", "Comsats", 23 , 23 , "Ahmad", "Malka Hans"}
print(collection)
print(type(collection))

col = set ()  # syntx of creating an empty set

#Methods In sets
col.add( "Ahsan")
col.add(23)
print(col)

print(collection.union(col))            #Union of sets
print(collection.intersection(col))     # intersection of sets