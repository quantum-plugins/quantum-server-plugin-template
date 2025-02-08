#
# DON'T CHANGE THIS FILE!!!!
#

from abc import ABC, abstractmethod
from typing import List, Dict, Any

Backend = str
Backends = List[Backend] 
Metadata = Dict[Any, Any]
ResultType = str
QasmFilePath = str
Results = Dict|float

def check_backend(func):
    def wrapper(self, 
    target_backend:Backend, 
    qasm_file_path:QasmFilePath,
    metadata:Metadata, 
    result_type:ResultType):
        assert target_backend in self.backends, "Invalid Target Backend. Selected Backend doesn't exists for this plugin!"

        return func(self, target_backend, qasm_file_path, metadata, result_type)

    return wrapper

class PluginInterface(ABC):
    def __init__(self, backends:Backends):
        self.backends = backends

    @abstractmethod
    def execute(self, target_backend:Backend, qasm_file_path:QasmFilePath, metadata:Metadata, result_type:ResultType) -> Results:
        pass