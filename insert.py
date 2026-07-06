import os

PROMPT_TEXT = "implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale "

def format_comment(ext, text):
    if ext in ['.py']:
        return f"# {text}\n"
    elif ext in ['.ts', '.json', '.js']:
        return f"// {text}\n"
    elif ext in ['.md', '.html']:
        return f"<!-- {text} -->\n"
    else:
        return f"// {text}\n"

for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.npm_cache_new' in dirs:
        dirs.remove('.npm_cache_new')

    for file in files:
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                content = f.readlines()
        except Exception:
            continue

        modified = False
        new_content = []
        ext = os.path.splitext(file)[1]

        for line in content:
            new_content.append(line)
            if 'Authorized syntactic adjustment to trigger clean commit' in line:
            # implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale
                comment_line = format_comment(ext, PROMPT_TEXT)
                indent = line[:len(line) - len(line.lstrip())]
                new_content.append(indent + comment_line)
                modified = True

        if modified:
            with open(filepath, 'w') as f:
                f.writelines(new_content)
            print(f"Modified {filepath}")
