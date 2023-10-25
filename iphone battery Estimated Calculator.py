# 아이폰 모델별 런닝타임 정보 (시간)
iphone_runtimes = {
    "7": 4,
    "7+": 4,
    "8": 4,
    "8+": 5,
    "x": 4,
    "xs": 5,
    "xs max": 5,
    "xr": 2,
    "11": 6,
    "11 pro": 7,
    "11 pro max": 8,
    "12": 7,
    "12 Pro": 8,
    "12 pro max": 8,
    "12 mini": 5,
    "13": 8,
    "13 pro": 8,
    "13 pro max": 9,
    "13 mini": 7,
    "14": 9,
    "14 pro": 8,
    "14 pro max": 10,
    "14+": 10,
    "15": 9,
    "15 pro": 9,
    "15 pro max": 12,
    "15+": 13,
    "se": 3,
}

# 아이폰 모델의 지원 여부를 확인하는 함수
def is_supported_model(model):
    return model in iphone_runtimes

# 아이폰 모델과 배터리 성능 최대치(%)를 입력받아 런닝타임을 계산하는 함수
def calculate_runtime(model, battery_percentage):
    if is_supported_model(model):
        runtime = iphone_runtimes[model]
        estimated_runtime = runtime * (battery_percentage / 100)
        return estimated_runtime
    else:
        return None

# 사용자 입력을 받고 적절한 데이터 타입으로 변환하는 함수
def get_user_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        try:
            user_input = data_type(user_input)
            return user_input
        except ValueError:
            print("올바른 형식으로 입력해주세요.")

# 배터리 성능 최대치 입력 함수
def get_battery_percentage():
    print("설정>배터리>배터리 성능 상태 및 충전>성능 최대치 확인")
    return get_user_input("배터리 성능 최대치(%)를 입력하세요: ", float)

# 아이폰 모델 입력 함수
def get_iphone_model():
    while True:
        iphone_model = get_user_input("귀하의 아이폰 모델 (7부터 15까지, SE도 포함 영어는 소문자로 작성): ", str)
        if is_supported_model(iphone_model):
            return iphone_model
        else:
            print("지원하지 않는 아이폰 모델입니다.")

# 메인 실행 함수
def main():
    iphone_model = get_iphone_model()
    battery_percentage = get_battery_percentage()

    estimated_runtime = calculate_runtime(iphone_model, battery_percentage)
    if estimated_runtime is not None:
        print(f"{iphone_model}의 예상 러닝타임은 약 {estimated_runtime:.2f} 시간입니다.")
    else:
        print("지원하지 않는 아이폰 모델입니다.")

# 프로그램 시작
if __name__ == "__main__":
    main()

