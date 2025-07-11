def generate_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return generate_fibonacci(n - 1) + generate_fibonacci(n - 2)

fibonacci_num, i, sum = 0, 0, 0

while fibonacci_num < 4 * 10 ** 6:
    fibonacci_num = generate_fibonacci(i)

    if fibonacci_num % 2 == 0:
        sum += fibonacci_num

    i += 1

print(sum)
