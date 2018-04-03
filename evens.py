def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    
    evens = 0 
    for n in numbers:
        if n % 2 == 0:
            evens += 1
            
    if evens == 0:
        return False
    else:
        return evens %2== 0
    
assert even_number_of_evens([]) == False, "no numbers"
assert even_number_of_evens([2, 4]) == True, "one even number"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1,3,9]) == False, "Three odd numbers"

print("All tests passed!")


