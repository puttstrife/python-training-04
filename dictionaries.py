# Dictionaries stores data values are in key value pairs
# it looks like javascript objects


band = {

    "vocals": "Plant",
    "guitar": "Page"
}


band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(type(band2))
print(len(band))  # len determines how many key value pairs in the dictionary


# Access items

print(band["vocals"])
print(band.get("vocals"))
print(band.get("guitar"))

# list all keys

print(band.keys())
print(band.items())


# verify a key exists

print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"  # this returns a tupple
print(band)


print(band.popitem())  # remove the last added item
print(band)

# delete and clear an item

band["drums"] = "Bonham"  # this returns a tupple
del band["drums"]
print(band)

band2.clear()  # clear method

print(band2)

del band2


# copying dictionaries

# band2 = band  # creates a reference therefore it's not how we copy
# print("bad copy!")

# print(band2)
# print(band)


# band2['drums'] = "Jeff"
# print(band)
# print(band)


band2 = band.copy()
band2['Drums'] = "Jeff"
print("Good Copy")
print(band)
print(band2)

# or use the dict() constructor function

band3 = dict(band)
print("Good Copy")
print(band3)

band3["Singer"] = "Hitler"
print(band3)


# Nested Dictionaries means value of a key value pair can be a dictionary

print("-------------")

member1 = {

    "name": "plant",
    "instrument": "vocals"
}


member2 = {

    "name": "Jeff",
    "instrument": "piano"
}

band = {

    "member1": member1,
    "member2": member2

}


print(band)
print(band["member2"]["name"])  # we have to go one level deeper use brackets


# Sets this is the final collection type


nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allow in sets

nums = {1, 2, 2, 3}
print(nums)


# True is a dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in the set
print(2 in nums)

# but you can't refer ro an element in
# the set with an index position or a key

nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)  # update method
print(nums)

# you can use update with lists, tuples and dictionaries too

# Merge 2 sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = two.union(one)
print(mynewset)

# keep everything except the duplicated
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
