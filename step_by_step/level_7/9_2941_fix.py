import sys
input = sys.stdin.readline

word = list(input().rstrip())
count = len(word)
for i in range(0, len(word) - 1):
    if i > len(word) - 3:
        if word[i] == 'd' and word[i+1] == '-':
            count -= 1
        elif word[i] == 'c' and word[i+1] == '-':
            count -= 1
        elif word[i] == 'c' and word[i+1] == '=':
            count -= 1
        elif word[i] == 'l' and word[i+1] == 'j':
            count -= 1
        elif word[i] == 'n' and word[i+1] == 'j':
            count -= 1
        elif word[i] == 's' and word[i+1] == '=':
            count -= 1
        elif word[i] == 'z' and word[i+1] == '=':
            count -= 1
    else:
        if word[i] == 'c' and word[i+1] == '-':
            count -= 1
        elif word[i] == 'c' and word[i+1] == '=':
            count -= 1
        elif word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=': # 마지막 예외 처리 ?
            count -= 1
        elif word[i] == 'd' and word[i+1] == '-':
            count -= 1
        elif word[i] == 'l' and word[i+1] == 'j':
            count -= 1
        elif word[i] == 'n' and word[i+1] == 'j':
            count -= 1
        elif word[i] == 's' and word[i+1] == '=':
            count -= 1
        elif word[i] == 'z' and word[i+1] == '=':
            count -= 1
print(count)
################################################################ fix 2 (i - 1) 개념으로 접근하자
a = input()
n = len(a)
for i in range (n):
	if a[i] == "=":
		if (i > 1) and (a[i - 1] == "z") and (a[i - 2] == "d"):
			n -= 2
		else:
			n -= 1
	elif a[i] == "-":
		n -= 1
	elif a[i] == "j":
		if (a[i - 1] == "l") or (a[i - 1] == "n"):
			n -= 1
print(n)
