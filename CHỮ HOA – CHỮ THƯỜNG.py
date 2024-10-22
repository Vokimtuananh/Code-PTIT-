def transform_string(s):
    lower_count = sum(1 for c in s if c.islower())
    upper_count = sum(1 for c in s if c.isupper())
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()
s = input()
print(transform_string(s))