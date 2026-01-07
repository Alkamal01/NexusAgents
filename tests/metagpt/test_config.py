#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/9 15:57
@Author  : alexanderwu
@File    : test_config.py
"""

from nexus_agents.config2 import Config
from nexus_agents.configs.llm_config import LLMType
from tests.nexus_agents.provider.mock_llm_config import mock_llm_config


def test_config_1():
    cfg = Config.default()
    llm = cfg.get_openai_llm()
    if cfg.llm.api_type == LLMType.OPENAI:
        assert llm is not None


def test_config_from_dict():
    cfg = Config(llm=mock_llm_config)
    assert cfg
    assert cfg.llm.api_key == "mock_api_key"
