# Onboard-Network-Py
A Python implementation of a UDP client and server, augmented with Protobuf messages

There is no lib folder here as this code is meant to be added as a Git submodule in lib.

To generate Protobuf files:
```bash
mkdir generated  # if needed
protoc -I=Protobuf --python_out=generated Protobuf/*.proto
```
