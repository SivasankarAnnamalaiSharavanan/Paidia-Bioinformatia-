def triangular_number(base):
  if base < 2:
      return 0
  return (base * (base - 1)) / 2

def cumulative_allelic_dominance_probability(k, m, n):
  allelic_dominance_rates = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
  inheritance_frequencies = [
      triangular_number(k),
      m * k,
      n * k,
      triangular_number(m),
      m * n,
      triangular_number(n)
  ]
  dot_sum = 0
  for rate, freq in zip(allelic_dominance_rates, inheritance_frequencies):
      dot_sum += rate * freq
  freq_sum = sum(inheritance_frequencies)

  return dot_sum / freq_sum

try:
  with open('rosalind_iprb.txt', 'r') as file:
      k, m, n = map(int, file.readline().split())
  probability = cumulative_allelic_dominance_probability(k, m, n)
  print(f"The probability of producing an individual with a dominant phenotype is: {round(probability, 5)}")

except FileNotFoundError:
  print("Error: 'population.txt' file not found. Please ensure it is in the correct directory.")