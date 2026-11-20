
const { isComponentAllowed } = require("./security-utils");

const components = [
    "Button",
    "Card",
    "Script",
    "Input",
    "iframe"
];

components.forEach((name) => {
    if (isComponentAllowed(name)) {
        console.log(name + " - Allowed");
    } else {
        console.log(name + " - Rejected");
    }
});
