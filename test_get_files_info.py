from functions.get_files_info import get_files_info

print("test1")
my_table = get_files_info("calculator", ".")
print("Result for current directory:\n" + my_table)

print("test2")                                      # THIS TEST CASE IS NOT BEING HANDLED CORRECTLY
my_table = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:\n" + my_table)

print("test3")
my_table = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:\n" + my_table)

print("test4")
my_table = get_files_info("calculator", "../")
print("Result for '../' directory:\n" + my_table)



