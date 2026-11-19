
const config = {
    project: "AuraGen",
    member: 4,
    module: "Security",
    active: true
};

// Convert JavaScript object into JSON text
const jsonText = JSON.stringify(config, null, 2);

console.log("Converted JSON:");
console.log(jsonText);
