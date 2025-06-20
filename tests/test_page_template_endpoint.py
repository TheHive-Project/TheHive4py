from typing import List

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.types.page_template import InputUpdatePageTemplate, OutputPageTemplate


class TestPageTemplateEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi):
        created_page_template = thehive.page_template.create(
            page_template={
                "title": "my page template",
                "category": "testing",
                "content": "...",
            }
        )
        fetched_page_template = thehive.page_template.get(created_page_template["_id"])
        assert created_page_template == fetched_page_template

    def test_update(self, thehive: TheHiveApi, test_page_template: OutputPageTemplate):
        page_template_id = test_page_template["_id"]
        update_fields: InputUpdatePageTemplate = {
            "title": "updated page template name",
            "content": "updated page template description",
        }
        thehive.page_template.update(
            page_template_id=page_template_id, fields=update_fields
        )
        updated_page_template = thehive.page_template.get(
            page_template_id=page_template_id
        )

        for key, value in update_fields.items():
            assert updated_page_template.get(key) == value

    def test_delete(self, thehive: TheHiveApi, test_page_template: OutputPageTemplate):
        page_template_id = test_page_template["_id"]
        thehive.page_template.delete(page_template_id=page_template_id)
        with pytest.raises(TheHiveError):
            thehive.page_template.get(page_template_id=page_template_id)

    def test_find(
        self,
        thehive: TheHiveApi,
        test_page_templates: List[OutputPageTemplate],
    ):
        found_templates = thehive.page_template.find()
        original_ids = [template["_id"] for template in test_page_templates]
        found_ids = [template["_id"] for template in found_templates]
        assert sorted(found_ids) == sorted(original_ids)
