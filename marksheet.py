s1=int(input("Enter subject1 mark:"))
s2=int(input("Enter subject2 mark:"))
s3=int(input("Enter subject3 mark:"))

total=s1+s2+s3
print("Total:",total)

pr=total/3
print("PR:",pr)

if pr>=70:
    print("Result:Dist.")
elif pr>=60:
    print("Result:First Class")
elif pr>=50:
    print("Result:Second Class")
elif pr>=40:
    print("Result:Pass Class")
else:
    print("Result:FAIL")