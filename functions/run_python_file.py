import os
import sys
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes the content of a Python file to run tests in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to a specific file relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "description": "Optional arguments",
                    "items": {
                        "type": "string",
                        "description": "Each argument is a string"
                    }
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
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    except:
        return "Error: in standard library call in function: validate_filepath"

    if not os.path.isfile(target_dir):  
        return f'Error: "{file_path}" does not exist or is not a a regular file'

    if not target_dir.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    return target_dir


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:
        return_msg = validate_filepath(working_directory, file_path) 
        if return_msg[0:6] == "Error:":
            return return_msg
        else:
            target_dir = return_msg

        command = ["python", return_msg]

        #print(f"args: {args}")
        if args != None:
            command.extend(args)                # if args exist, extend the command
        #command.extend(['capture_output=True'])  #i.e STDOUT & STDERR
        #command.extend(['text=True'])            # decode output to strings not bytes
        #command.extend(['timeout=30'])           # in seconds

        #print(f"command: {command}")
        result = subprocess.run(command, capture_output=True, text=True, timeout=30 )
    
        return_msg = ""
        if result.returncode != 0:
            return_msg += f'\nProcess exited with code {result.returncode}' 

        if result.stdout == None and result.stderr == None:
            return_msg += f'\nNo output produced'

        if result.stdout != None:
            return_msg += "\nSTDOUT: " + result.stdout

        if result.stderr != None:
            return_msg += "\nSTDERR: " + result.stderr   
    
        return return_msg

    except subprocess.CalledProcessError as e: 
        return f"Error: executing Python file: {e.returncode}"
