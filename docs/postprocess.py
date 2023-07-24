
import sys

def modify_html(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        html_content = file.read()

    split_str_1 = '"><code class="docutils literal notranslate"><span class="pre">'
    split_str_2 = "."

    new_content = []
    for line in html_content.split('\n'):
        if split_str_1 in line:
            s1, s2 = line.split(split_str_1)
            if split_str_2 in s2:
                s3, s4 = s2.split(split_str_2, 1)  # using 1 to split at the first dot only
                new_line = "".join([s1, split_str_1, split_str_2, s4])
                new_content.append(new_line)
            else:
                new_content.append(line)
        else:
            new_content.append(line)

    html_content_modified = '\n'.join(new_content)

    with open(file_path, 'w', encoding='utf8') as file:
        file.write(html_content_modified)

if __name__ == '__main__':
    modify_html(sys.argv[1])
