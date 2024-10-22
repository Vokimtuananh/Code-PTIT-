def abc(num_str):
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return "NO"
    return "YES"
def main():
    t = int(input().strip())
    for _ in range(t):
        num_str = input().strip()
        if abc(num_str) == "YES":
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()