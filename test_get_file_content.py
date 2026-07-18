from functions.get_file_content import get_file_content, validate_filepath

print("\ntest0")                                                      
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

print("\ntest1")                                                      # CORRECT
result = get_file_content("calculator", "main.py")
print(f"Result for calculator/main.py directory:\n{result}")

print("\ntest2")                                                      # CORRECT                                     
result = get_file_content("calculator", "pkg/calculator.py")
print(f"Result for pkg/calculator.py:\n{result}")

print("\ntest3")                                                      # CORRECT
result = get_file_content("calculator", "/bin/cat")
print(f"Result for /bin/cat:\n{result}")

print("\ntest4")                                                        # CORRECT
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"Result for calculator/pkg/does_not_exist.py\n{result}")



