#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/29 15:35
@Author  : alexanderwu
@File    : __init__.py
"""

from nexus_agents.tools import libs  # this registers all tools
from nexus_agents.tools.tool_registry import TOOL_REGISTRY
from nexus_agents.configs.search_config import SearchEngineType
from nexus_agents.configs.browser_config import WebBrowserEngineType


_ = libs, TOOL_REGISTRY  # Avoid pre-commit error


class SearchInterface:
    async def asearch(self, *args, **kwargs):
        ...


__all__ = ["SearchEngineType", "WebBrowserEngineType", "TOOL_REGISTRY"]
