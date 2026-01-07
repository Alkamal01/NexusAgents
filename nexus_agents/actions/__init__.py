#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 17:44
@Author  : alexanderwu
@File    : __init__.py
"""
from enum import Enum

from nexus_agents.actions.action import Action
from nexus_agents.actions.action_output import ActionOutput
from nexus_agents.actions.add_requirement import UserRequirement
from nexus_agents.actions.debug_error import DebugError
from nexus_agents.actions.design_api import WriteDesign
from nexus_agents.actions.design_api_review import DesignReview
from nexus_agents.actions.project_management import WriteTasks
from nexus_agents.actions.research import CollectLinks, WebBrowseAndSummarize, ConductResearch
from nexus_agents.actions.run_code import RunCode
from nexus_agents.actions.search_and_summarize import SearchAndSummarize
from nexus_agents.actions.write_code import WriteCode
from nexus_agents.actions.write_code_review import WriteCodeReview
from nexus_agents.actions.write_prd import WritePRD
from nexus_agents.actions.write_prd_review import WritePRDReview
from nexus_agents.actions.write_test import WriteTest
from nexus_agents.actions.di.execute_nb_code import ExecuteNbCode
from nexus_agents.actions.di.write_analysis_code import WriteAnalysisCode
from nexus_agents.actions.di.write_plan import WritePlan


class ActionType(Enum):
    """All types of Actions, used for indexing."""

    ADD_REQUIREMENT = UserRequirement
    WRITE_PRD = WritePRD
    WRITE_PRD_REVIEW = WritePRDReview
    WRITE_DESIGN = WriteDesign
    DESIGN_REVIEW = DesignReview
    WRTIE_CODE = WriteCode
    WRITE_CODE_REVIEW = WriteCodeReview
    WRITE_TEST = WriteTest
    RUN_CODE = RunCode
    DEBUG_ERROR = DebugError
    WRITE_TASKS = WriteTasks
    SEARCH_AND_SUMMARIZE = SearchAndSummarize
    COLLECT_LINKS = CollectLinks
    WEB_BROWSE_AND_SUMMARIZE = WebBrowseAndSummarize
    CONDUCT_RESEARCH = ConductResearch
    EXECUTE_NB_CODE = ExecuteNbCode
    WRITE_ANALYSIS_CODE = WriteAnalysisCode
    WRITE_PLAN = WritePlan


__all__ = [
    "ActionType",
    "Action",
    "ActionOutput",
]
