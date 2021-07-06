from dataclasses import dataclass, field
from typing import Optional

from serde import deserialize, serialize


@deserialize(rename_all="pascalcase")
@serialize(rename_all="pascalcase")
@dataclass
class WriteOptions:
    """ WriteOptions model """

    region: str
    namespace: str
    auth_token: str
    # ctx:
