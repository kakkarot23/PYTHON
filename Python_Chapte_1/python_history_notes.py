
# =============================================================
# 🐍 PYTHON HISTORY & THEORY NOTES
# =============================================================

# 📖 Introduction
# Python is a high-level, interpreted programming language created by Guido van Rossum in 1989.
# It was officially released in 1991. Python emphasizes code readability and simplicity.
# The name "Python" was inspired by the British comedy group "Monty Python".

# -------------------------------------------------------------
# 🕰️ Timeline of Python Versions and Evolution
# -------------------------------------------------------------

# 1980s: ABC Language
# Guido van Rossum worked on a language called ABC at CWI (Centrum Wiskunde & Informatica) in the Netherlands.
# Python was designed as a successor to ABC, improving its limitations while maintaining its ease of use.

# 1989: Birth of Python
# Guido started implementing Python during Christmas holidays as a hobby project.

# 1991: Python 0.9.0 Released
# - Included features like: functions, exception handling, and core data types (str, list, dict).
# - Also introduced modules and the concept of namespaces.

# 1994: Python 1.0 Released
# - Introduced lambda, map(), filter(), and reduce() functions.
# - Marked Python’s first major public adoption.

# 2000: Python 2.0 Released
# - Introduced list comprehensions, garbage collection, Unicode support.
# - Set the foundation for modern Python.
# - However, it created backward compatibility issues later.

# 2008: Python 3.0 Released
# - Major redesign of the language; not backward compatible with Python 2.
# - Emphasized clarity and consistency (e.g., print() became a function).
# - Added better Unicode handling, new libraries, and simplified syntax.

# 2020: Python 2 officially retired
# - Python 3 became the only officially supported version.
# - Most modern systems and frameworks now run exclusively on Python 3.

# 2023–2025: Python continues evolving
# - Improved pattern matching, async features, type hints, and performance.
# - Python 3.12 (and beyond) focuses on speed and better runtime memory management.

# -------------------------------------------------------------
# 🧩 Python Philosophy (The Zen of Python)
# -------------------------------------------------------------

# Accessible by typing `import this` in Python interpreter.
# Written by Tim Peters, it summarizes Python’s guiding principles:

# - Beautiful is better than ugly.
# - Explicit is better than implicit.
# - Simple is better than complex.
# - Readability counts.
# - Errors should never pass silently.

# -------------------------------------------------------------
# 💡 Key Features of Python
# -------------------------------------------------------------

# 1. Interpreted Language: Code runs line by line (no compilation step).
# 2. Dynamically Typed: No need to declare variable types explicitly.
# 3. High-Level: Easy to write, read, and maintain.
# 4. Object-Oriented: Supports classes, inheritance, polymorphism.
# 5. Portable: Works on Windows, macOS, Linux, etc.
# 6. Extensive Libraries: Offers modules for data science, AI, web, automation, etc.
# 7. Open Source: Freely available and community-driven.

# -------------------------------------------------------------
# 🧠 Python Applications
# -------------------------------------------------------------

# Python is widely used across many domains:

# - Web Development: Django, Flask, FastAPI
# - Data Science: Pandas, NumPy, Matplotlib
# - Artificial Intelligence: TensorFlow, PyTorch, Scikit-learn
# - Automation: Selenium, PyAutoGUI, OS scripting
# - Game Development: Pygame, Panda3D
# - Cybersecurity & Ethical Hacking: Scapy, Nmap libraries
# - IoT & Robotics: MicroPython, Raspberry Pi
# - Education: First language for programming learners

# -------------------------------------------------------------
# 🔢 Python Syntax Examples (Brief Overview)
# -------------------------------------------------------------

# Variables and Data Types
x = 10
y = "Hello, Python!"
z = [1, 2, 3, 4]

# Conditional Statements
if x > 5:
    print("X is greater than 5")

# Loops
for i in range(3):
    print("Loop iteration:", i)

# Functions
def greet(name):
    return f"Hello, {name}"

# Object-Oriented Example
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# -------------------------------------------------------------
# 🧱 Modern Python Features (3.x)
# -------------------------------------------------------------

# - Type Hints
def add(a: int, b: int) -> int:
    return a + b

# - F-Strings for Formatting
name = "Jayesh"
print(f"Welcome, {name}")

# - List Comprehensions
squares = [i**2 for i in range(5)]

# - Async Programming
# async def fetch_data():
#     await some_async_operation()

# -------------------------------------------------------------
# 🧩 Conclusion
# -------------------------------------------------------------

# Python has evolved into one of the most versatile and beginner-friendly languages in history.
# From simple scripts to AI-driven systems, Python continues to be the foundation for innovation.
# It blends simplicity, power, and scalability — a true “Swiss Army knife” of programming.

