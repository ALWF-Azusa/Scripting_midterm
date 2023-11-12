employee_records = []

print("-" * 30)
print("{:^30}".format("員工薪資輸入"))
print("{:^30}".format("若姓名處未輸入則代表結束"))
print("-" * 30)

while True:
    name = input("請輸入姓名: ")
    if not name:
        break

    try:
        salary = int(input("請輸入薪資: "))
        print()

    except ValueError:
        print("薪資輸入錯誤，請重新輸入有效數字。")
        continue

    employee_records.append({"eName": name, "eSalary": salary})

print("-" * 30)

for record in employee_records:
    print("員工{:<6}的薪資為 {:>5,}".format(record['eName'], record['eSalary']))

total_salary = sum(record['eSalary'] for record in employee_records)
average_salary = total_salary / len(employee_records) if employee_records else 0

# average_salary = total_salary / len(employee_records)
# if employee_records else 0

print("-" * 30)
print("合計薪資為: {:>13,}".format(total_salary))
print("平均薪資為: {:>16.2f}".format(average_salary))
print("============================")
