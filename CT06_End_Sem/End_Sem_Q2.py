"""
============================================================
Q2. List Operations
============================================================
You are working with a list of planets.
The program must perform several operations on this list.

Program Requirements:
- Use the list:
  planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
- Print the 3rd item using index
- Append "neptune" to the list
- Rename "mars" to "muskworld"
- Remove "uranus" from the list
- Using a for loop, print all the planets one by one

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================



# ============================================================
# Step 2: Print the 3rd item (Test Case 1)
#     - Comment after testing
# ============================================================



# ============================================================
# Step 3: Append "neptune"
# ============================================================



# ============================================================
# Step 4: Rename "mars" to "muskworld"
# ============================================================



# ============================================================
# Step 5: Remove "uranus"
# ============================================================



# ============================================================
# Step 6: Loop through and print all planets
# ============================================================

#question 2
planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
print(planets[2])
planets.append("neptune")
planets[3] = "muskworld"
planets.pop(6)
for i in range(len(planets)):
    print(planets[i])