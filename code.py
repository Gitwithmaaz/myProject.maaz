def print_m_correct(height):
  if height % 2 == 0 or height <= 0:
    print("Height must be an odd positive integer.")
    return

  width = 2 * height - 1
  mid = height // 2

  for row in range(height):
    for col in range(width):
      if (col == 0 or  # Left vertical line
          col == width - 1 or # Right vertical line
          (row <= mid and (  # Top V shape
              (row == col and col <= mid) or
              (row + col == 2 * mid and col >= mid)
          ))):
        print("*", end="")
      else:
        print(" ", end="")
    print()

# Example usage:
print_m_correct(7)
