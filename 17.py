x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

if area == 0:
    print("Ba điểm thẳng hàng, không tạo thành tam giác.")
else:
    print("Ba điểm tạo thành một tam giác với diện tích:", area)
