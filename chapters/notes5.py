minutes = 105
print(minutes / 60)
hours = minutes // 60
print(hours)
remainder = minutes - hours * 60
print(remainder)
remainder = minutes % 60
print(remainder)
print(213 % 100)
start = 11
duration = 3
end = (start + duration) % 12
print(end)
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)
def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)

print_n_times('Hello', 3)


name = input('What is your name?\n')
print(name)
prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
print(speed)

# testing commit signatures
