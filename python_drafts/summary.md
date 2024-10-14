
# Code Summaries

## 1. Read N characters from a file
```python
file = open("/usercode/files/books.txt")

N = int(input("Enter the number of characters to read: "))

try:
    content = file.read(N)
    print(content)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()
```
### Summary:
- This program reads the first `N` characters from the `books.txt` file. 
- It takes user input for `N`, reads the characters, and prints them. 
- The `try-except-finally` structure ensures that errors are handled and the file is closed properly.

---

## 2. Handle Input Errors for Numeric Values
```python
def withdraw(amount):
    print(str(amount) + " withdrawn!")

amount = input()
try:
    amount = int(amount)  
    withdraw(amount)
except ValueError:
    print("Please enter a number")
```
### Summary:
- This program simulates a withdrawal by prompting the user for an amount.
- It converts the input to an integer and raises an exception if the input is invalid (non-numeric).
- If a `ValueError` is raised, it prints "Please enter a number".

---

## 3. Count Words in Each Line of a File
```python
with open("/usercode/files/books.txt") as f:
    for line_number, line in enumerate(f, start=1):
        word_count = len(line.split())
        print(f"Line {line_number}: {word_count} words")
```
### Summary:
- This program reads a file and counts how many words each line contains.
- It outputs the word count in the format: `Line {line_number}: {word_count} words`.
- It uses `enumerate` to keep track of the line numbers starting from 1.

---

## 4. Prevent "False" from being printed
```python
condition = False

if not condition:
    pass  
else:
    print('The condition is True')
```
### Summary:
- This example demonstrates how to prevent "False" from being printed.
- If the condition is `False`, the program does nothing using the `pass` statement.
- If the condition is `True`, a message is printed.

---

## 5. Program to Write and Read Numbers from a File
```python
n = int(input())

with open("numbers.txt", "w") as file:
    for i in range(1, n + 1):
        file.write(f"{i}\n")

with open("numbers.txt", "r") as f:
    print(f.read(), end='')
```
### Summary:
- This program writes numbers from 1 to `n` to a file (`numbers.txt`) and then reads and prints the file content.
- It uses two `with` statements to handle writing and reading operations, ensuring the file is properly closed.

