from __future__ import annotations

import argparse
import ast
import logging
from collections.abc import Generator
from typing import Any

import pyflakes.checker

from flake8.options.manager import OptionManager

LOG = logging.getLogger(__name__)

FLAKE8_PYFLAKES_CODES = {
    "UnusedImport": "F401",
    "ImportShadowedByLoopVar": "F402",
    "ImportStarUsed": "F403",
    "LateFutureImport": "F404",
    "ImportStarUsage": "F405",
    "ImportStarNotPermitted": "F406",
    "FutureFeatureNotDefined": "F407",
    "PercentFormatInvalidFormat": "F501",
    "PercentFormatExpectedMapping": "F502",
    "PercentFormatExpectedSequence": "F503",
    "PercentFormatExtraNamedArguments": "F504",
    "PercentFormatMissingArgument": "F505",
    "PercentFormatMixedPositionalAndNamed": "F506",
    "PercentFormatPositionalCountMismatch": "F507",
    "PercentFormatStarRequiresSequence": "F508",
    "PercentFormatUnsupportedFormatCharacter": "F509",
    "StringDotFormatInvalidFormat": "F521",
    "StringDotFormatExtraNamedArguments": "F522",
    "StringDotFormatExtraPositionalArguments": "F523",
    "StringDotFormatMissingArgument": "F524",
    "StringDotFormatMixingAutomatic": "F525",
    "FStringMissingPlaceholders": "F541",
    "TStringMissingPlaceholders": "F542",
    "MultiValueRepeatedKeyLiteral": "F601",
    "MultiValueRepeatedKeyVariable": "F602",
    "TooManyExpressionsInStarredAssignment": "F621",
    "TwoStarredExpressions": "F622",
    "AssertTuple": "F631",
    "IsLiteral": "F632",
    "InvalidPrintSyntax": "F633",
    "IfTuple": "F634",
    "BreakOutsideLoop": "F701",
    "ContinueOutsideLoop": "F702",
    "YieldOutsideFunction": "F704",
    "ReturnOutsideFunction": "F706",
    "DefaultExceptNotLast": "F707",
    "DoctestSyntaxError": "F721",
    "ForwardAnnotationSyntaxError": "F722",
    "RedefinedWhileUnused": "F811",
    "UndefinedName": "F821",
    "UndefinedExport": "F822",
    "UndefinedLocal": "F823",
    "UnusedIndirectAssignment": "F824",
    "DuplicateArgument": "F831",
    "UnusedVariable": "F841",
    "UnusedAnnotation": "F842",
    "RaiseNotImplemented": "F901",
}


class FlakesChecker(pyflakes.checker.Checker):
    with_doctest = False

    def __init__(self, tree: Any, filename: str) -> None:
        ...

    @classmethod
    def add_options(cls, parser: OptionManager) -> None:
        ...

    @classmethod
    def parse_options(cls, options: Any) -> None:
        ...

    def run(self) -> Generator:
        ...