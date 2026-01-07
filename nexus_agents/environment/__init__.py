#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   :

from nexus_agents.environment.base_env import Environment

# from nexus_agents.environment.android.android_env import AndroidEnv
from nexus_agents.environment.werewolf.werewolf_env import WerewolfEnv
from nexus_agents.environment.stanford_town.stanford_town_env import StanfordTownEnv
from nexus_agents.environment.software.software_env import SoftwareEnv


__all__ = ["AndroidEnv", "WerewolfEnv", "StanfordTownEnv", "SoftwareEnv", "Environment"]
