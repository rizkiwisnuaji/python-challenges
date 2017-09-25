import time

base_int = input("Please enter numbers : ")
barrier = sorted(str(base_int))
bucket = []

def check_identical_list(p):
  return len(p) == len(set(p))

while True:
  base_int += 1
  if check_identical_list(str(base_int)) and all(x in str(base_int) for x in barrier):
    bucket.append(base_int)
    break
  time.sleep(0.1)
  
if len(bucket) > 0:
  print bucket[-1]
else: 
  print "No Results !"
