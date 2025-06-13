from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

# None, NaN, 0, '', False are considered "Null" types in Python.
# None equates to "null",
# NaN (Not a Number) is used to represent undefined or unrepresentable numerical results,
# 0 is the integer representation of "null" in many contexts,
# '' is an empty string, and False is the boolean representation of "null".


NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
