"""
nomad.models.event_stream

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/event_stream.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass
from typing import Optional, Union

from nomad.models.allocation import Allocation
from nomad.models.deployment import Deployment
from nomad.models.evaluation import Evaluation
from nomad.models.job import Job
from nomad.models.node import Node
from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Event:
    """ Event model """

    topic: str
    type: str
    key: str
    filter_keys: Optional[list[str]]
    index: Optional[int]
    payload: Optional[dict[str, Union[Evaluation, Allocation, Deployment, Job, Node]]]


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Events:
    """ Events model """

    index: int
    events: Optional[list[Event]]
