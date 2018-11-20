from typing import Dict

from pipeline_definition.types.common_data_types import File
from pipeline_definition.types.data_types import DataType


class Dbsnp(File):
    @staticmethod
    def name():
        return "DBSNP"

    @staticmethod
    def doc():
        pass

    # @classmethod
    # def schema(cls) -> Dict:
    #     return {
    #         "path": {"type": "string", "required": True}
    #     }
