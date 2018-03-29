def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
        
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One Lower Case"
assert count_upper_case("$#@!@#") == 0, "Special Characters"
assert count_upper_case("BB") == 2, "Two upper case"

print("All tests passed")
