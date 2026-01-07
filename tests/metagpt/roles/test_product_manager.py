#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/16 14:50
@Author  : alexanderwu
@File    : test_product_manager.py
"""
import json

import pytest

from nexus_agents.actions import WritePRD
from nexus_agents.context import Context
from nexus_agents.logs import logger
from nexus_agents.roles import ProductManager
from nexus_agents.utils.common import any_to_str
from nexus_agents.utils.git_repository import GitRepository
from tests.nexus_agents.roles.mock import MockMessages


@pytest.mark.asyncio
async def test_product_manager(new_filename):
    context = Context()
    try:
        product_manager = ProductManager(context=context)
        # prepare documents
        logger.info(MockMessages.req)
        rsp = await product_manager.run(MockMessages.req)
        logger.info(rsp)
        assert rsp.cause_by == any_to_str(WritePRD)
        # assert REQUIREMENT_FILENAME in context.repo.docs.changed_files
        logger.info(rsp)
        assert len(rsp.content) > 0
        doc = list(rsp.instruct_content.docs.values())[0]
        m = json.loads(doc.content)
        assert m["Original Requirements"] == MockMessages.req.content

        # nothing to do
        rsp = await product_manager.run(rsp)
        assert rsp is None
    except Exception as e:
        assert not e
    finally:
        # Clean up using the project path
        if context.config.project_path:
            git_repo = GitRepository(context.config.project_path)
            git_repo.delete_repository()


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
