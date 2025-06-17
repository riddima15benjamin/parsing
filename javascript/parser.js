const esprima = require("esprima");
const fs = require("fs");

const code = fs.readFileSync("sample.js", "utf-8");
const ast = esprima.parseModule(code, { tolerant: true });

function extractClasses(ast) {
    const classes = [];

    function walk(node) {
        if (!node || typeof node !== "object") return;

        if (node.type === "ClassDeclaration") {
            const className = node.id.name;
            const methods = [];

            for (const bodyElement of node.body.body) {
                if (bodyElement.type === "MethodDefinition") {
                    methods.push(bodyElement.key.name);
                }
            }

            classes.push({ name: className, methods: methods });
        }

        for (const key in node) {
            walk(node[key]);
        }
    }

    walk(ast);
    return classes;
}

console.log(JSON.stringify(extractClasses(ast), null, 2));
