# Onboard-Network-Py
A Python implementation of a UDP client and server, augmented with Protobuf messages

To generate Protobuf files:
```bash
protoc -I=lib/proto --python_out=lib/generated lib/proto/*.proto
```
