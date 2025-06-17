# Simple regex-based structure for C/C++
import re

def parse_c_cpp(code):
    class_pattern = re.compile(r'class\s+(\w+)', re.MULTILINE)
    function_pattern = re.compile(r'(\w[\w\s\*]+)\s+(\w+)\s*\(.*\)', re.MULTILINE)

    classes = class_pattern.findall(code)
    functions = function_pattern.findall(code)

    return {"classes": classes, "functions": [f[1] for f in functions]}

if __name__ == "__main__":
    with open("sample.cpp") as f:
        code = f.read()
    from pprint import pprint
    pprint(parse_c_cpp(code))
