import os
import ast

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith('.py'):
                print('{}{}'.format(subindent, f))
                try:
                    parse_python_file(os.path.join(root, f), subindent)
                except SyntaxError:
                    print(f"Skipping file {f} due to SyntaxError")

def parse_python_file(file, indent):
    with open(file, "r") as source:
        try:
            tree = ast.parse(source.read())
            classes = [node.name for node in ast.walk(tree) if isinstance(node, 
ast.ClassDef)]
            for c in classes:
                print('{}{}'.format(indent + '    ', c))
        except SyntaxError:
            raise

# Provide the directory you want to start from
list_files('src')

