from collections import Counter

with open("input", "r") as f:
    lines = f.readlines()

f.close()

list1 = []
list2 = []

for line in lines:
    parts = line.strip().split("   ")
    if len(parts) >= 2:
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

list1_ordered = sorted(list1)
list2_ordered = sorted(list2)


distances = [abs(a - b) for a, b in zip(list1_ordered, list2_ordered)]

total_distance = sum(distances)

print(f"Total distance: {total_distance}")

list2_counter = Counter(list2)

similarities = [locationID * list2_counter[locationID] for locationID in list1]

similarity_score = sum(similarities)

print(f"Similarity score: {similarity_score}")
