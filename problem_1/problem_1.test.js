const fs = require('fs');

const expectedAnswers = JSON.parse(fs.readFileSync('problem_1_expected_answers.json'));
import { euler_1 } from './problem_1.js';

let successfulTests = 0;
const failedTests = [];

expectedAnswers.forEach((expectedAnswer) => {
    console.log(`Input of ${expectedAnswer.input} should yield ${expectedAnswer.expected_answer}`);
    let success = false;
    let formatCharacter = "\033[1;31m";
    const closingFormatCharacter = "\033[0m";
    let answer = euler_1(expectedAnswer.input);
    if (answer === expectedAnswer.expected_answer) {
        succesfulTests++;
        success = true;
        formatCharacter = "\033[1;32m";
    } else {
        failedTests.push({
            'input': expectedAnswer.input,
            'expectedAnswer': expectedAnswer.expected_answer,
            'actualAnswer': answer
        });
    }
    console.log(`${formatCharacter}Input of ${expectedAnswer.input} yields ${answer}${closingFormatCharacter}`);
});

const totalTests = successfulTests + failedTests.length;
console.log(`\033[1mTotal tests: ${totalTests}\033[0m`);
console.log(`\033[1;32mSuccessful tests: ${successfulTests} (${successfulTests * 100 / totalTests}%)\033[0m`);
if (failedTests.length > 0) {
    console.log(`\033[1;31mFailed tests: ${failedTests.length} (${failedTests.length * 100 / totalTests}%)\033[0m`);
    failedTests.forEach((test) => {
        console.log(`\033[1;31mInput of ${test.input} should have yielded ${test.expectedAnswer} but yields ${test.actualAnswer}\033[0m]`);
    });
}