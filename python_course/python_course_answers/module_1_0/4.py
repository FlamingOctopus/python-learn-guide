for row in range(15):
  for col in range(30):
    if col == row:
      print("^", end="")
    elif col == -row+14:
      print("^", end="")
    else:
      print(" ",end="")
  print()