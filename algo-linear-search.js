const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}
arrayToSearchThrough.push(4);

function linearSearch(valueToFind, arrayToSearchThrough) {
    let index;
    for (let i = 0; i <= arrayToSearchThrough.length; i++){
        if (arrayToSearchThrough[i]===valueToFind){
            index = i;
        }
    }
    console.log(index);
    return 0
};

function globalLinearSearch(valueToFind, arrayToSearchThrough) {
    let arrayOfIndex=[];
    for (let i = 0; i <= arrayToSearchThrough.length; i++){
        if (arrayToSearchThrough[i]===valueToFind){
            arrayOfIndex.push(i);
        }
    }
    console.log(arrayOfIndex);
    return 0
};


linearSearch(6, arrayToSearchThrough);
globalLinearSearch(4, arrayToSearchThrough);
