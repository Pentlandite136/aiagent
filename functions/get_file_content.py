import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lists the content of a file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to a specific file relative to the working directory (default is the working directory itself)",
                }
            }
        }   
    }
}


def validate_filepath(working_directory: str, file_path: str) -> str:
    try:
        absolute_wd_path = os.path.abspath(working_directory)
        #print(f"absolute_wd_path: {absolute_wd_path}")
        
        stripped_file_path = file_path.strip()   # remove any leading & trailing whitespace
        start_index = 0                          # assume starting char is non-slash
        if stripped_file_path[0] == "/":         # is it?
            start_index = 1                      # ignore it, or BAD things happen when we .join()cd 

        #print(f"start_index: {start_index}")    

        target_dir_joined = os.path.join(absolute_wd_path, file_path[start_index:])
        #print(f"target_dir_joined: {target_dir_joined}")
        
        target_dir = os.path.normpath(target_dir_joined)
        #print(f"target_dir: {target_dir}")
 
        common_path = os.path.commonpath([absolute_wd_path, target_dir])
        #print(f"common_path: {common_path}")
 
        valid_target_dir  = os.path.commonpath([absolute_wd_path, target_dir]) == absolute_wd_path
        #print(f"valid_target_dir: {valid_target_dir}")
        
        if not valid_target_dir or file_path[0] == "/":
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    except:
        return "Error: in standard library call in function: validate_filepath"


    if os.path.isdir(target_dir):  
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # MAX_CHARS = 10000
    try:
        with open("config.py", "r") as config_file:     # improve hard-coded path to config file later
            config_file_string = config_file.read()     
    except FileNotFoundError:
        return f"Error: file 'config.py' does not exist"
    except PermissionError:
        return f"Error: You do not have permission to access file '{config.py}' "
    except OSError as e:
        return f"Error: System error occurred: {e}" 

    param_list = config_file_string.split("\n")
    found = False 
    for param in param_list:
        param_key_value_list = param.split("=")
        if param_key_value_list[0] == "MAX_CHARS":
            max_read_value = int(param_key_value_list[1])
            found = True
            break

    # print(f"max_read_value: {max_read_value}")

    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(max_read_value)
            if f.read(1):
                file_content_string += f'[...File "{target_dir}" truncated at {max_read_value} characters]'
    except FileNotFoundError:
        return f"Error: file '{target_dir}' does not exist"
    except PermissionError:
        return f"Error: You do not have permission to access file '{target_dir}' "
    except OSError as e:
        return f"Error: System error occurred: {e}" 

    return file_content_string


def get_file_content(working_directory: str, file_path: str) -> str:

    return_msg = validate_filepath(working_directory, file_path) 

    return return_msg  

