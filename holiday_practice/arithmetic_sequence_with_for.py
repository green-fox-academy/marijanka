
def find_missing(sequence):

  d = sequence[1]-sequence[0]
  e = sequence[2]-sequence[1]

  if sequence[1]-sequence[0] == sequence[-1]-sequence[-2]:
    for i in sequence:
      if sequence[i+1] != sequence[i] + d:
        print(sequence[i] + d)
        break
  else:
    print(sequence[0] + e)


sequence = [1, 3, 4, 5, 6, 7]
find_missing(sequence)
