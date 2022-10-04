function fibonacci (num) {
    
    let num1 = 0;
    let num2 = 1; 
    let fib;
    if (num<2){
        console.log(num);
    }
    else{
      for (let i = 1; i < num; i++){
        fib = num1 + num2;
        num1 = num2;
        num2 = fib;
      }
      console.log(fib);
    }
};

fibonacci(7);