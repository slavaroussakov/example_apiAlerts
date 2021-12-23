"""This file houses the CheckFactory, of which there should only be one instance"""
from checks import PriceDeviationCheck
from repos import PublicApiRepo
from result_processors import StdoutProcessor


class CheckFactory():
    """This class is reponsible for determining the type of check to run
    based on input from our entry point, as well as assembling any
    dependencies needed to construct those checks. Checks should not be
    responsible for gathering their own dependencies."""

    def get_check_by_parameter(self, parameter):
        """Determine which check to use, then build and return.
        Currently this ignores parameter input as there is only
        one check."""
        match parameter:
            case _:
                return PriceDeviationCheck(PublicApiRepo(), StdoutProcessor())
