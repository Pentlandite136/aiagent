import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                }
            }
        }   
    }
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_wd_path = os.path.abspath(working_directory)
        # print(f"absolute_wd_path: {absolute_wd_path}")
        
        stripped_directory = directory.strip()   # remove any leading & trailing whitespace
        start_index = 0                          # assume starting char is non-slash
        if stripped_directory[0] == "/":         # is it?
            start_index = 1                      # ignore it, or BAD things happen when we .join()cd 

        # print(f"start_index: {start_index}")    

        target_dir_joined = os.path.join(absolute_wd_path, directory[start_index:])
        # print(f"target_dir_joined: {target_dir_joined}")
        
        target_dir = os.path.normpath(target_dir_joined)
        # print(f"target_dir: {target_dir}")
 
        common_path = os.path.commonpath([absolute_wd_path, target_dir])
        # print(f"common_path: {common_path}")

 
        valid_target_dir  = os.path.commonpath([absolute_wd_path, target_dir]) == absolute_wd_path
        # print(f"valid_target_dir: {valid_target_dir}")
        
        if not valid_target_dir or directory[0] == "/":
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # else:
            # return f'Success: "{directory[start_index]:}" is within the working directory'
    except:
        return "Error: in standard library call"  

    file_list = os.listdir(target_dir)
    # print(f"file_list: {file_list}")

    dir_item_list = []
    for file_name in file_list:
        try:
             # print(f"working_dir+file_name: {working_directory + "/" + file_name}")
            file_size = os.path.getsize(target_dir + "/" + file_name)
        except FileNotFoundError:
            return f"Error: file '{file_name}' not found"
        except PermissionError:
            return f"Error: you do not have permission to access file '{file_name}'"

        # print(f"file_size: {file_size}")
        is_dir = os.path.isdir(working_directory + "/" + file_name)
        my_tuple = (file_name, file_size, is_dir)
        dir_item_list.append(my_tuple)
    
    target_directory_contents = ""
    for one_tuple in dir_item_list:
        target_directory_contents += f"- {one_tuple[0]}: file_size={one_tuple[1]} bytes, is_dir={one_tuple[2]}\n"

    # print(target_directory_contents)
    # print(f"dir_item_list: {dir_item_list}")
    return target_directory_contents


    