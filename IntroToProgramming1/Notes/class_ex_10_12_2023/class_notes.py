def main():
    word_count = ["a", "e", "i", "o", "u"]
    userStr = str(input())
    userStr = userStr.lower()
    cnt = 0

    for i in userStr:
        if i == word_count:
            cnt += 1
    print(cnt)
main()