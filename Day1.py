sonar=[
199,
200,
208,
210,
200,
207,
240,
269,
260,
263,
]

# numbers = [int(line) for line in sonar.splitlines()]

count = 0

for i in range(1, len(sonar)):
    if sonar [i]>sonar[i-1]:
        count += 1

print(f'part 1:{count}')

count = sum(
    sonar[i]> sonar[i-3]
    for i in range(3, len(sonar))
)

print(f'part 2:{count}')
print(len(sonar))

