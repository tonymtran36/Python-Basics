#BMI = weight / height ^ 2
#bmi = weight / height**2
#weight = kilograms
#height = meters
def calculate_bmi(*args):
    cases = int(args[0])
    output = []
    for i in range(1, cases+1):
    #for w, h in args:
        w = args[i][0]
        h = args[i][1]
        bmi = w / (h**2)
        if bmi < 18.5:
            output.append("Underweight")
        if bmi >= 18.5 and bmi < 25:
            output.append("Normal Weight")
        if bmi >= 25 and bmi < 30:
            output.append("Overweight")
        if bmi >30:
            output.append("Obesity")
    return output


result = calculate_bmi(3, (80, 1.73), (55, 1.58), (49, 1.91))

print(result)