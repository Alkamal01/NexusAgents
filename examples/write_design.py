import asyncio

from nexus_agents.environment.mgx.mgx_env import MGXEnv
from nexus_agents.logs import logger
from nexus_agents.roles.architect import Architect
from nexus_agents.roles.di.team_leader import TeamLeader
from nexus_agents.schema import Message


async def main():
    msg = "Write a TRD for a snake game"
    env = MGXEnv()
    env.add_roles([TeamLeader(), Architect()])
    env.publish_message(Message(content=msg, role="user"))
    tl = env.get_role("Mike")
    await tl.run()

    role = env.get_role("Bob")
    result = await role.run(msg)
    logger.info(result)


if __name__ == "__main__":
    asyncio.run(main())
