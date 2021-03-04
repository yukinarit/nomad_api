"""
nomad.models.deployment

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/deployments.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass, field
from typing import Optional

from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Deployment:
    """ Deployment model """

    id: str = field(metadata={"serde_rename": "ID"})
    namespace: str
    job_id: str = field(metadata={"serde_rename": "JobID"})
    job_version: int
    job_modify_index: int
    job_spec_modify_index: int
    job_create_index: int
    is_multiregion: bool
    task_groups: Optional[dict[str, "DeploymentState"]]
    status: str
    status_description: str
    create_index: int
    modify_index: int


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class DeploymentState:
    """ DeploymentState model """

    placed_canaries: Optional[list[str]]
    auto_revert: bool
    progress_deadline: int
    # required_progress_by
    promoted: bool
    desired_canaries: int
    desired_total: int
    placed_allocs: int
    healthy_allocs: int
    unhealthy_allocs: int
