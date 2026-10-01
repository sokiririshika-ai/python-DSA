def longestsubstring(a):
  b = {}
  max_length = 0
  start = 0
  
  for end in range(len(a)):
      if a[end] in b:
          start = b[a[end]] + 1
      
      b[a[end]] = end
      max_length = max(max_length, end - start + 1)
  
  return max_length

# Example usage
print(longestsubstring("abcdeffghijklmno"))  
print(longestsubstring("hasini"))     
print(longestsubstring("pwwkew"))