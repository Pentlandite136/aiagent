from functions.run_python_file import run_python_file, validate_filepath

print("\ntest1")                                                      # should print calc usage instructions; PASSED
result = run_python_file("calculator", "main.py")
print(f"Result for calculator/main.py:\n{result}")

print("\ntest2")                                                      # should run calc result; PASSED                                    
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(f'Result for calculator/main.py ["3 + 5"]:\n{result}')

print("\ntest3")                                                      # should run calc tests; PASSED
result = run_python_file("calculator", "tests.py")
print(f"Result for calculator/tests.py:\n{result}")

print("\ntest4")                                                      # should return an error; PASSED
result = run_python_file("calculator", "../main.py")
print(f"Result for calculator/../main.py:\n{result}")

print("\ntest5")                                                      # should return an error; PASSED
result = run_python_file("calculator", "nonexistent.py")
print(f"Result for calculator/nonexistent.py:\n{result}")

print("\ntest6")                                                      # should return an error; PASSED
result = run_python_file("calculator", "lorem.txt")
print(f"Result for calculator/lorem.txt:\n{result}")


