import asyncio
import dataclasses
import email.message
import inspect
import json
from contextlib import AsyncExitStack, asynccontextmanager
from enum import Enum, IntEnum
from typing import (
    Any,
    AsyncIterator,
    Callable,
    Coroutine,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

from fastapi import params
from fastapi._compat import (
    ModelField,
    Undefined,
    _get_model_config,
    _model_dump,
    _normalize_errors,
    lenient_issubclass,
)
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import (
    _should_embed_body_fields,
    get_body_field,
    get_dependant,
    get_flat_dependant,
    get_parameterless_sub_dependant,
    get_typed_return_annotation,
    solve_dependencies,
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import (
    FastAPIError,
    RequestValidationError,
    ResponseValidationError,
    WebSocketRequestValidationError,
)
from fastapi.types import DecoratedCallable, IncEx
from fastapi.utils import (
    create_cloned_field,
    create_model_field,
    generate_unique_id,
    get_value_or_default,
    is_body_allowed_for_status_code,
)
from pydantic import BaseModel
from starlette import routing
from starlette.concurrency import run_in_thread