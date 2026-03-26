import time

text = "insert text here"
n = len(text)

frames = [             ]

for x in range(n):
    frames.append(" " * x + text)

for y in range(n - 2, -1, -1):
    frames.append(" " * y + text)

while True:
    for i in frames:
        print(i)
        time.sleep(0.07)

"""hello
 hello
  hello
   hello
    hello
   hello
  hello
 hello
hello
hello
 hello
  hello
   hello
    hello
   hello
  hello
 hello
hello
hello
 hello
  hello
   hello
    hello
   hello
  hello
 hello
hello """
