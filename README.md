# Onboard-Network-Py
A Python implementation of a UDP client and server, augmented with Protobuf messages

There is no lib folder here as this code is meant to be added as a Git submodule in lib.

To generate Protobuf files:
```bash
mkdir generated  # if needed
protoc --python_out=generated Protobuf/*.proto
```

## Importing files

Always treat imports as starting from the top-level directory, _not_ this submodule. For example: 
```
bin/
lib/
  network/  (this repository)
    bin/
    generated/Protobuf/
    Protobuf/
    src/
```
To import a file in `src`:
```py
from lib.network import UdpClient
```

Imports rely on `__init__.py` spelling out every single file to import. Since this is annoying for generated files, you must import Protobuf files directly:
```py
from lib.network.generated.Protobuf.wrapper_pb2 import WrappedMessage
```

The Protobuf files must be in `generated/Protobuf`, not `generated`, due to the `protoc` compiler using absolute imports, not relative imports.
