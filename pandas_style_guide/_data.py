import pkgutil
import collections
from typing import List, Tuple, Dict
import ast
from pandas_style_guide import _plugins

FUNCS = collections.defaultdict(list)
def register(tp):
    def register_decorator(func):
        FUNCS[tp].append(func)
        return func
    return register_decorator


def visit(funcs, tree: ast.Module) -> Dict[int, List[int]]:
    "Step through tree, recording when nodes are in annotations."
    in_annotation = False
    nodes: List[Tuple[bool, ast.AST]] = [(in_annotation, tree)]

    while nodes:
        in_annotation, node = nodes.pop()

        tp = type(node)
        for ast_func in funcs[tp]:
            yield from ast_func(in_annotation, node)

        for name in reversed(node._fields):
            value = getattr(node, name)
            if name in {"annotation", "returns"}:
                next_in_annotation = True
            else:
                next_in_annotation = in_annotation
            if isinstance(value, ast.AST):
                nodes.append((next_in_annotation, value))
            elif isinstance(value, list):
                for value in reversed(value):
                    if isinstance(value, ast.AST):
                        nodes.append((next_in_annotation, value))

def _import_plugins() -> None:
    # https://github.com/python/mypy/issues/1422
    plugins_path: str = _plugins.__path__  # type: ignore
    mod_infos = pkgutil.walk_packages(plugins_path, f'{_plugins.__name__}.')
    for _, name, _ in mod_infos:
        __import__(name, fromlist=['_trash'])


_import_plugins()