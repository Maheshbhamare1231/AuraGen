
const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "ui.json");

const data = fs.readFileSync(filePath, "utf8");
const config = JSON.parse(data);

console.log("Project:", config.project);
console.log("Module:", config.module);
console.log("Components:");

config.components.forEach((component) => {
    console.log(
        component.name,
        "-",
        component.allowed ? "Allowed" : "Rejected"
    );
});
