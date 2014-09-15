import sys

def crossSequence(A, i, k, j):
  prev = A[k] # Keep track of previous element
  l_index = r_index = k

  # From x = midpoint - 1 down to i, continue
  # iterating if x <= previous element.
  for x in range(k - 1, i-1, -1):
    if (A[x] > prev): break
    prev = A[x]
    l_index -= 1

  prev = A[k] # re-initialize prev for other direction

  # From x = midpoint + 1 to j, continue
  # iterating if x >= previous element
  for x in A[k+1:j+1]:
    if (x < prev): break
    prev = x
    r_index += 1
  return (l_index, r_index)

def longSequence(A, i, j):
  # base case
  if (i == j): 
    return (i, j)

  # Calculate midpoint:
  k = (i + j) / 2
  
  # Max sequence of left hand side
  (start1, end1) = longSequence(A, i, k)
  # Max sequence of right hand side
  (start2, end2) = longSequence(A, k + 1, j)
  # Max sequence that crosses the midpoint
  # between left and right arrays
  (start3, end3) = crossSequence(A, i, k, j)
  
  # Comparisons to return the largest sequence
  if (end1 - start1 > end2 - start2 and end1 - start1 > end3 - start3):
    return (start1, end1)
  if (end3 - start3 > end2 - start2): return (start3, end3)
  return (start2, end2)

def main(argv):
  if (len(argv) != 3): 
    print "Invalid number of arguments."
    print "python ps2b.py <infile.txt> <outfile.txt>"
    return
  input_filename = argv[1]
  output_filename = argv[2]
  input_file = open(input_filename, "r")
  output_file = open(output_filename, "w")
  A = []
  for line in input_file:
    A.append(int(line.rstrip()))
  if (len(A) == 1): 
    input_file.close()
    output_file.close()
    print "Empty list provided...terminating..."
    return
  if (len(A) > 1): A.pop(0)
  (start, end) = longSequence(A, 0, len(A) - 1)
  input_file.close()
  output_file.write(str(end - start + 1)+"\n")
  output_file.write(str(start + 1) + "\n")
  for x in A[start:end+1]:
    output_file.write(str(x) + "\n")
  output_file.close()
  return

if __name__ == "__main__":
  main(sys.argv)
