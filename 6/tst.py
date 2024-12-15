def swap_and_print(s, p1, p2):
    print("Before Swap:", s)
    s[s.index(p1)], s[s.index(p2)] = p2, p1
    print("After Swap:", s)

# Example
s = ['apple', 'banana', 'cherry', 'date']
swap_and_print(s, 'banana', 'date')
