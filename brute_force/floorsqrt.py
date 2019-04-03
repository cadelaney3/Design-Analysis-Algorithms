def floorsqrt(n):
	floor = 0
	while floor * floor < n:
		floor = floor + 1 
	if floor * floor == n:
		return floor
	else:
		return floor - 1 

print(floorsqrt(16))
print(floorsqrt(18))
print(floorsqrt(25))
print(floorsqrt(2))
print(floorsqrt(5))
print(floorsqrt(45))
