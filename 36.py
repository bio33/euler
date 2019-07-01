def string_palindrome(binary_string):
    l = len(binary_string)
    if l % 2 == 0:
        first_half = binary_string[:l//2]
        second_half = binary_string[l//2:]
    else:
        first_half = binary_string[:l//2]
        second_half = binary_string[l//2 + 1:]

    if first_half == second_half[::-1]:
        return True
    else:
        return False


def num_palindrome(num):
    return string_palindrome(str(num))


def get_binary(num):
    binary_str = "{0:b}".format(num)
    return binary_str

total_sum = 0
for i in range(1000000):
    if num_palindrome(i):
        binary = get_binary(i)
        if string_palindrome(binary):
            print(i)
            total_sum += i

print(total_sum)