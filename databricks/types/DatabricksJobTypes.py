from typing import (
    Dict,
    List,
    TypedDict
)

class DatabricksRunJobPipelineParamsType(TypedDict):
    full_refresh: bool

class DatabricksRunJobRequestType(TypedDict):
    idempotency_token: str
    jar_params: List[str]
    notebook_params: Dict[str, str]
    python_params: List[str]
    spark_submit_params: List[str]
    python_named_params: Dict[str, str]
    pipeline_params: DatabricksRunJobPipelineParamsType
    sql_params: Dict[str, str]
    dbt_commands: List[str]

class DatabricksRunJobResponseType(TypedDict):
    run_id: int