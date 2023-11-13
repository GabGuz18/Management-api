class CategoryDuplicatedError(Exception):
    """Raised when category duplicated"""
    pass

class UpdateQuantityError(Exception):
    """Raised when cannot update quantity"""
    pass

class IngredientDuplicatedError(Exception):
    """Raised when ingredint duplicated"""
    pass

class IncorrectFormat(Exception):
    """Raised when format is incorrect"""
    pass