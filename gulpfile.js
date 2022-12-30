const { series } = require("gulp");

async function test() {
    await console.log("Test");
}

async function tick() {
    await console.log("Tick");
}

exports["default"] = test;
exports["test"] = series(test, tick);


