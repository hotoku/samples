import { helloTest } from '../src/hello';
import { expect } from 'chai';
import 'mocha';

describe('First test', () => {    
    it('should return true', () => {
        console.log("hello");
        const result = helloTest();
        expect(result).to.equal(true);
    });
    
});
