matrix_size = int(input())
matrix = [[int(num) for num in input().split(", ")] for _ in range(matrix_size)]

primary_diagonal = [matrix[i][i] for i in range(matrix_size)]
secondary_diagonal = [matrix[i][matrix_size - 1 - i] for i in range(matrix_size)]

print(f"First diagonal: {', '.join([str(num) for num in primary_diagonal])}. "
      f"Sum: {sum(primary_diagonal)}\n"
      f"Second diagonal: {', '.join([str(num) for num in secondary_diagonal])}. "
      f"Sum: {sum(secondary_diagonal)}")
