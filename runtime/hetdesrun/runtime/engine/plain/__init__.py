from typing import Callable, Dict, Any, Union
import asyncio
import logging
from hetdesrun.runtime import RuntimeExecutionError, MissingOutputDataError
from hetdesrun.runtime.logging import execution_context_filter

from hetdesrun.runtime.engine.plain.workflow import Workflow
from hetdesrun.runtime import runtime_component_logger

from hetdesrun.runtime.engine.plain.execution import run_func_or_coroutine

logger = logging.getLogger(__name__)


logger.addFilter(execution_context_filter)
runtime_component_logger.addFilter(execution_context_filter)


async def workflow_execution_plain(workflow: Workflow) -> Dict[str, Any]:
    res: Dict[str, Any] = await workflow.result
    return res
