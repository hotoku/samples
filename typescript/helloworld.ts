class HelloWorld{
    constructor(public txt: string){
    }

    greet(){
        console.log(this.txt);
    }
}

const hw = new HelloWorld("Hello World!");
hw.greet();
