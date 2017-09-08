1. len('deed') == 4     'bit' in 'habit'

2. 0

3. dance_style[-4]      dance_style[3]

4. title[2]

5. s[-5:]   s[4:9]

6. madam

7. 'abc123'.isalnum()   'apple'.upper() == 'APPLE'

8. s.isalpha() or s.isnumeric()     s.lower() or s.upper() or s.isdigit()

9. s1.rfind(s2)

10. 55

11. 9

12. 00112233445566778899

13. message = 'Happy 29th!'
new_message = ''
for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char
print(new_message)


message = 'Happy 29th!'
new_message = ''

for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)

print(new_message)


14. for ch in s1:
        if ch in s2:
            res = res + ch




