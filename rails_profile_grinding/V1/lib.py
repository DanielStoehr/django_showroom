from numbers import Number
from ..models import Specification
from typing import Union

LOWER_LIMIT = -5
UPPER_LIMIT = 5


def get_processes(data):

    d = dict()
    d["mainProgram"] = get_serialized_main_program(data["main_program_file"])
    d["time"] = get_serialized_time(data["process_time_in_minutes"])
    d["timestamp"] = get_serialized_timestamp(data["timestamp"])
    d["processTimeEvaluation"] = get_serialized_process_time_evaluation(
        data["main_program_file"], data["process_time_in_minutes"]
    )
    d["grindingTimeEvaluation"] = get_serialized_grinding_time_evaluation(
        data["main_program_file"], data["p004"]
    )
    d["dressingTimeEvaluation"] = get_serialized_dressing_time_evaluation(
        data["main_program_file"], data["p003"]
    )

    return d


def get_times_response(data, date_to: str, date_from: str, invnr: str, model_name: str):
    d = dict()

    d["inventoryNumber"] = invnr
    d["machineName"] = model_name.split("_")[0]
    d["dateFrom"] = date_from
    d["dateTo"] = date_to
    d["processes"] = [get_processes(x) for x in data]

    return d


def get_serialized_main_program(name: str):
    return {
        "value": name,
        "unit": "",
        "description": "Mainprogram grinding-process",
    }


def get_serialized_time(time: float):
    return {
        "value": time,
        "unit": "min",
        "description": "Process Time",
    }


def get_serialized_timestamp(timestamp: str):
    return {
        "value": timestamp,
        "unit": "YYYY-MM-DD hh-mm-ss",
        "description": "Timestamp of end of process",
    }


def get_serialized_process_time_evaluation(main_program: str, time: float):
    specification = get_specification(main_program)
    if not specification:
        value = 3
    else:
        value = evaluate(specification.target_process_time, time)
    return {
        "value": value,
        "unit": "",
        "description": {
            "0": "OK",
            "1": "over upper bound",
            "2": "under lower bound",
            "3": "undefined",
        },
    }


def get_serialized_grinding_time_evaluation(main_program: str, time: float):
    specification = get_specification(main_program)
    if not specification:
        value = 3
    else:
        value = evaluate(specification.target_grinding_time, time)
    return {
        "value": value,
        "unit": "",
        "description": {
            "0": "OK",
            "1": "over upper bound",
            "2": "under lower bound",
            "3": "undefined",
        },
    }


def get_serialized_dressing_time_evaluation(main_program: str, time: float):
    specification = get_specification(main_program)
    if not specification:
        value = 3
    else:
        value = evaluate(specification.target_dressing_time, time)
    return {
        "value": value,
        "unit": "",
        "description": {
            "0": "OK",
            "1": "over upper bound",
            "2": "under lower bound",
            "3": "undefined",
        },
    }


def get_specification(prog_name: str):
    request = Specification.objects.filter(prog_name=prog_name).first()
    if request:
        return request
    return None


def evaluate(target: float, value: float) -> int:
    deviation = (value / target - 1) * 100
    if deviation < LOWER_LIMIT:
        return 2
    if deviation > UPPER_LIMIT:
        return 1
    return 0
