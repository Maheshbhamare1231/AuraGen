
const allowedComponents = [
    "Button",
    "Text",
    "Card",
    "Input",
    "Container",
    "Image",
    "Form"
];

function checkComponent(component) {

    if (allowedComponents.includes(component)) {
        return component + " is Allowed";
    } else {
        return component + " is Rejected";
    }

}

console.log(checkComponent("Button"));
console.log(checkComponent("Card"));
console.log(checkComponent("Script"));
console.log(checkComponent("iframe"));
console.log(checkComponent("Input"));
console.log(checkComponent("Image"));
console.log(checkComponent("Form"));
console.log(checkComponent("Script"));
console.log(checkComponent("Video"));