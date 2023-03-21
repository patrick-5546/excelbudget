"""Excelbudget: a personal bookkeeping assistant."""

from .configure import post_state_configuration, pre_state_configuration
from .state import setup_state


def main():
    "Entry point for the application script."
    pre_config = pre_state_configuration()
    state = setup_state(pre_config)
    post_state_configuration(state)
    state.cmd.run()