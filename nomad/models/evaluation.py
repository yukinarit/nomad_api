"""
nomad.models.evaluation

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/evaluations.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Evaluation:
    """ Evaluation model """

    id: str = field(metadata={"serde_rename": "ID"})
    priority: int
    type: str
    triggered_by: str
    namespace: str
    job_id: str = field(metadata={"serde_rename": "JobID"})
    job_modify_index: int
    node_id: str = field(metadata={"serde_rename": "NodeID"})
    node_modify_index: int
    deployment_id: str = field(metadata={"serde_rename": "DeploymentID"})
    status: str
    status_description: str
    wait: int
    # wait_until: datetime
    next_eval: str
    previous_eval: str
    blocked_eval: str
    # FailedTGAllocs
    class_eligibility: Optional[dict[str, bool]]
    escaped_computed_class: bool
    quota_limit_reached: str
    annotate_plan: bool
    queue_allocations: Optional[dict[str, int]]
    snapshot_index: int
    create_index: int
    modify_index: int
    create_time: int
    modify_time: int
