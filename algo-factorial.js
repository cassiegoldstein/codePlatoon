function factorial (num) {
    let fact = 1;
      for (let i = 0; i < num; i++){
        fact = fact * (num-i);
      }
      console.log(fact);
};

factorial(10);