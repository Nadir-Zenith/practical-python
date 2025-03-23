# bounce.py
#
# Exercise 1.5

height = 100 #meters
bounce_back_ratio = 3.0/5.0

for i in range(10):
    height *= bounce_back_ratio
    print(f'{i+1:<4} bounce, height: {round(height,4):>10} meters')