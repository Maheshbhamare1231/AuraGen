
const parser = require("@babel/parser");

/**
 * Validate React JSX code using Babel.
 */
function validateJSX(code) {
    try {
        parser.parse(code, {
            sourceType: "module",
            plugins: ["jsx"]
        });

        return {
            valid: true,
            message: "React JSX syntax is valid."
        };

    } catch (error) {
        return {
            valid: false,
            message: error.message,
            line: error.loc ? error.loc.line : null,
            column: error.loc ? error.loc.column : null
        };
    }
}

// Read JSX code from standard input
let input = "";

process.stdin.setEncoding("utf8");

process.stdin.on("data", (chunk) => {
    input += chunk;
});

process.stdin.on("end", () => {
    try {
        const result = validateJSX(input);
        console.log(JSON.stringify(result));
    } catch (error) {
        console.log(JSON.stringify({
            valid: false,
            message: error.message
        }));
        process.exitCode = 1;
    }
});

// Export function for possible future use
module.exports = { validateJSX };
