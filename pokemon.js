//this loop grabs every pokemon container individually
const btn = document.querySelector('button');

//generate initial pokemon
function generatePokemon() {
    //declare variables
    const pokemonName = document.querySelector('.pokemon-name');
    const pokemonImage = document.querySelector('.pokemon-image');
    const pokemonType = document.querySelector('.pokemon-type');
    const random = Math.floor(Math.random() * 256 + 1);
    //get random pokemon from api
    axios.get(`https://pokeapi.co/api/v2/pokemon/${random}`)
        .then(response => {
            pokemonName.innerHTML = response.data.forms[0].name;
            pokemonImage.src = response.data.sprites.front_default;
            //retrieve pokemon type
            const team = response.data.types[0].type.name;
            pokemonType.innerHTML = team;
            //call generate team function to retrieve five additional pokemon of same type
            generateTeam(team);
        })
        .catch(error => {
            //alert if errors
            pokemonName.innerHTML = "An error has occurred.";
            pokemonImage.src = "";
        })
}

//generate team of 5 pokemon of same type as original random pokemon
function generateTeam(team) {
    const pokemonContainers = document.querySelectorAll('.pokemon-team');
    //loop through each container to get 5 different pokemon
    for (const container of pokemonContainers) {
        const pokemonName = container.querySelector('.pokemon-name');
        const pokemonImage = container.querySelector('.pokemon-image');
        const random = Math.floor(Math.random() * 70);
        const pokemonType = container.querySelector('.pokemon-type')
        //retrieve pokemon of given type
        axios.get(`https://pokeapi.co/api/v2/type/${team}`)
            .then(response => {
                //get random pokemon from list of pokemon with given type
                pokemonName.innerHTML = response.data.pokemon[random].pokemon.name;
                //retrieve url to get pokemon image
                const url = response.data.pokemon[random].pokemon.url;
            //call function using url to retrieve pokemon image
                getPoke(url, pokemonImage, pokemonType);
            })
            .catch(error => {
                pokemonName.innerHTML = "An error has occurred.";
                pokemonImage.src = "";
            })
    }

}

//function to display pokemon image and type
function getPoke(url, pokemonImage, pokemonType) {
    axios.get(`${url}`)
        .then(response => {
            console.log(response.data);
            pokemonImage.src = response.data.sprites.front_default;
            pokemonType.innerHTML = response.data.types[0].type.name;
        })
        .catch(error => {
            console.log("error");
        })
}


btn.addEventListener("click", generatePokemon);
