var bottle_num = 99;
var bottle = " bottles ";

function bottleSong() {
    // Write your code here!
    while (bottle_num >= 0) {
        if (bottle_num == 2){
            console.log(bottle_num+' bottles of beer on the wall, '+bottle_num+' bottles of beer. Take one down and pass it around, '+(bottle_num=bottle_num-1)+' bottle of beer on the wall.');

        }
        else if (bottle_num == 1){
            console.log(bottle_num+' bottle of beer on the wall, '+bottle_num+' bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.');
            bottle_num--;
        }
        else if (bottle_num == 0){
            console.log('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.');
            bottle_num--;
        }
        else{
            console.log(bottle_num+' bottles of beer on the wall, '+bottle_num+' bottles of beer. Take one down and pass it around, '+(bottle_num=bottle_num-1)+' bottles of beer on the wall.');
        }
        
        
      }
  };
  
  bottleSong();