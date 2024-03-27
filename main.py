/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
1.
def reverse_string(input_string):
    return input_string[::-1]

def main():
    input_string = input().strip()
    reversed_string = reverse_string(input_string)
    print(reversed_string)

if __name__ == "__main__":
    main()
    
2.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    num = int(input().strip())
    if is_prime(num):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
    
3.
from functools import cmp_to_key

def compare(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    return int(yx) - int(xy)

def largest_number(arr):
    arr.sort(key=cmp_to_key(compare))
    return ''.join(map(str, arr))

def main():
    arr = eval(input().strip())  # Safely evaluate the input string as a list
    result = largest_number(arr)
    print(result)

if __name__ == "__main__":
    main()
    
4.
def reverse_number(n):
    return int(str(n)[::-1])

def main():
    n = int(input().strip())
    reversed_n = reverse_number(n)
    print(reversed_n)

if __name__ == "__main__":
    main()
    
5.
def find_max_min(arr):
    if not arr:
        return None, None
    max_element = min_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num
    return max_element, min_element

def main():
    arr = eval(input().strip())  
    max_element, min_element = find_max_min(arr)
    print(max_element, min_element)

if __name__ == "__main__":
    main()
