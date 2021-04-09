import ast
from typing import Iterator, Tuple

from pandas_dev_flaker._data import State, register

MSG = "PSG010 don't import numpy.random"


@register(ast.ImportFrom)
def visit_ImportFrom(
    state: State,
    node: ast.ImportFrom,
    parent: ast.AST,
) -> Iterator[Tuple[int, int, str]]:
    if node.module == "numpy.random" or (
        node.module == "numpy"
        and "random" in {name.name for name in node.names}
    ):
        yield node.lineno, node.col_offset, MSG