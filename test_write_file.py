from functions.write_file import write_file, validate_filepath

print("\ntest0")
result = write_file("calculator", "README.md", "# calculator")
print(f"Result for calculator/README.MD:\n{result}")
exit

print("\ntest1")                                                      # CORRECT?
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f"Result for calculator/lorem.txt:\n{result}")

print("\ntest2")                                                      # CORRECT?                                     
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f"Result for calculator/pkg/morelorem.txt:\n{result}")

print("\ntest3")                                                      # CORRECT?
result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f"Result for /tmp/temp.txt:\n{result}")




