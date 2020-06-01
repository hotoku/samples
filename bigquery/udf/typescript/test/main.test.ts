import { f } from "../src/main";
import { expect } from "chai";
import "mocha";

describe("main", () => {
    it("should double argument", () => {
        expect(f(1)).to.equal(2);
    })
})
