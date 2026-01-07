#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import asyncio

from nexus_agents.config2 import Config
from nexus_agents.roles import Searcher
from nexus_agents.tools.search_engine import SearchEngine


async def main():
    question = "What are the most interesting human facts?"

    search = Config.default().search
    kwargs = search.model_dump()
    await Searcher(search_engine=SearchEngine(engine=search.api_type, **kwargs)).run(question)


if __name__ == "__main__":
    asyncio.run(main())
