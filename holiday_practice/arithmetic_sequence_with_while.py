def find_missing(sequence):

  d = sequence[1]-sequence[0]
  i = 0

  if sequence[1]-sequence[0] == sequence[-1]-sequence[-2]:
    while i  < len(sequence):
      if sequence[i+1] == sequence[i] + d:
        i += 1
      else:
        return sequence[i] + d
        break
  else:
      return sequence[0] + (sequence[-1]-sequence[-2])
