from permissions.base import ModelPermissionsMixin


class Users(ModelPermissionsMixin):
    __PERMISSIONS__ = [
        'VIEW_ME',
        'EDIT_ME',
        'CHANGE_PASSWORD',
        'VIEW_ROLES'
    ]
