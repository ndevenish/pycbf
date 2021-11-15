import os
from typing import IO, Any, Dict, Union, type_check_only

import numpy as np
from numpy.typing import NDArray

@type_check_only
class ImgOpaqueData:
    pass

class Img:
    @property
    def columns(self) -> int: ...
    @property
    def rows(self) -> int: ...
    @property
    def rowmajor(self) -> bool: ...
    @property
    def fields(self) -> Dict[str, str]: ...
    @property
    def image(self) -> NDArray[np.int32]: ...
    def __init__(self) -> None: ...
    def get_field(self, name: str) -> str: ...
    def get_number(self, name: str) -> float: ...
    def active_views(self) -> int: ...
    @classmethod
    def read_mar345(self, filename: Union[str, bytes, os.PathLike]) -> Img: ...
    def read_mar345data(self, file: IO) -> ImgOpaqueData: ...
    def read_mar345header(self, file: IO, org_data: ImgOpaqueData) -> None: ...
    def set_dimensions(self, columns: int, rows: int) -> None: ...
    def set_tags(self, number: int) -> None: ...