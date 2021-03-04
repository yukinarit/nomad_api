from nomad.models.jobs import Job
from serde.json import from_json

JSON = """
[
  {
    "ID": "example",
    "ParentID": "",
    "Name": "example",
    "Type": "service",
    "Priority": 50,
    "Status": "pending",
    "StatusDescription": "",
    "JobSummary": {
      "JobID": "example",
      "Namespace": "default",
      "Summary": {
        "cache": {
          "Queued": 1,
          "Complete": 1,
          "Failed": 0,
          "Running": 0,
          "Starting": 0,
          "Lost": 0
        }
      },
      "Children": {
        "Pending": 0,
        "Running": 0,
        "Dead": 0
      },
      "CreateIndex": 52,
      "ModifyIndex": 96
    },
    "CreateIndex": 52,
    "ModifyIndex": 93,
    "JobModifyIndex": 52
  }
]
"""


def test_unpack():
    jobs = from_json(list[Job], JSON)
    print(jobs)
