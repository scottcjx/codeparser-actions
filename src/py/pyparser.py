import ast

def parse_function(node):
    if isinstance(node, ast.FunctionDef):
        function_name = node.name
        function_body = node.body

        function_file_name = f"{function_name}.py"

        with open(function_file_name, 'w') as outfile:
            for statement in function_body:
                statement_str = ast.to_source(statement)
                outfile.write(statement_str + '\n')

def parse_file(filename):
    with open(filename, 'r') as infile:
        source_code = infile.read()

    ast_tree = ast.parse(source_code)

    for node in ast_tree.body:
        parse_function(node)

if __name__ == '__main__':
    filename = 'input.py'
    parse_file(filename)
