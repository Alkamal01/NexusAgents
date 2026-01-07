from nexus_agents.environment.werewolf.const import RoleType
from nexus_agents.ext.werewolf.roles.base_player import BasePlayer


class Guard(BasePlayer):
    name: str = RoleType.GUARD.value
    profile: str = RoleType.GUARD.value
    special_action_names: list[str] = ["Protect"]
