points = list(map(int, input().split()))
print(min(points), points.index(min(points)))
print(max(points), points.index(max(points)))
print(*points)