import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites a file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to a specific file relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "The text to be written to the file",
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
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    except:
        return "Error: in standard library call in function: validate_filepath"

    if os.path.isdir(target_dir):  
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    #print(f"file_path: {file_path}")
    if not os.path.isfile(file_path):
         os.makedirs(file_path, exist_ok=True)

    return target_dir


def write_file(working_directory: str, file_path: str, content: str) -> str:

    return_msg = validate_filepath(working_directory, file_path) 
    if return_msg[0:6] == "Error:":
        return return_msg
    else:
        target_dir = return_msg

    try:
        with open(target_dir, "w") as f:
            chars_written = f.write(content)
    
    except FileNotFoundError:
        return f"Error: file '{target_dir}' does not exist"
    except PermissionError:
        return f"Error: You do not have permission to access file '{target_dir}' "
    except OSError as e:
        return f"Error: System error occurred: {e}" 

    if len(content) != chars_written:
        return f'Error: not all characters were written to file'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
