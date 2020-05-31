class Point{
    x: number;
    y: number;

    constructor (x: number, y: number){
        this.x = x;
        this.y = y;
    }
};

class Line{
    p1: Point;
    p2: Point;

    constructor (p1: Point, p2: Point){
        this.p1 = p1;
        this.p2 = p2;
    }

    distance(p: Point): number{
        if(this.p1.x === this.p2.x) return Math.abs(p.x - this.p1.x);
        const t1 = (this.p2.y - this.p1.y) / (this.p2.x - this.p1.x);
        const t2 =  this.p1.y - a * this.p1.x;
        const a = t1;
        const b -1;
        const c = t2;
        return Math.abs(a*p.x + b*p.y + c) / Math.sqrt(a*a + b*b);        
    }
}



function quickhul(ps: Array<Point>): Array<Point>{
    ps.sort((a, b) => {
        if(a.x < b.x) return 1;
        if(a.x > b.x) return -1;
        return -1;
    })
    return [];
}
