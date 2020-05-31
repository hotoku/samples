import { helloTest } from "../src/hello";
import { Line, Point, quickhul } from "../src/quickhul";
import { expect } from "chai";
import "mocha";



function nearly_equal(x: number, y: number): boolean{
    return Math.abs(x - y) < 0.000001;
}

describe("Line", () => {
    it("should be 0", () => {
        const p1 = new Point(1, 0);
        const p2 = new Point(0, 1);
        const p3 = new Point(0, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            0
        );
        expect(ret).to.equal(true);
    });

    it("should be 1", () => {
        const p1 = new Point(0, 0);
        const p2 = new Point(1, 0);
        const p3 = new Point(1, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            1
        );
        expect(ret).to.equal(true);
    });

    it("should be 1", () => {
        const p1 = new Point(100, 0);
        const p2 = new Point(101, 0);
        const p3 = new Point(101, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            1
        );
        expect(ret).to.equal(true);
    });

    it("should be -1", () => {
        const p1 = new Point(0, 0);
        const p2 = new Point(1, 0);
        const p3 = new Point(1, -1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            -1
        );
        expect(ret).to.equal(true);
    });

    it("should be 1", () => {
        const p1 = new Point(0, 0);
        const p2 = new Point(0, 1);
        const p3 = new Point(1, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            -1
        );
        expect(ret).to.equal(true);
    });

    it("should be -1", () => {
        const p1 = new Point(0, 0);
        const p2 = new Point(0, 1);
        const p3 = new Point(-1, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            1
        );
        expect(ret).to.equal(true);
    });

    it("should be 1", () => {
        const p1 = new Point(0, 0);
        const p2 = new Point(0, 1);
        const p3 = new Point(1, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            -1
        );
        expect(ret).to.equal(true);
    });

    it("should be sqrt(2)", () => {
        const p1 = new Point(-1, -1);
        const p2 = new Point(1, 1);
        const p3 = new Point(-1, 1);
        const l = new Line(p1, p2);
        const ret = nearly_equal(
            l.distance(p3),
            Math.sqrt(2)
        );
        expect(ret).to.equal(true);
    });
})

describe("quickhul", () => {
    it("should return 4 points", () => {
        const ps = [
            new Point(-1, 0),
            new Point(0, -1),
            new Point(1, 0),
            new Point(0, 1),
            new Point(0, 0),
        ]
        const ret = quickhul(ps);
        expect(ret.length).to.equal(4);
    })
});
