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
