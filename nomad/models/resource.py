"""
nomad.models.resource

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/resources.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from nomad.models.constraint import Constraint
from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeDeviceResource:
    vendor: str
    type: str
    name: str
    # instances: Optional[list[NodeDevice]]
    # attributes: Optional[dict[str, Attribute]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NetworkResource:
    mode: str
    device: str
    cidr: str = field(metadata={"serde_rename": "CIDR"})
    ip: str = field(metadata={"serde_rename": "IP"})
    dns: Optional[str] = field(metadata={"serde_rename": "DNS"})
    reserved_ports: Optional[list[str]]
    dynamic_ports: Optional[str]
    mbits: str = field(metadata={"serde_rename": "MBits"})


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Resources:
    cpu: Optional[int] = field(metadata={"serde_rename": "CPU"})
    memory_mb: Optional[int] = field(metadata={"serde_rename": "MemoryMB"})
    disk_mb: Optional[int] = field(metadata={"serde_rename": "DiskMB"})
    networks: Optional[list[NetworkResource]]
    devcies: Optional[list["RequestedDevice"]]
    iops: Optional[int] = field(metadata={"serde_rename": "IOPS"})


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class RequestedDevice:
    name: str
    count: Optional[int]
    constraints: Optional[list[Constraint]]
    # affinities: Optional[list[Affinity]]
