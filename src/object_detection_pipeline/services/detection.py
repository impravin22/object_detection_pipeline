from __future__ import annotations

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class DetectionService:
    """Domain service for Object detection orchestration."""

    def __init__(self, model_name: str = "dummy") -> None:
        self.model_name = model_name

    async def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("running detection service", extra={"keys": list(payload.keys())})
        return {"ok": True, "model": self.model_name, "received": list(payload.keys())}
