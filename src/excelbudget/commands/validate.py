from argparse import Namespace, _SubParsersAction
from typing import List

from excelbudget.commands.abstractcommand import AbstractCommand


class Validate(AbstractCommand):
    """The `validate` command implementation.

    Attributes:
        name (str): The command's CLI name.
        aliases (List[str]): The command's CLI aliases.
    """

    name: str = "validate"
    aliases: List[str] = ["v"]

    @classmethod
    def configure_args(cls, subparsers: _SubParsersAction) -> None:
        """Configures the argument parser for the `validate` command.

        Args:
            subparsers (_SubParsersAction): The command `subparsers`.
        """
        parser = subparsers.add_parser(
            cls.name, aliases=cls.aliases, help="validate an existing excelbudget file"
        )
        parser.set_defaults(init=Validate)

    def __init__(self, args: Namespace) -> None:
        raise NotImplementedError

    def run(self) -> None:
        raise NotImplementedError
