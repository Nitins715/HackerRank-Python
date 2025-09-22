import re

pattern =r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"

def fun(s):
    return re.match(pattern, s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)