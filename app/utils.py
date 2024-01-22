from uuid import UUID

from sqlalchemy.orm.exc import NoResultFound


def convert_to_UUID(uuid: str) -> UUID:
    try:
        return UUID(uuid)
    except ValueError:
        raise ValueError("Некорректный формат UUID.")


def get_error_code(error: Exception) -> int:
    if isinstance(error, NoResultFound):
        return 404
    return 400
