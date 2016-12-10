import random

def one_run(length=100, run_len=4):
  last = 0
  run = 0
  for i in xrange(length):
    next = random.randint(1,3)
    run = run+1 if next == last else 1
    last = next
    if run == run_len:
      return True
  return False

results = {True: 0.0, False: 0.0}
count = 10000
for i in xrange(count):
    results[one_run(100, 5)] += 1

print results[True] / count
