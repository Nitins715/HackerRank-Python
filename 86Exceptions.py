test_cases = int(input())
test_cases_list = [input().split(" ") for _ in range(test_cases)]
    
for num in test_cases_list:
    try:
        print(int(num[0]) // int(num[1]))
    except Exception as e:
        print(f"Error Code: {e}")