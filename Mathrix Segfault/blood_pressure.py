#Param Nayar
def bloodpressure(age):
    if age < 10 and age >= 0:
        return 0.14
        #print("The probability this individual has blood pressure issues based on age is 0.14")
    if age < 20 and age >= 10:
        return 0.13
        #print("The probability this individual has blood pressure issues based on age is 0.13")
    if age < 30 and age >= 20:
        return 0.15
        #print("The probability this individual has blood pressure issues based on age is 0.15")
    if age < 40 and age >= 30:
        return 0.16
        #print("The probability this individual has blood pressure issues based on age is 0.16")
    if age < 50 and age >= 40:
        return 0.47
        #print("The probability this individual has blood pressure issues based on age is 0.47")
    if age < 60 and age >= 50:
        return 0.45
        #print("The probability this individual has blood pressure issues based on age is 0.45")
    if age < 70 and age >=60:
        return 0.49
        #print("The probability this individual has blood pressure issues based on age is 0.49")
    if age < 80 and age >= 70:
        return 0.45
        #print("The probability this individual has blood pressure issues based on age is 0.45")
    if age > 80:
        return 0.47
        #print("The probability this individual has blood pressure issues based on age is o.47")
    else:
        return 0.0
