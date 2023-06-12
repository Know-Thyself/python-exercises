from prettytable import PrettyTable, ALL

pokémon_table = PrettyTable()
pokémon_table.field_names = ["Pokémon name", "Type", "Species", "Abilities"]
pokémon_table.add_rows(
    [
        ["Squirtle", "Water", "Tiny Turtle Pokémon", "Torrent"],
        ["Bulbasaur", "Grass, Poison", "Seed Pokémon", "Overgrow"],
        ["Charmander", "Fire", "Lizard Pokémon", "Blaze"],
    ]
)

pokémon_table.align = "l"
pokémon_table.header = True
pokémon_table.border = True
# pokémon_table.hrules = ALL
print(pokémon_table)
