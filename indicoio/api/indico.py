from typing import Union, List
from io import TextIOWrapper

from .base import ObjectProxy
from .model_group import ModelGroup
from .job_result import JobResult


class Indico(ObjectProxy):
    def model_groups(self, *fields):
        """
        Schema Introspection Client method generation should take care of query building
        and response extraction
        """
        fields = fields or ("id", "name", "status", "retrainRequired")
        model_groups_response = self.graphql.query(
            f"""query {{
        modelGroups {{
            modelGroups {{
                {",".join(fields)}
            }}
        }}}}"""
        )

        return [
            self.build_object(ModelGroup, **mg)
            for mg in model_groups_response["data"]["modelGroups"]["modelGroups"]
        ]

    def submission(self, workflow_id: int, data: List[Union[str, TextIOWrapper]]):
        """
        Submission API
        workflow_id: ID of workflow to run
        data: List of string or read file-like objects
        """
        jobs = []
        for item in data:
            storage_obj_dict = self.storage.upload(item)
            response = self.graphql.query(
                """mutation workflowSubmissionMutation($workflowId: Int, $files: JSONString) {
                    workflowSubmissionMutation(workflowId: $workflowId, files: $files) {
                        job_id
                    }
                }""",
                variables={"workflowId": workflow_id, "files": storage_obj_dict},
            )
            job_id = response["data"]["workflowSubmissionMutation"]["jobId"]
            job = self.build_object(JobResult, id=job_id)
            jobs.append(job)
        return jobs

