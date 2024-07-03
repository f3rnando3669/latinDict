from typing import List
import re
from FileUtilities import readfile

def remove_headings(arr: List[str]) -> List[str]:
    """
    takes an array of sentences
    produces an array that omits headings
    """
    rv = []
    for line in arr:
        line = re.sub(r"[0-9]. \*\*([a-zA-Z]* [a-zA-Z]*)*\*\*:", r"", line)
        if line:
            rv.append(line)
    
    return rv

def remove_indent_spacing(arr: List[str]) -> List[str]:
    """
    takes an array of sentences
    produces an array that has sentences reformatted to have no tab indentation
    """
    rv = []
    for line in arr:
        line = line.strip()
        if line:
            rv.append(line + "\n")
    
    return rv

def remove_line_spacing(text: str) -> str:

    rv = ""
    window_length = 0

    for i in range(len(text)):
        if text[i] != '\n':
            if window_length > 0:
                rv += "\n"
                window_length = 0
            rv += text[i]
        else:
            window_length += 1
    
    return rv

def r_enforce_prompt(text, starts_with, prompt_tail, delimiter="\n", start=0, end=0):
    if end == 0:
        end = len(text)
    lines = text.split(delimiter)
    unrelated = []
    complete = []
    incomplete = []
    enforce = False
    # print(lines)
    for i, line in enumerate(lines):
        if i < start:
            continue
        if i > end:
            break
        line = line.strip()
        if line.startswith(starts_with):
            if line:
                # print(line)
                line_arr = line.split(" ")

                if f"{prompt_tail}" in line_arr:
                    complete.append(line+"\n")
                else:
                    incomplete.append(line + f",{prompt_tail}\n")
                    # print(line_arr)
                    if not enforce:
                        enforce = True
        else:
            unrelated.append(line)

    return "".join(complete+incomplete).rstrip(), enforce

def get_start(text, prefix_pattern=r"- "):
    prefix = re.sub(prefix_pattern, r"\1", text)
    return prefix

def get_shot_prompt(path, starts_with, prompt_tail, start=0, end=0):
    text = readfile(path)
    prompt, _ = r_enforce_prompt(text, starts_with=starts_with, prompt_tail=prompt_tail, start=start, end=end)
    return prompt
