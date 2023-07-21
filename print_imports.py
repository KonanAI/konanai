import os
import re

def find_imports(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    # Patterns for import statements
    import_patterns = [r'^import .+', r'^from .+ import .+']

    for line in lines:
        for pattern in import_patterns:
            if re.match(pattern, line.strip()):
                print(line.strip())

# Walk the directory
for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.py'):
            find_imports(os.path.join(root, file))

