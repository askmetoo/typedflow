from typedflow.batch import Batch
from typedflow.counted_cache import CacheTable
from typedflow.types import K
from typing import Any, Callable, Dict, Type, TypeVar

T = TypeVar('T')

class ConsumerNode:
    func: Callable[..., Any]
    debug: bool = ...
    precs: Dict[str, ProviderNode] = ...
    def __post_init__(self) -> None: ...
    def set_upstream_node(self, key: str, node: ProviderNode) -> None: ...
    def get_arg_types(self) -> Dict[str, Type]: ...
    def accept(self, batch_id: int) -> Batch[Dict[str, Any]]: ...
    def lt_op(self, another: ProviderNode) -> Callable[[str], None]: ...
    def __lt__(self, another: ProviderNode) -> Callable[[str], None]: ...
    def __gt__(self, another: Any) -> Any: ...
    def __call__(self, args: Dict[str, ProviderNode]) -> T: ...
    def __init__(self, func: Any, debug: Any) -> None: ...

class ProviderNode:
    func: Callable[..., K]
    debug: bool = ...
    cache_table: CacheTable[int, Batch[K]] = ...
    def __post_init__(self) -> None: ...
    def get_return_type(self) -> Type[K]: ...
    def get_or_produce_batch(self, batch_id: int) -> Batch[K]: ...
    def add_succ(self) -> None: ...
    def gt_op(self, another: ConsumerNode) -> Callable[[str], None]: ...
    def __gt__(self, another: ConsumerNode) -> Callable[[str], None]: ...
    def __lt__(self, another: Any) -> Any: ...
    def __init__(self, func: Any, debug: Any) -> None: ...