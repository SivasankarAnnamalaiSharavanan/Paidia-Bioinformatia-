def calculate_rabbit_pairs(n, k):
  if n == 1 or n == 2:
      return 1

  rabbit_pairs = [0] * (n+1)
  rabbit_pairs[1], rabbit_pairs[2] = 1, 1

  for month in range(3, n + 1):
      rabbit_pairs[month] = rabbit_pairs[month - 1] + k * rabbit_pairs[month - 2]
  return rabbit_pairs[n]

with open('rosalind_fib.txt', 'r') as file:
  n, k = map(int, file.readline().split())
result = calculate_rabbit_pairs(n, k)
print(f"Total number of rabbit pairs after {n} months: {result}")
