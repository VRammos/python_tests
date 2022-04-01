import matplotlib.pyplot as plt

math_grades = []

for grades in range(8):
  math_grades.append(randrange(0,11))

math_grades

x = list(range(1,9))
y = math_grades
print("x =", x)
print("y =", y)
plt.plot(x, y, marker="o")
plt.title('Math Grades')
plt.xlabel('Tests')
plt.ylabel('Grades')
plt.show()

// A simple graphic showing the (random) grades of a student on many tests
