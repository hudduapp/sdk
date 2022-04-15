from sdk.projects import get_project, create_project, list_projects, update_project


class Data:
    def __init__(self, token: str) -> None:
        self.token = token

    class Projects:
        def __init__(self, account_id: str) -> None:
            self.account_id = account_id

        def create(**args):
            create_project(account_id=account_id, **args)

        def get(**args):
            get_project(account_id=account_id, **args)

        def list(**args):
            get_projects(account_id=account_id, **args)

        def update(**args):
            update_project(account_id=account_id, **args)

        def delete(**args):
            print("-- dummy")
