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
        return p.minus(this.p1).rotate(-theta).y;
    }

    is_left(p: Point): boolean{
         return this.p2.minus(this.p1).rotate90().dotproduct(p) >= 0;
    }

    search_farthest_right(vs: Array<Point>): Point{
        // Returns the point to which signed distance is minimum.
        let ret = vs[0];
        let min = this.distance(ret);
        for(let i = 1; i < vs.length; i++){
            const v = this.distance(vs[i]);
            if(v < min){
                ret = vs[i];
                min = v;
            }
        }
        return ret;
    }
}

class Node<T>{
    v: T;
    prev: Node<T>;
    next: Node<T>;
    constructor(v: T, prev: Node<T> = null, next: Node<T> = null){
        this.v = v;
        this.prev = prev;
        this.next = next;
    }
}

class RingList<T>{
    start: Node<T>;
    size: number;

    constructor(vs: Array<T>){
        const nodes = vs.map(v => new Node(v));
        const num = vs.length;
        for(let i = 0; i < num; i++){
            const p = i === 0 ? num-1 : i-1;
            const n = i === (num-1) ? 0 : i+1;
            nodes[i].prev = nodes[p];
            nodes[i].next = nodes[n];
        }
        this.start = nodes[0];
        this.size = vs.length;
    }

    to_array(): Array<T>{
        const ret: Array<T> = [];
        let v = this.start;
        for(let i = 0; i < this.size; i++){
            ret.push(v.v);
            v = v.next;
        }
        return ret;
    }

    insert(pos: Node<T>, v: T){
        const n = new Node<T>(v, pos, pos.next);
        pos.next.prev = n;
        pos.next = n;
        this.size++;
    }
}

function contains(ring: RingList<Point>, p: Point){
    let v = ring.start;
    while(true){
        const l = new Line(v.v, v.next.v);
        if(l.distance(v.v) < -1e-10) return false;
        /*
          Here, we want to check if l.distance(v.v) is negative.
          Considering numerical error, tiny buffer is introduced.
          Because of that, this function return true for the point that is outside of the ring but very close to it.
        */

        if(v.next === ring.start) break;
        v = v.next;
    }
    return true;
}

export function quickhul(ps: Array<Point>): Array<Point>{
    if(ps.length <= 3){
        return ps;
    }
    var cand = ps;
    cand.sort((a, b) => {
        if(a.x < b.x) return 1;
        if(a.x > b.x) return -1;
        return -1;
    })
    const n = ps.length;
    const ret = new RingList([
        cand[0], cand[n-1]
    ]);
    cand = cand.slice(1, n-1);
    while(cand.length > 0){
        let v1 = ret.start;
        const inserts: Array<[Node<Point>, Point]> = [];
        for(let i = 0; i < ret.size; i++){
            const v2 = v1.next;
            const l = new Line(v1.v, v2.v);
            const v3 = l.search_farthest_right(cand);
            if(l.distance(v3) < 0){
                inserts.push([v1, v3]);
            }
            v1 = v2;
        }
        for(let i = 0; i < inserts.length; i++){
            ret.insert(inserts[i][0], inserts[i][1]);
        }
        cand = cand.filter(v => !contains(ret, v));
    }
    return ret.to_array();
}
