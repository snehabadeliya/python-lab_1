total=int(input("enter the maximum mark of a subject"))
mark1=int(input("enter marks of first subject"))
mark2=int(input("enter marks of second subject"))
mark3=int(input("enter marks of third subject"))
mark4=int(input("enter marks of forth subject"))
mark5=int(input("enter marks of fifth subject"))
average=(mark1+mark2+mark3+mark4+mark5)/5
print("Avg is ",average)
percentages=(average/total)*100
print("according to the percentages, ")
if percentages >=90:
    print("grade: A")
elif percentages >=80 and percentages <90:
    print("grade: b")
elif percentages >=70 and percentages <80:
    print("grade: c")
elif percentages >=60 and percentages <70:
    print("grade: d")
else:
    print("grade: e")
