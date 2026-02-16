class CharacterError(Exception):
    """Base exception for character-related errors."""
    pass

class InvalidLivesError(TypeError):
    """Raised when lives is outside 0-99
   - Message: `c`"""
    pass

class InvalidCoinsError(TypeError):
    """Raised when coins is outside 0-999
   - Message: `"Coins must be between 0 and 999"`"""
    pass

class CharacterDeadError(ValueError):
    """Raised when using a dead character
   - Message: `"<name> has no lives remaining!"""
    pass
