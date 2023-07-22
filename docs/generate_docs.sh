#!/bin/bash

# Step 0: Clean-up
echo "Cleaning up..."
rm -rf ./source/konanai

# Step 1: Generate .rst files for all modules and scripts
echo "Generating .rst files..."
sphinx-apidoc -o source/konanai ../src/konanai

# Step 2: Rename .rst files to remove the konanai. prefix
echo "Renaming .rst files..."
find source/konanai -name 'konanai.*.rst' -exec bash -c 'mv "$1" "${1/konanai./}"' _ {} \;

# Step 3: Edit all the .rst files to change the references
echo "Editing .rst file references..."
for file in $(find ./source/konanai -type f -name "*.rst"); do
    sed -i "" "s/konanai.//g" $file
done

# Step 4: Move the modules.rst file to the source directory
echo "Moving modules.rst file..."
mv ./source/konanai/modules.rst ./source/

echo "Done!"
