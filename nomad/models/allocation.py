"""
nomad.models.allocation

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/allocations.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from nomad.models.job import Job
from nomad.models.resource import Resources
from nomad.models.service import Service
from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Allocation:
    """ Allocation model """

    id: str = field(metadata={"serde_rename": "JobID"})
    namespace: str
    eval_id: str = field(metadata={"serde_rename": "EvalID"})
    name: str
    node_id: str = field(metadata={"serde_rename": "NodeID"})
    node_name: str
    job_id: str = field(metadata={"serde_rename": "JobID"})
    job: Job
    task_group: str
    resources: Resources
    task_resources: Optional[dict[str, Resources]]
    # allocated_resources
    services: Optional[dict[str, Service]]
    # metrics
    desired_status: str
    desired_description: str
    # desired_transition
    client_status: str
    client_description: str
    # task_states
    deployment_id: str = field(metadata={"serde_rename": "DeploymentID"})
    # deployment_status
    followup_eval_id: str = field(metadata={"serde_rename": "FollowupEvalID"})
    previous_allocation: str
    next_allocation: str
    # reschedule_tracker
    preempted_allocations: Optional[list[str]]
    preempted_by_allocation: str
    create_index: int
    modify_index: int
    alloc_modify_index: int
    create_time: int
    modify_time: int
