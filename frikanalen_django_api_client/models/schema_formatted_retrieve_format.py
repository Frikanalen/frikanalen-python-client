from enum import Enum


class SchemaFormattedRetrieveFormat(str, Enum):
    VALUE_0 = ".json"

    def __str__(self) -> str:
        return str(self.value)
