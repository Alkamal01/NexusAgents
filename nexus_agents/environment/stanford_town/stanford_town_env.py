#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : MG StanfordTown Env

from nexus_agents.environment.base_env import Environment
from nexus_agents.environment.stanford_town.stanford_town_ext_env import StanfordTownExtEnv


class StanfordTownEnv(StanfordTownExtEnv, Environment):
    pass
