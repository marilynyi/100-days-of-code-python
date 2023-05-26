# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_heights = 0
for i in student_heights:
    total_heights += i

average_height = int(round(total_heights / len(student_heights),0))
print(average_height)
