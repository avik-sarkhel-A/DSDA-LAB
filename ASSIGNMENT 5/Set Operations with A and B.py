A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

joined_set = A.union(B)

intersection_set = A.intersection(B)

is_subset = A.issubset(B)

are_disjoint = A.isdisjoint(B)

joined_ab = A.union(B)

joined_ba = B.union(A)

symmetric_difference = A.symmetric_difference(B)

del A
del B

print(f"Joined Set: {joined_set}")
print(f"Intersection Set: {intersection_set}")
print(f"Is A a subset of B? {is_subset}")
print(f"Are A and B disjoint sets? {are_disjoint}")
print(f"Joined A with B: {joined_ab}")
print(f"Joined B with A: {joined_ba}")
print(f"Symmetric Difference: {symmetric_difference}")