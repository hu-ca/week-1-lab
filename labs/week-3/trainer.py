#!/usr/bin/env python3

"""Trainer class for managing a team of Pokemon."""

from pokemon import Pokemon


class Trainer:
    """A Pokemon trainer who manages a team of Pokemon."""


    def __init__(self, name: str) -> None:
        """Initialise a new Trainer."""
        self.name = name
        self.team: list[Pokemon] = []
        self.max_team_size = 6
        pass

    def add_to_team(self, pokemon: Pokemon) -> bool:
        """Add a Pokemon to the trainer's team.

        Returns True if successful, False if team is full.
        """
        if len(self.team) == self.max_team_size:
            return False
        else:
            self.team.append(pokemon)
            return True
        pass

    def get_team_size(self) -> int:
        """Get the number of Pokemon in the team."""
        return len(self.team)
        pass

    def get_first_available(self) -> Pokemon | None:
        """Get the first non-fainted Pokemon in the team."""
        for x in range(self.get_team_size()):
            if(self.team[x].is_fainted() == False):
                return self.team[x]
        return None
        pass

    def get_pokemon_by_type(self, pokemon_type: type) -> list[Pokemon]:
        """Get a list of all Pokemon in the team that are instances of pokemon_type."""
        all_types: list["Pokemon"] = []
        for p in self.team:
            if isinstance(p, pokemon_type):
                all_types.append(p)
        return all_types
        pass

    def __str__(self) -> str:
        """Return a string representation of this Trainer."""
        return f'{self.name} ({self.get_team_size()}/6 Pokemon)'
        pass

        