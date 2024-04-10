#Task 1:


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_submitted_and_attended = set(submitted) & set(attended)
print("Students who both submitted assignments and attended class:", both_submitted_and_attended)




#Task 2:


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

lists_are_identical = set(submitted) == set(attended)
print("Are the two lists identical in terms of content?:", lists_are_identical)




#Task 3:


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended = list(set(attended) & set(submitted))
print("The attended list after removing students who didn't submit:", attended)


