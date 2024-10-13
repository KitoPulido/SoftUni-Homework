pool = float(input())
pipe1 = float(input())
pipe2 = float(input())
hours = float(input())

full = (pipe1 * hours) + (pipe2 * hours)
pool1 = pool / 100
pipes = full / 100
full_percent = full / pool1
pipe1_percent = (pipe1 * hours) / pipes
pipe2_percent = (pipe2 * hours) / pipes
if full <= pool:
    print(f"The pool is {full_percent:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.")
elif full > pool:
    overflow = full - pool
    print(f"For {hours} hours the pool overflows with {overflow} liters.")