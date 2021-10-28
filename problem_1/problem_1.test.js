import { expect } from 'chai';
import 'mocha';
const fs = require('fs');

const answers = JSON.parse(fs.readFileSync('problem_1_expected_answers.json'));
import { euler_1 } from './problem_1.js';

answers.forEach((answer) => {
    describe(`Input: ${answer.input}`, () => {
        it(`should be ${answer.expected_answer}`, () => {
            expect(euler_1(answer.input)).to.equal(answer.expected_answer);
        });
    });
});