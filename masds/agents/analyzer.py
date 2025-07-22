PROMPT = """
You are an experienced Product Manager in a Multi-Agent Software Development System.
Your job is to read a project description and a list of previous conversations (if given).
You should read the project description (and previous conversation) carefully and write a Product Requirement Document (PRD) if the project description in clear.
Otherwise, you should ask follow-up questions to gather information for writing a PRD.
 
your response should be exactly in this JSON format:
{{
"reasoning": "<your internal reasoning and chain of thoughts>",
    "is_clear": "<boolean (true | false). whether the project description is clear for writing a PRD or not>",
    "prd": "<a dictionary-based PRD if you have all the necessary information. otherwise, leave it blank.>",
    "questions": [ // list of follow-up questions if the project description is not clear for writing a PRD. otherwise, leave it blank.
        "question 1",
        "question 2",
        ...
    ] 
}}

Project Description:
{description}

Previous Messages:
{messages}
"""


from typing_extensions import Any, TypedDict, List, Dict
import copy

from .. import constants as C, utils


class AnalyzerState(TypedDict):
    reasoning: str
    messages: List[Dict[str, str]]
    prd: dict[str, Any]
    is_clear: bool


def analysis_agent(state):
    messages = []
    is_clear = False
    description = state["description"]

    while not is_clear:
        prompt = PROMPT.format(description=description, messages=messages)

        a_resp = C.LLM.invoke(prompt).content
        a_resp = utils.convert_response_to_json(a_resp)

        a_resp["is_clear"] = a_resp["is_clear"] in (True, "True", "true", "1", 1)
        is_clear = a_resp["is_clear"]

        if not is_clear:
            for i, q in enumerate(a_resp["questions"]):
                u_resp = input(f"({i + 1}/{len(a_resp['questions'])}) | {q}\n")
                messages.append({"assistant_question": q, "user_response": u_resp})

    result = copy.deepcopy(state)
    result["analyzer"] = copy.deepcopy(a_resp)

    print("################")
    for k, v in a_resp.items():
        print(f"{k=}: {type(v)} | {v=}")
    print("################")

    utils.write_json_file("../.masds_cache/prd.json", a_resp["prd"])

    return result
