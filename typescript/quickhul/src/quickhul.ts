export class Point{
    x: number;
    y: number;

    constructor (x: number, y: number){
        this.x = x;
        this.y = y;
    }

    minus(p: Point): Point{
        return new Point(
            this.x - p.x,
            this.y - p.y
        )
    }

    rotate90(): Point{
        return new Point(
            -this.y,
            this.x
        )
    }

    rotate(theta: number){
        const s = Math.sin(theta);
        const c = Math.cos(theta);
        return new Point(
            c * this.x + -s * this.y,
            s * this.x + c * this.y
        );
    }

    product(a: number): Point{
        return new Point(a*this.x, a*this.y);
    }

    length(): number{
        return Math.sqrt(this.x * this.x + this.y * this.y);
    }

    normalize(): Point{
        return this.product(1 / this.length());
    }

    dotproduct(p: Point): number{
        return this.x * p.x + this.y * p.y;
    }
};

export class Line{
    p1: Point;
    p2: Point;

    constructor (p1: Point, p2: Point){
        this.p1 = p1;
        this.p2 = p2;
    }

    distance(p: Point): number{
        // Returns signed distance.
        // Distance is positive if p is on the right of line(p1 -> p2) and negative if right.
        const q = this.p2.minus(this.p1).normalize();
        const theta = Math.abs(Math.acos(q.x)) * (q.y > 0 ? 1 : -1);
        return p.rotate(-theta).y;
    }

    is_left(p: Point): boolean{
         return this.p2.minus(this.p1).rotate90().dotproduct(p) >= 0;
    }
}



export function quickhul(ps: Array<Point>): Array<Point>{
    const ret = [];
    const cand = ps;
    cand.sort((a, b) => {
        if(a.x < b.x) return 1;
        if(a.x > b.x) return -1;
        return -1;
    })
    const n = ps.length;
    // let p1 = 
    return ret;
}

