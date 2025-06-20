from typing import List

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.types.case_template import InputCaseTemplate, OutputCaseTemplate


class TestCaseTemplateEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi):
        created_case_template = thehive.case_template.create(
            case_template={
                "name": "my first template",
                "description": "Template description",
            }
        )
        fetched_case_template = thehive.case_template.get(created_case_template["_id"])
        assert created_case_template == fetched_case_template

    def test_update(self, thehive: TheHiveApi, test_case_template: OutputCaseTemplate):
        case_template_id = test_case_template["_id"]
        update_fields: InputCaseTemplate = {
            "name": "updated template name",
            "description": "updated template description",
        }
        thehive.case_template.update(
            case_template_id=case_template_id, fields=update_fields
        )
        updated_case_template = thehive.case_template.get(
            case_template_id=case_template_id
        )

        for key, value in update_fields.items():
            assert updated_case_template.get(key) == value

    def test_delete(self, thehive: TheHiveApi, test_case_template: OutputCaseTemplate):
        case_template_id = test_case_template["_id"]
        thehive.case_template.delete(case_template_id=case_template_id)
        with pytest.raises(TheHiveError):
            thehive.case_template.get(case_template_id=case_template_id)

    def test_link_and_find_page_templates(
        self,
        thehive: TheHiveApi,
        test_case_template: OutputCaseTemplate,
        test_page_templates: List[dict],
    ):
        case_template_id = test_case_template["_id"]
        page_template_ids = [
            page_template["_id"] for page_template in test_page_templates
        ]

        thehive.case_template.link_page_templates(
            case_template_id=case_template_id,
            page_template_ids=page_template_ids,
        )

        linked_page_templates = thehive.case_template.find_page_templates(
            case_template_id=case_template_id
        )

        linked_page_template_ids = [
            page_template["_id"] for page_template in linked_page_templates
        ]
        assert sorted(linked_page_template_ids) == sorted(page_template_ids)

    def test_find(
        self,
        thehive: TheHiveApi,
        test_case_templates: List[OutputCaseTemplate],
    ):
        found_templates = thehive.case_template.find()
        original_ids = [template["_id"] for template in test_case_templates]
        found_ids = [template["_id"] for template in found_templates]
        assert sorted(found_ids) == sorted(original_ids)
