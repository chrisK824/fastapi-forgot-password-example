from enum import Enum
from permissions.models_permissions import *
from typing import List


class Role(str, Enum):
    ADMINISTRATOR = "ADMINISTRATOR"
    USER = "USER"

    @classmethod
    def get_roles(cls):
        values = []
        for member in cls:
            values.append(f"{member.value}")
        return values


ROLE_PERMISSIONS = {
    Role.ADMINISTRATOR: [
        Users.permissions.FULL_PERMISSIONS,
    ],
    Role.USER: [
        [
            Users.permissions.CHANGE_PASSWORD,
            Users.permissions.VIEW_ME,
            Users.permissions.EDIT_ME
        ]
    ]
}


def get_role_permissions(role: Role):
    permissions = set()
    for permissions_group in ROLE_PERMISSIONS[role]:
        for permission in permissions_group:
            permissions.add(str(permission))
    return list(permissions)
