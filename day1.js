const projectName = "AuraGen";
const moduleName = "AST Injector";
const memberNumber = 4;

console.log("Project:", projectName);
console.log("Module:", moduleName);
console.log("Member:", memberNumber);

function validateOutput(output) {
    if (output === null || output === undefined) {
        return "Invalid Output";
    }

    return "Output Received";
}

console.log(validateOutput("React Component"));
console.log(validateOutput(null));