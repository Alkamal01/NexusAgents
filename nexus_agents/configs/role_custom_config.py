#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/4/22 16:33
@Author  : Justin
@File    : role_custom_config.py
"""
from nexus_agents.configs.llm_config import LLMConfig
from nexus_agents.utils.yaml_model import YamlModel


class RoleCustomConfig(YamlModel):
    """custom config for roles
    role: role's className or role's role_id
    To be expanded
    """

    role: str = ""
    llm: LLMConfig
