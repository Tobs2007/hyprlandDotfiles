#! /usr/bin/python
import sys
from typing import Any


def execOperation(base,value,operation,fallback = "*"):  # pyright: ignore[reportMissingParameterType]
    """
    calculate `base (operation ?? fallback) value`
    """
    if not operation:
        operation = fallback
    match operation:
        case "+": return base + value
        case "-": return base - value
        case "*": return base * value
        case "/": return base / value
        case "^": return base ** value
        case _: raise Exception("invalid operator received")
        


def evaluateParsed(data: list[dict[str,Any]]) :  # pyright: ignore[reportExplicitAny]
    data = sorter(data)
    computeVal = 0
    operation = None
    for i in data:
        match i["type"]:

            case "sub":
                recurse = evaluateParsed(i["value"])
                computeVal = execOperation(computeVal,recurse,operation,"+")
            
            case "value":
                computeVal = execOperation(computeVal,i["value"],operation,"+")
                operation = None
            
            case "operation":
                operation = i["value"]
            
            case _: print("invalid argument type")
    return computeVal

def sorter(data: list[Any]):  # pyright: ignore[reportExplicitAny]
    if len(data) < 2:
        return data
    indexbaked = {}
    for index,e in enumerate(data):
        indexbaked.update({index: e})
    for e in indexbaked.copy().items():
        index, d = e
        
        if d["value"] in ["*","/","^"] and len(data) > 3:
            repIndexes = [index-1,index,index+1]
            available = indexbaked.keys()
            impossible = False
            for ind in repIndexes:
                if ind not in available:
                    impossible = True
            
            if not impossible:
                # remove old values
                new = []
                # new.append({"type": "value","value":1})
                new.append(indexbaked[index-1])
                new.append(indexbaked[index])
                new.append(indexbaked[index+1])
                for i in [-1,0,1]:
                    indexbaked.pop(index+i)
                indexbaked.update({index+1: {"type": "sub","value": new}})
    return list(indexbaked.values())
            



CHARS_SUB = "("
CHARS_NUM = "1234567890."
CHARS_OPERATOR = "+-*/^"



def getIndexOfFirstIdentifier(data: str):
    matchers, identifierType = None, None

    if data[0] in CHARS_SUB:
        matchers = CHARS_NUM+CHARS_OPERATOR
        identifierType = "SUB"

    elif data[0] in CHARS_NUM:
        matchers = CHARS_SUB+CHARS_OPERATOR
        identifierType = "NUM"

    elif data[0] in CHARS_OPERATOR:
        matchers = CHARS_SUB+CHARS_NUM
        identifierType = "OPERATOR"

    assert matchers


    for index, char in enumerate(data):
        if char in matchers:
            return index, identifierType

    return len(data), identifierType


def getSubEnd(data: str):
    height = 0
    for index, char in enumerate(data):
        if char == "(": height += 1
        elif char == ")": height -= 1
        if height == 0: return index
    raise Exception("invalid bracket placement")

def deduplicateOperators(data: list[Any]):  # pyright: ignore[reportExplicitAny]
    previousIsOperator = False
    indexbaked = {}
    for index,e in enumerate(data):
        indexbaked.update({index: e})
    for index, value in indexbaked.copy().items():
        if value["type"] == "operation":
            if previousIsOperator:
                indexbaked.pop(index)
            previousIsOperator = True
        else:
            previousIsOperator = False
        if value["type"] == "sub":
            indexbaked[index]["value"] = deduplicateOperators(indexbaked[index]["value"])
    return list(indexbaked.values())

def getNextSegment(data: str):
    index, identifier = getIndexOfFirstIdentifier(data)
    match identifier:
        case "NUM":
            if data[:index].find(".") == -1:
                value = int(data[:index])
            else:
                value = float(data[:index])
            

            return [{"type": "value","value": value}] ,data[index:]

        case "OPERATOR":
            return [{"type": "operation","value": data[:index]}] ,data[index:]

        case "SUB":
            end = getSubEnd(data)
            inner = data[1:end]
            outer = data[end+1:]

            return [{"type": "operation","value": "*"},{"type": "sub","value": parseEquation(inner)}] ,outer
        case _: raise Exception("failed to parse",data)


def parseEquation(data: str):
    result = []
    element, further = getNextSegment(data)
    for i in element:
        result.append(i)
    while further != "":
        element, further = getNextSegment(further)
        for i in element:
            result.append(i)
    if result[0]["type"] == "operation" and result[0]["value"] in "*/":
        result[0]["value"] = "+"
    return result

def pasreEvaluate(data: str):

    parsed = parseEquation(data.replace(" ",""))
    parsed = deduplicateOperators(parsed)
    return evaluateParsed(parsed)

try:
    if len(sys.argv) > 1:
        res = pasreEvaluate(sys.argv[1])
        if res != "":
            print(res)
        else:
            print("empty return")
    else:
        print("Calculator")
except Exception as e:
    print("invalid",str(e))