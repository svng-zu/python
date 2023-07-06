# cnt = 0 #12의 배수의 개수를 저장하기 위한 변수
# loop = 0 #조건 확인한 개수를 저장하기 위한 변수
#
# for idx in range(0 , 100) :
#     loop = loop + 1
#     if idx % 4 == 0 :
#         loop = loop +1
#         if idx % 3 == 0 :
#             cnt = cnt + 1
#
# print("12의 배수 개수" , cnt ,  "조건 확인 개수" , loop)
# 화이트 박스 테스트 => 동작이 효율적인가? 내부 구조 확인
# 블랙 박스 테스트 => 결과 값이 옳은가? 외부 구조 확인
#
# year = 2023
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print(year, "는 윤년이 아님")
# else :
#     print(year, "는 윤년 임")

print("{0} 은 {1}을 좋아합니다.".format("아담", "신촌 라이브 카페"))