async function fetchAllPokemons() {
    try {
        let allPokemon = [];
        let URL = "https://pokeapi.co/api/v2/pokemon";

        while (URL) {
            const pokemonData = await fetchPokemonData(URL);
            if (!pokemonData) {
                break;
            }
            const results = pokemonData.results;
            allPokemon.push(...results); // Spread operator to push individual pokemon
            URL = pokemonData.next;
        }
        return allPokemon; // Return the array of all Pokemon
    } catch (error) {
        console.error("Error: Not found", error);
        return [];
    }
}

function fetchPokemonData(URL) {
    return fetch(URL)
        .then(response => response.json())
        .catch(error => {
            console.error("Error fetching Pokemon data:", error);
            return null;
        });
}

// Call the function and handle the promise
fetchAllPokemons()
    .then(allPokemon => {
        fetchAllPokemons = document.getElementById("pokemons")

        console.log("All Pokemons:");
        allPokemon.forEach((pokemon, index) => {
            console.log(`${index + 1}. ${pokemon.name}`);
        });
    })
    .catch(error => console.error("Error fetching all Pokemons:", error));
    





