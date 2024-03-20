// Function to fetch Pokmon character data
function fetchPokemonData(name) {
    fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
      .then(response => response.json())
      .then(data => {
        // Display information about the Pokmon character
        const pokemonInfo = document.getElementById('pokemonInfo');
        pokemonInfo.innerHTML = `
          <h2>${data.name}</h2>
          <img src="${data.sprites.front_default}" alt="${data.name}">
          <p>Height: ${data.height}</p>
          <p>Weight: ${data.weight}</p>
          <p>Abilities: ${data.abilities.map(ability => ability.ability.name).join(', ')}</p>
        `;
      })
      .catch(error => {
        console.error('Error fetching Pokémon data:', error);
        const pokemonInfo = document.getElementById('pokemonInfo');
        pokemonInfo.innerHTML = '<p>Pokémon not found.</p>';
      });
  }
  
  // Function to search for Pokemon character
  function searchPokemon() {
    const searchInput = document.getElementById('searchInput');
    const pokemonName = searchInput.value.trim().toLowerCase();
    if (pokemonName) {
      fetchPokemonData(pokemonName);
    }
  }
  