
const allowedComponents = [
    "Button",
    "Text",
    "Card",
    "Input",
    "Container"
];

function isComponentAllowed(componentName) {
    return allowedComponents.includes(componentName);
}

module.exports = {
    isComponentAllowed
};
