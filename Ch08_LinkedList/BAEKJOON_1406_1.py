# https://www.acmicpc.net/problem/1406

lst = list(input())
command_count = int(input())
print(lst, command_count)

cursor = len(lst)
for _ in range(command_count):
    command = input().split()
    if command[0] == 'P':
        if cursor == len(lst):
            lst.append(command[1])
            cursor += 1
        else:
            lst.insert(cursor, command[1])
            cursor += 1
    elif command[0] == 'L' and cursor > 0:
        cursor -= 1
    elif command[0] == 'B' and cursor > 0:
        del lst[cursor - 1]
        cursor -= 1
    elif command[0] == 'D' and cursor != len(lst):
        cursor += 1

print("".join(lst))
