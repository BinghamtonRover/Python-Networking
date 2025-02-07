# Onboard-Network-Py
A Python implementation of a UDP client and server, augmented with Protobuf messages

There is no lib folder here as this code is meant to be added as a Git submodule in lib.

To generate Protobuf files:
```bash
python Protobuf\gen-python -p *
```

Due to [an unresolved bug in `protoc`](https://github.com/protocolbuffers/protobuf/issues/1491),
the output from these files will not work out of the box. Using an IDE or CLI tool, perform the
following find and replace with RegEx enabled:

- Directory: src/generated/
- Find: `import (\w+)_pb2 as .+`
- Replace: `from . import $1_pb2 as $1__pb2`

This replaces all instances of `import xxx as yyy` with `from . import xxx as yyy`.

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
from lib.network.generated import Device
```
