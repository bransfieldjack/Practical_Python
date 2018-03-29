def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
    assert count_upper_case("A") == 1, "Single character returned."
    
print("Looks like it is working after all, but nothing appears to be happening in the program. ")