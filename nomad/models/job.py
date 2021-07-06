"""
nomad.models.job


The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/jobs.go)
in Hashicorp Nomad project.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from nomad.models.constraint import Constraint
from nomad.models.task import Affinity, TaskGroup
from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class RegisterRequest:
    """ RegisterRequest """

    job: Job
    enforce_index: bool
    modify_index: int
    policy_override: bool
    preserve_counts: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class RegisterOptions:
    """ RegisterOptions model """

    enforce_index: bool
    modify_index: int
    policy_override: bool
    preserve_counts: bool


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Children:
    """ Children model """

    pending: int
    running: int
    dead: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Summary:
    """ Summary model """

    queued: int
    complete: int
    failed: int
    running: int
    starting: int
    lost: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class JobSummary:
    """ JobSummary model """

    job_id: str = field(metadata={"serde_rename": "JobID"})
    namespace: str
    summary: dict[str, Summary]
    create_index: int
    modify_index: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Job:
    """ Job model """

    region: Optional[str]
    namespace: Optional[str]
    id: Optional[str] = field(metadata={"serde_rename": "ID"})
    name: Optional[str]
    type: Optional[str]
    priority: int
    all_at_once: Optional[bool]
    datacenters: Optional[list[str]]
    constraints: Optional[list[Constraint]]
    affinities: Optional[list[Affinity]]
    task_groups: Optional[list[TaskGroup]]
    # update
    # multiregion
    # spreads: Optional[list[Spread]]
    # periodic
    # parameterized_job
    # reschedule
    # migrate
    meta: Optional[dict[str, str]]
    consul_token: Optional[str]
    vault_token: Optional[str]
    stop: Optional[bool]
    parent_id: Optional[str] = field(metadata={"serde_rename": "ParentID"})
    dispatched: Optional[bool]
    # payload: byte
    vault_namespace: Optional[str]
    nomad_token_id: Optional[str] = field(metadata={"serde_rename": "NomadTokenID"})
    status: Optional[str]
    status_description: Optional[str]
    stable: Optional[bool]
    version: Optional[int]
    submit_time: Optional[int]
    create_index: Optional[int]
    modify_index: Optional[int]
    job_modify_index: Optional[int]
