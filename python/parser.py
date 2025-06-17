import ast

def parse_python_classes(code):
    tree = ast.parse(code)
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)],
                "base_classes": [b.id for b in node.bases if isinstance(b, ast.Name)]
            }
            classes.append(class_info)
    return classes

if __name__ == "__main__":
    with open("sample.py") as f:
        code = f.read()
    from pprint import pprint
    pprint(parse_python_classes(code))
