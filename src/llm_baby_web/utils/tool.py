# -*- encoding: utf-8 -*-
"""
@Time    :   2024-01-25 23:26:23
@desc    :   some common tools
@Author  :   ticoAg
@Contact :   1627635056@qq.com
"""
from loguru import logger
from pathlib import Path
import json


def loadJS(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def dumpJS(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)

def dumpsJS(obj):
    return json.dumps(obj, ensure_ascii=False)


class Args:
    ...


args = Args()


logger.add(
    Path("logs", "chatbot.log"),
    encoding="utf-8",
    rotation="00:00",
    retention="10 days",
    compression="gz",
    backtrace=True,
    diagnose=True,
)
