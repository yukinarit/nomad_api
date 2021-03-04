"""
nomad.models.constraint

The models defined in this module can be found
[here](https://github.com/hashicorp/nomad/blob/v1.0.4/api/constraint.go)
in Hashicorp Nomad project.
"""
from dataclasses import dataclass

from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class Constraint:
    """ Constraint model """

    l_target: str
    r_target: str
    operand: str
