"""
nomad.models.task

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/tasks.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from serde import deserialize, serialize

from .constraint import Constraint
from .resource import Resources
from .service import Service


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Affinity:
    l_target: str
    r_target: str
    operand: str
    weight: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class RestartPolicy:
    interval: int
    attempts: str
    delay: int
    mode: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class LogConfig:
    max_files: int
    max_file_size_mb: int = field(metadata={"serde_rename": "MaxFileSizeMB"})


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class TaskArtifact:
    getter_source: Optional[str]
    getter_options: Optional[dict[str, str]]
    getter_headers: Optional[dict[str, str]]
    getter_mode: Optional[str]
    relative_dest: Optional[str]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Vault:
    policies: list[str]
    namespace: Optional[str]
    env: Optional[bool]
    change_mode: Optional[str]
    change_signal: Optional[str]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Template:
    source_path: Optional[str]
    dest_path: Optional[str]
    embedded_tmpl: Optional[str]
    change_mode: Optional[str]
    change_signal: Optional[str]
    splay: Optional[int]
    perms: Optional[str]
    left_delim: Optional[str]
    right_delim: Optional[str]
    envvars: Optional[int]
    vault_grace: Optional[int]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class VolumeMount:
    volume: str
    destination: str
    read_only: bool
    propagation_mode: str


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Task:
    name: str
    driver: str
    user: str
    # lifecycle: TaskLifecycle
    # config
    constraints: Optional[list[Constraint]]
    affinities: Optional[list[Affinity]]
    env: Optional[dict[str, str]]
    services: Optional[list[Service]]
    resources: Resources
    restart_policy: RestartPolicy
    templates: Optional[list[Template]]
    # dispatch_payload: DispatchPayloadConfig
    volume_mounts: Optional[list[VolumeMount]]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class TaskGroup:
    name: str
    count: int
    constraints: Optional[list[Constraint]]
    affinities: Optional[list[Affinity]]
    tasks: Optional[list[Task]]
    meta: Optional[dict[str, str]]
    kill_timeout: Optional[str]
    log_config: Optional[LogConfig]
    artifacts: Optional[list[TaskArtifact]]
    vault: Optional[Vault]
