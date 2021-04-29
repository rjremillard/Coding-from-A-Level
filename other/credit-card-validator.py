def checkCard(num: str) -> bool:
    sum_ = 0
    for i in range(1, len(num)+1):
        if i % 2:
            prod = int(num[len(num)-i] * 2)
            sum_ += prod // 10 + prod % 10
        else:
            sum_ += int(num[len(num)-i])
    
    return bool(sum_ % 10)


number = input("Credit Card Number: ").replace(" ", "")
print("Valid" if checkCard(number) else "Invalid")
