"""
Copyright (c) 2023 Gou Haoming
chineseEasyWordcloud is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""

from typing import List
import jieba
from . import stopwords
import re

def cutChinese(content: str) -> List[str]:
    return [i for i in jieba.cut(content) if isinstance(i,str)]

def removeStopwords(content: List[str],stopwords: List[str]=stopwords.getDefault()) -> List[str]:
    return [i for i in content if i not in stopwords]

def removeWhiteSpace(content: List[str]) -> List[str]:
    return [i for i in content if re.match(r"^\S*$",i)]


def removeNonsenseCharacter(content: List[str]) -> List[str]:
    return [i for i in content if re.match(r"^[\w]*$", i) and i not in ["\n","\t"]]

def cutWordDefault(content: str) -> List[str]:
    return removeNonsenseCharacter(removeWhiteSpace(removeStopwords(cutChinese(content))))
