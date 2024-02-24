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

band2 = band  # creates a reference
print("bad copy!")

print(band2)
print(band)
