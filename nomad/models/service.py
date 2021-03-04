"""
nomad.models.service

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/services.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Service:
    id: str = field(metadata={"serde_rename": "ID"})
    name: str
    tags: Optional[list[str]]
    canary_tags: Optional[list[str]]
    enable_tag_override: bool
    port_label: str
    address_mode: str
    # checks: Optional[list[]]
    # check_restart: Optional[list[]]
    # connect: Optional[list[]]
    meta: Optional[dict[str, str]]
    canary_meta: Optional[dict[str, str]]
    task_name: str
