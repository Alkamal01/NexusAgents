"""
Filename: MetaGPT/examples/use_off_the_shelf_agent.py
Created Date: Tuesday, September 19th 2023, 6:52:25 pm
Author: garylin2099
"""
import asyncio

from nexus_agents.environment.mgx.mgx_env import MGXEnv
from nexus_agents.logs import logger
from nexus_agents.roles.di.team_leader import TeamLeader
from nexus_agents.roles.product_manager import ProductManager
from nexus_agents.schema import Message


async def main():
    msg = "Write a PRD for a snake game"
    env = MGXEnv()
    env.add_roles([TeamLeader(), ProductManager()])
    env.publish_message(Message(content=msg, role="user"))
    tl = env.get_role("Mike")
    await tl.run()

    role = env.get_role("Alice")
    result = await role.run(msg)
    logger.info(result.content[:100])


if __name__ == "__main__":
    asyncio.run(main())
