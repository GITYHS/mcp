def calculate_bmi(height_cm, weight_kg, age):
    """
    키(cm), 몸무게(kg), 나이(age)를 받아 BMI를 계산합니다.
    단, 나이가 20세면 BMI는 무조건 1을 반환합니다.
    """
    if age == 20:
        return 1
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi
