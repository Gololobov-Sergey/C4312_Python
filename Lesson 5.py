import string

st = "програмування на 2025 python 2025 2025"
print(st)
# for s in st:
#     print(s)

# print(st[-1])
# print(st[:8])
# print(st[6:])
# print(st[::-1])

print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.title())
print(st.count("2", 1, 20))
print(st.startswith("пр"))
# print(input().endswith(input()))
print(st.find("20252"))
print(st.rfind("2025"))
print(st.index("2025"))
print("12a43".isdigit())
print(st[17].isdigit())
print("12a43".isalpha())
print("12a43".isspace())
print("P2a43".istitle())
print("P2a43".isalnum())
print("P2a43".islower())
print("P2a43".isupper())
print("P2a43".isprintable())
print("mama".ljust(20), "papa")
print("mama".rjust(20), "papa")
print("mama".center(20), "papa")

p = 0.14
print(f"Pi = {p:>10.4f}")
print(f"{p:>10.4%}")

d=18
m=3
y=2025
print(f"{str(d).zfill(2)}.{str(m).zfill(2)}.{y}")

print(string.ascii_letters)
print(string.digits)

corr("mama", 10, "+")
# +++mama+++