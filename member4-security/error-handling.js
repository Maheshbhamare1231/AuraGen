
const fs = require("fs");

try {
    const data = fs.readFileSync("ui.json", "utf8");

    const config = JSON.parse(data);

    console.log("JSON file loaded successfully!");
    console.log("Project:", config.project);

} catch (error) {
    console.log("Error occurred:", error.message);
}
