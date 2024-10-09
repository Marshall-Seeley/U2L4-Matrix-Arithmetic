# There is no need to import SAMPLE_MATRICES
# Marshall Seeley
# U2L4
# Matrix Arithmetic

# Addition:
def mat_sum(m1, m2):
  # Judgement:
  if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    # The Actual Math:
    # The Dimensions:
    width = len(m1[0])
    height = len(m1)

    # The Generation:
    SumMatrix = [[0 for x in range(width)] for y in range(height)]
    for l in range(0, len(SumMatrix)):
      for e in range(0, len(SumMatrix[l])):
        sum = m1[l][e] + m2[l][e]
        SumMatrix[l][e] = sum
    return SumMatrix

  # If the Condition Fails:
  else:
    SumMatrix = "NO SOLUTION"
    return SumMatrix



# Multiplication:
def mat_mul(m1, m2):
  # The Dimensions:
  m1width = len(m1[0])
  m1height = len(m1)
  m2width = len(m2[0])
  m2height = len(m2)

  # Judgement:
  if m1width == m2height:
    # The Actual Math:

    # The Generation:
    ProductMatrix = [[0 for x in range(m2width)] for y in range(m1height)]
    sum = 0
    print (sum)
    sol_row = 0
    sol_col = 0
    for row in range(0, m1height):
      for col in range(0, m2width):
        sum = 0
        for i in range(0, m1width):
          product = m1[row][i] * m2[i][col]
          sum += product
        ProductMatrix[row][col] = sum

  else:
    ProductMatrix = "NO SOLUTION"

  return ProductMatrix
