import pycparser
import os

def parse_function(node):
    if node.type == 'FuncDef':
        function_name = node.name.name
        function_body = node.body.block_items

        function_file_name = f"{function_name}.c"
        print(function_file_name)

        with open(function_file_name, 'w') as outfile:
            for statement in function_body:
                statement_str = pycparser.CParser.emit(statement)
                outfile.write(statement_str + '\n')

def parse_file(filename):
    parser = pycparser.CParser()
    ast = parser.parse(filename)

    for node in ast.ext:
        parse_function(node)

if __name__ == '__main__':
    filename = 'input.c'
    parse_file(filename)
    
    # print the number of files in the current directory
    num_files = len(os.listdir())
    print(f"Number of files outputted: {num_files}")
