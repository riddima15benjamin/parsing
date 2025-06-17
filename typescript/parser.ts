const { Project } = require("ts-morph");
const fs = require("fs");

const project = new Project();
const sourceFile = project.addSourceFileAtPath("sample.ts");

const classes = sourceFile.getClasses().map(cls => ({
  name: cls.getName(),
  methods: cls.getMethods().map(m => m.getName())
}));

console.log(JSON.stringify(classes, null, 2));
