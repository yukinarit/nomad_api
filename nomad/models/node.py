"""
nomad.models.node

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/nodes.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from nomad.models.resource import NetworkResource, NodeDeviceResource, Resources
from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Address:
    """ Address model """

    family: str
    alias: str
    address: str
    reserved_ports: str
    gateway: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeNetwork:
    """ NodeNetwork model """

    mode: str
    device: str
    mac_address: str
    speed: int
    addresses: Optional[list[Address]]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeReservedNetworkResources:
    """ NodeReservedNetworkResources model """

    reserved_host_ports: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeEvent:
    """ NodeEvent model """

    message: str
    subsystem: str
    details: Optional[dict[str, str]]
    timestamp: str
    create_index: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class CSITopology:
    """ CSITopology model """

    segments: dict[str, str]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class CSINodeInfo:
    """ CSINodeInfo model """

    id: str = field(metadata={"serde_rename": "ID"})
    max_volumes: int
    accessible_topology: CSITopology
    requires_node_stage_volume: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class CSIControllerInfo:
    """ CSIControllerInfo model """

    supports_read_only_attach: bool
    supports_attach_detach: bool
    supports_list_volumes: bool
    supports_list_volumes_attached_nodes: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class CSIInfo:
    """ CSIInfo model """

    plugin_id: str = field(metadata={"serde_rename": "PluginID"})
    alloc_id: str = field(metadata={"serde_rename": "AllocID"})
    healthy: bool
    health_description: str
    update_time: str
    requires_controller_plugin: bool
    requires_topologies: bool
    controller_info: Optional[CSIControllerInfo]
    node_info: Optional[CSINodeInfo]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class DrainStrategy:
    """ DrainStrategy model """

    force_deadline: str
    started_at: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class DrainSpec:
    """ DrainSpec model """

    deadline: int
    ignore_system_jobs: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class DriverInfo:
    """ DriverInfo model """

    attributes: Optional[dict[str, str]]
    detected: bool
    healthy: bool
    health_description: str
    update_time: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class HostVolumeInfo:
    """ HostVolumeInfo model """

    path: str
    read_only: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeCpuResources:
    """ NodeCpuResources model """

    cpu_shares: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeMemoryResources:
    """ NodeMemoryResources model """

    memory_mb: int = field(metadata={"serde_rename": "MemoryMB"})


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeDiskResources:
    """ NodeDiskResources model """

    disk_mb: int = field(metadata={"serde_rename": "DiskMB"})


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeReservedResources:
    """ NodeReservedResources model """

    cpu: NodeCpuResources
    memory: NodeMemoryResources
    disk: NodeDiskResources
    # networks: NodeReservedResources


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class NodeResources:
    """ NodeResources model """

    cpu: NodeCpuResources
    memory: "NodeMemoryResources"
    disk: "NodeDiskResources"
    networks: Optional[list[NetworkResource]]
    devices: Optional[list[NodeDeviceResource]]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Node:
    """ Node model """

    id: str = field(metadata={"serde_rename": "ID"})
    datacenter: str
    name: str
    http_addr: str = field(metadata={"serde_rename": "HTTPAddr"})
    tls_enabled: bool = field(metadata={"serde_rename": "TLSEnabled"})
    attributes: dict[str, str]
    resources: Resources
    reserved: Resources
    node_resources: NodeResources
    reserved_resources: NodeReservedResources
    links: dict[str, str]
    meta: dict[str, str]
    node_class: str
    drain: bool
    drain_strategy: Optional[DrainStrategy]
    scheduling_eligibility: str
    status: str
    status_description: str
    status_updated_at: int
    events: list[NodeEvent]
    drivers: Optional[dict[str, DriverInfo]]
    host_volumes: Optional[dict[str, HostVolumeInfo]]
    # csi_controller_plugins: Optional[dict[str, CSIInfo]]
    # csi_node_plugins: Optional[dict[str, CSIInfo]]
    create_index: int
    modify_index: int
