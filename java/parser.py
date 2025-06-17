import javalang

def parse_java_classes(code):
    tree = javalang.parse.parse(code)
    classes = []
    for path, node in tree.filter(javalang.tree.ClassDeclaration):
        methods = [m.name for m in node.methods]
        classes.append({
            "name": node.name,
            "methods": methods,
            "extends": node.extends.name if node.extends else None
        })
    return classes

if __name__ == "__main__":
    with open("Sample.java") as f:
        code = f.read()
    from pprint import pprint
    pprint(parse_java_classes(code))
