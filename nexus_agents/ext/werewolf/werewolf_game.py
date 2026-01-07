from typing import Any, Optional

from nexus_agents.actions.add_requirement import UserRequirement
from nexus_agents.context import Context
from nexus_agents.environment.werewolf.werewolf_env import WerewolfEnv
from nexus_agents.ext.werewolf.schema import WwMessage
from nexus_agents.team import Team


class WerewolfGame(Team):
    """Use the "software company paradigm" to hold a werewolf game"""

    env: Optional[WerewolfEnv] = None

    def __init__(self, context: Context = None, **data: Any):
        super(Team, self).__init__(**data)
        ctx = context or Context()
        if not self.env:
            self.env = WerewolfEnv(context=ctx)
        else:
            self.env.context = ctx  # The `env` object is allocated by deserialization

    def run_project(self, idea):
        """Run a project from user instruction."""
        self.idea = idea
        self.env.publish_message(
            WwMessage(role="User", content=idea, cause_by=UserRequirement, restricted_to={"Moderator"})
        )
