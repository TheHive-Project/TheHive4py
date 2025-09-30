from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.cortex import (
    InputAnalyzerJob,
    InputResponderAction,
    OutputAnalyzer,
    OutputAnalyzerJob,
    OutputResponder,
    OutputResponderAction,
)


class CortexEndpoint(EndpointBase):
    def create_analyzer_job(self, job: InputAnalyzerJob) -> OutputAnalyzerJob:
        """Create an analyzer job.

        Args:
            job: The metadata of the analyzer job to create.
        Returns:
            The created analyzer job.
        """
        return self._session.make_request(
            "POST", path="/api/connector/cortex/job", json=job
        )

    def bulk_create_analyzer_jobs(
        self, jobs: List[InputAnalyzerJob]
    ) -> List[OutputAnalyzerJob]:
        """Create multiple analyzer jobs in bulk.

        Args:
            jobs: The list of analyzer jobs to create.

        Returns:
            The list of created analyzer jobs.
        """
        return self._session.make_request(
            "POST", path="/api/v1/connector/cortex/job/_bulk", json={"jobs": jobs}
        )

    def create_responder_action(
        self, action: InputResponderAction
    ) -> OutputResponderAction:
        """Create a responder action.

        Args:
            action: The metadata of the responder action to create.
        Returns:
            The created responder action.
        """
        return self._session.make_request(
            "POST", path="/api/connector/cortex/action", json=action
        )

    def list_analyzers(self, range: Optional[str] = None) -> List[OutputAnalyzer]:
        """List all analyzers.

        Args:
            range: Optional range for pagination.
        Returns:
            A list of analyzers.
        """
        params = {"range": range}
        return self._session.make_request(
            "GET", path="/api/connector/cortex/analyzer", params=params
        )

    def list_analyzers_by_type(self, data_type: str) -> List[OutputAnalyzer]:
        """List all analyzers of a given data type.

        Args:
            data_type: The data type that the analyzers should support.
        Returns:
            A list of analyzers that support the given data type.
        """
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/type/{data_type}"
        )

    def get_analyzer(self, analyzer_id: str) -> OutputAnalyzer:
        """Get an analyzer by id.

        Args:
            analyzer_id: The id of the analyzer to get.
        Returns:
            The analyzer specified by the id.
        """
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/{analyzer_id}"
        )

    def get_analyzer_job(self, job_id: str) -> OutputAnalyzerJob:
        """Get an analyzer job by id.

        Args:
            job_id: The id of the analyzer job to get.
        Returns:
            The analyzer job specified by the id.
        """
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/job/{job_id}"
        )

    def find_analyzer_jobs(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAnalyzerJob]:
        """Find analyzer jobs.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of analyzer jobs matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listJob"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "analyzer-jobs"},
            json={"query": query},
        )

    def list_responders(
        self, entity_type: str, entity_id: str
    ) -> List[OutputResponder]:
        """List all responders of a given entity type.

        Args:
            entity_type: The type of the entity.
            entity_id: The id of the entity or its name (depends on the entity).
        Returns:
            A list of responders that support the given entity type.
        """
        return self._session.make_request(
            "GET", f"/api/connector/cortex/responder/{entity_type}/{entity_id}"
        )
