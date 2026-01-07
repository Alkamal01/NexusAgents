import asyncio

from nexus_agents.logs import logger
from nexus_agents.roles.di.data_interpreter import DataInterpreter
from nexus_agents.utils.recovery_util import save_history


async def main(requirement: str = ""):
    di = DataInterpreter()
    rsp = await di.run(requirement)
    logger.info(rsp)
    save_history(role=di)


if __name__ == "__main__":
    requirement = "Run data analysis on sklearn Iris dataset, include a plot"
    asyncio.run(main(requirement))
