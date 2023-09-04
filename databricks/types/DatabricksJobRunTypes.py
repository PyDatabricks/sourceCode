from databricks.types.DatabricksJobManagerTypes import (
    DatabricksCreateJobContinuousType,
    DatabricksCreateJobEmailNotificationType,
    DatabricksCreateJobGitSourceType,
    DatabricksCreateJobHealthType,
    DatabricksCreateJobNotificationSettingsType,
    DatabricksCreateJobRunAsType,
    DatabricksCreateJobScheduleType,
    DatabricksCreateJobTasksDbtTaskType,
    DatabricksCreateJobTasksLibrariesType,
    DatabricksCreateJobTasksNewClusterType,
    DatabricksCreateJobTasksPipelineTaskType,
    DatabricksCreateJobTasksPythonWheelTaskType,
    DatabricksCreateJobTasksSparkJarTaskType,
    DatabricksCreateJobTasksSparkPythonTaskType,
    DatabricksCreateJobTasksSparkSubmitTaskType,
    DatabricksCreateJobTasksSqlTaskType,
    DatabricksCreateJobTriggerType,
    DatabricksCreateJobWebhookNorificationType
)
from typing import (
    Dict, 
    List,
    Literal,
    TypedDict
)
from databricks.databricks import Databricks

class JobRunOutputNotebookOutputType(TypedDict):
    result: str
    truncated: bool

class JobRunOutputSqlOutputQueryOutputSqlStatementType(TypedDict):
    lookup_key: str

class JobRunOutputSqlOutputQueryOutputType(TypedDict):
    query_text: str
    warehouse_id: str
    sql_statements: List[JobRunOutputSqlOutputQueryOutputSqlStatementType]
    output_link: str

class JobRunOutputSqlOutputDashboardOutputWidgetErrorType(TypedDict):
    message: str

class JobRunOutputSqlOutputDashboardOutputWidgetType(TypedDict):
    widget_id: str
    widget_title: str
    output_link: str
    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED"]
    error: JobRunOutputSqlOutputDashboardOutputWidgetErrorType
    start_time: int
    end_time: int

class JobRunOutputSqlOutputDashboardOutputType(TypedDict):
    widgets: List[JobRunOutputSqlOutputDashboardOutputWidgetType]
    warehouse_id: str

class JobRunOutputSqlOutputAlertOutputSqlStatementType(TypedDict):
    lookup_key: str

class JobRunOutputSqlOutputAlertOutputType(TypedDict):
    query_text: str
    warehouse_id: str
    sql_statements: List[JobRunOutputSqlOutputAlertOutputSqlStatementType]
    output_link: str
    alert_state: Literal["UNKNOWN", "OK", "TRIGGERED"]

class JobRunOutputSqlOutputType(TypedDict):
    query_output: JobRunOutputSqlOutputQueryOutputType
    dashboard_output: JobRunOutputSqlOutputDashboardOutputType
    alert_output: JobRunOutputSqlOutputAlertOutputType

class JobRunOutputDbtOutputType(TypedDict):
    artifacts_link: str
    artifacts_headers: Dict[str, str]

class JobRunOutputRunJobOutputType(TypedDict):
    run_id: int

class JobRunOutputMetadataStateType(TypedDict):
    life_cycle_state: Literal["PENDING", "RUNNING", "TERMINATING", "TERMINATED", "SKIPPED", "INTERNAL_ERROR", "BLOCKED", "WAITING_FOR_RETRY"]
    result_state: Literal["SUCCESS", "FAILED", "TIMEDOUT", "CANCELED", "MAXIMUM_CONCURRENT_RUNS_REACHED", "EXCLUDED", "SUCCESS_WITH_FAILURES", "UPSTREAM_FAILED", "UPSTREAM_CANCELED"]
    user_cancelled_or_timedout: bool
    state_message: str

class JobRunOutputMetadataScheduleType(TypedDict):
    quartz_cron_expression: str
    timezone_id: str
    pause_status: Literal["PAUSED", "UNPAUSED"]

class JobRunOutputMetadataContinuousType(TypedDict):
    pause_status: Literal["PAUSED", "UNPAUSED"]

class JobRunOutputMetadataTaskStateType(TypedDict):
    life_cycle_state: Literal["PENDING", "RUNNING", "TERMINATING", "TERMINATED", "SKIPPED", "INTERNAL_ERROR", "BLOCKED", "WAITING_FOR_RETRY"]
    result_state: Literal["SUCCESS", "FAILED", "TIMEDOUT", "CANCELED", "MAXIMUM_CONCURRENT_RUNS_REACHED", "EXCLUDED", "SUCCESS_WITH_FAILURES", "UPSTREAM_FAILED", "UPSTREAM_CANCELED"]
    user_cancelled_or_timedout: bool
    state_message: str

class JobRunOutputMetadataTaskDependsOnType(TypedDict):
    task_key: str

class JobRunOutputMetadataTaskNewClusterType(DatabricksCreateJobTasksNewClusterType): pass

class JobRunOutputMetadataTaskLibraryType(DatabricksCreateJobTasksLibrariesType): pass

class JobRunOutputMetadataTaskNotebookTaskType(TypedDict):
    notebook_path: str
    source: Literal["WORKSPACE", "GIT"]
    base_parameters: Dict[str, str]

class JobRunOutputMetadataTaskSparkJarTaskType(DatabricksCreateJobTasksSparkJarTaskType): pass

class JobRunOutputMetadataTaskSparkPythonTaskType(DatabricksCreateJobTasksSparkPythonTaskType): pass

class JobRunOutputMetadataTaskSparkSubmitTaskType(DatabricksCreateJobTasksSparkSubmitTaskType): pass

class JobRunOutputMetadataTaskPipelineTaskType(DatabricksCreateJobTasksPipelineTaskType): pass

class JobRunOutputMetadataTaskPythonWheelTaskType(DatabricksCreateJobTasksPythonWheelTaskType): pass

class JobRunOutputMetadataTaskSqlTaskType(DatabricksCreateJobTasksSqlTaskType): pass

class JobRunOutputMetadataTaskDbtTaskType(DatabricksCreateJobTasksDbtTaskType): pass

class JobRunOutputMetadataTaskRunJobTaskType(TypedDict):
    job_id: int
    
class JobRunOutputMetadataTaskClusterInstanceType(TypedDict):
    cluster_id: str
    spark_context_id: str

class JobRunOutputMetadataTaskGitSourceType(DatabricksCreateJobGitSourceType): pass


class JobRunOutputMetadataTaskType(TypedDict):
    run_id: int
    task_key: str
    description: str
    run_if: Literal["ALL_SUCCESS", "AT_LEAST_ONE_SUCCESS", "NONE_FAILED", "ALL_DONE", "AT_LEAST_ONE_FAILED", "ALL_FAILED"]
    state: JobRunOutputMetadataTaskStateType
    depends_on: List[JobRunOutputMetadataTaskDependsOnType]
    existing_cluster_id: str
    new_cluster: JobRunOutputMetadataTaskNewClusterType
    libraries: List[JobRunOutputMetadataTaskLibraryType]
    notebook_task: JobRunOutputMetadataTaskNotebookTaskType
    spark_jar_task: JobRunOutputMetadataTaskSparkJarTaskType
    spark_python_task: JobRunOutputMetadataTaskSparkPythonTaskType
    spark_submit_task: JobRunOutputMetadataTaskSparkSubmitTaskType
    pipeline_task: JobRunOutputMetadataTaskPipelineTaskType
    python_wheel_task: JobRunOutputMetadataTaskPythonWheelTaskType
    sql_task: JobRunOutputMetadataTaskSqlTaskType
    dbt_task: JobRunOutputMetadataTaskDbtTaskType
    run_job_task: JobRunOutputMetadataTaskRunJobTaskType
    start_time: int
    setup_duration: int
    execution_duration: int
    cleanup_duration: int
    end_time: int
    attempt_number: int
    cluster_instance: JobRunOutputMetadataTaskClusterInstanceType
    git_source: JobRunOutputMetadataTaskGitSourceType

class JobRunOutputMetadataJobClusterNewClusterType(JobRunOutputMetadataTaskNewClusterType): pass

class JobRunOutputMetadataJobClusterType(TypedDict):
    job_cluster_key: str
    new_cluster: JobRunOutputMetadataJobClusterNewClusterType

class JobRunOutputMetadataClusterSpecNewClusterType(JobRunOutputMetadataTaskNewClusterType): pass

class JobRunOutputMetadataClusterSpecLibraryType(DatabricksCreateJobTasksLibrariesType): pass

class JobRunOutputMetadataClusterSpecType(TypedDict):
    existing_cluster_id: str
    new_cluster: JobRunOutputMetadataClusterSpecNewClusterType
    libraries: List[JobRunOutputMetadataClusterSpecLibraryType]

class JobRunOutputMetadataClusterInstanceType(TypedDict):
    cluster_id: str
    spark_context_id: str

class JobRunOutputMetadataGitSourceType(DatabricksCreateJobGitSourceType): pass

class JobRunOutputMetadataOverridingParametersPipelineParamsType(TypedDict):
    full_refresh: bool

class JobRunOutputMetadataOverridingParametersType(TypedDict):
    jar_params: List[str]
    notebook_params: Dict[str, str]
    python_params: List[str]
    spark_submit_params: List[str]
    python_named_params: Dict[str, str]
    pipeline_params: JobRunOutputMetadataOverridingParametersPipelineParamsType
    sql_params: Dict[str, str]
    dbt_commands: List[str]

class JobRunOutputMetadataTriggerInfoType(TypedDict):
    run_id: int

class JobRunOutputMetadataRepairHistoryStateType(TypedDict):
    life_cycle_state: Literal["PENDING", "RUNNING", "TERMINATING", "TERMINATED", "SKIPPED", "INTERNAL_ERROR", "BLOCKED", "WAITING_FOR_RETRY"]
    result_state: Literal["SUCCESS", "FAILED", "TIMEDOUT", "CANCELED", "MAXIMUM_CONCURRENT_RUNS_REACHED", "EXCLUDED", "SUCCESS_WITH_FAILURES", "UPSTREAM_FAILED", "UPSTREAM_CANCELED"]
    user_cancelled_or_timedout: bool
    state_message: str

class JobRunOutputMetadataRepairHistoryType(TypedDict):
    type: Literal["ORIGINAL", "REPAIR"]
    start_time: int
    end_time: int
    state: JobRunOutputMetadataRepairHistoryStateType
    id: int
    task_run_ids: List[int]

class JobRunOutputMetadataType(TypedDict):
    job_id: int
    run_id: int
    creator_user_name: str
    original_attempt_run_id: int
    state: JobRunOutputMetadataStateType
    schedule: JobRunOutputMetadataScheduleType
    continuous: JobRunOutputMetadataContinuousType
    tasks: List[JobRunOutputMetadataTaskType]
    job_clusters: List[JobRunOutputMetadataJobClusterType]
    cluster_spec: JobRunOutputMetadataClusterSpecType
    cluster_instance: JobRunOutputMetadataClusterInstanceType
    git_source: JobRunOutputMetadataGitSourceType
    overriding_parameters: JobRunOutputMetadataOverridingParametersType
    start_time: int
    setup_duration: int
    execution_duration: int
    cleanup_duration: int
    end_time: int
    trigger_info: JobRunOutputMetadataTriggerInfoType
    run_duration: int
    trigger: Literal["PERIODIC", "ONE_TIME", "RETRY", "RUN_JOB_TASK", "FILE_ARRIVAL"]
    run_name: str
    run_page_url: str
    run_type: Literal["JOB_RUN", "WORKFLOW_RUN", "SUBMIT_RUN"]
    attempt_number: int
    repair_history: List[JobRunOutputMetadataRepairHistoryType]

class JobRunOutputResponseType(TypedDict):
    notebook_output: JobRunOutputNotebookOutputType
    sql_output: JobRunOutputSqlOutputType
    dbt_output: JobRunOutputDbtOutputType
    run_job_output: JobRunOutputRunJobOutputType
    logs: str
    logs_truncated: bool
    error: str
    error_trace: str
    metadata: JobRunOutputMetadataType

class DatabricksJobRunPipelineParamsType(TypedDict):
    full_refresh: bool

class DatabricksJobRunRequestType(TypedDict):
    rerun_tasks: List[str]
    latest_repair_id: int
    rerun_all_failed_tasks: bool
    jar_params: List[str]
    notebook_params: Dict[str, str]
    python_params: List[str]
    spark_submit_params: List[str]
    python_named_params: Dict[str, str]
    pipeline_params: DatabricksJobRunPipelineParamsType
    sql_params: Dict[str, str]
    dbt_commands: List[str]

class DatabricksJobRunResponseType(TypedDict):
    repair_id: int

class DatabricksJobInfoSettingsEmailNotificationsType(DatabricksCreateJobEmailNotificationType): pass

class DatabricksJobInfoSettingsTriggerType(DatabricksCreateJobTriggerType): pass

class DatabricksJobInfoSettingsWebhookNotificationsType(DatabricksCreateJobWebhookNorificationType): pass

class DatabricksJobInfoSettingsNotificationSettingsType(DatabricksCreateJobNotificationSettingsType): pass

class DatabricksJobInfoSettingsHealthType(DatabricksCreateJobHealthType): pass

class DatabricksJobInfoSettingsScheduleType(DatabricksCreateJobScheduleType): pass

class DatabricksJobInfoSettingsContinuousType(DatabricksCreateJobContinuousType): pass

class DatabricksJobInfoSettingsGitSourceType(DatabricksCreateJobGitSourceType): pass

class DatabricksJobInfoSettingsRunAsType(DatabricksCreateJobRunAsType): pass


class DatabricksJobInfoSettingsType(TypedDict):
    name: str
    tags: Dict[str, str]
    email_notifications: DatabricksJobInfoSettingsEmailNotificationsType
    trigger: DatabricksJobInfoSettingsTriggerType
    webhook_notifications: DatabricksJobInfoSettingsWebhookNotificationsType
    notification_settings: DatabricksJobInfoSettingsNotificationSettingsType
    timeout_seconds: int
    health: DatabricksJobInfoSettingsHealthType
    schedule: DatabricksJobInfoSettingsScheduleType
    continuous: DatabricksJobInfoSettingsContinuousType
    max_concurrent_runs: int
    git_source: DatabricksJobInfoSettingsGitSourceType
    run_as: DatabricksJobInfoSettingsRunAsType

class DatabricksJobInfoTriggerHistoryLastTriggeredType(TypedDict):
    timestamp: int
    description: str
    run_id: int

class DatabricksJobInfoTriggerHistoryLastNotTriggeredType(TypedDict):
    timestamp: int
    description: str
    run_id: int

class DatabricksJobInfoTriggerHistoryLastFailedType(TypedDict):
    timestamp: int
    description: str
    run_id: int

class DatabricksJobInfoTriggerHistoryType(TypedDict):
    last_triggered: DatabricksJobInfoTriggerHistoryLastTriggeredType
    last_not_triggered: DatabricksJobInfoTriggerHistoryLastNotTriggeredType
    last_failed: DatabricksJobInfoTriggerHistoryLastFailedType

class DatabricksJobInfoResponseType(TypedDict):
    job_id: int
    creator_user_name: str
    settings: DatabricksJobInfoSettingsType
    created_time: int
    run_as_user_name: str
    trigger_history: DatabricksJobInfoTriggerHistoryType


class DatabricksJobRunInfoStateType(TypedDict):
    life_cycle_state: Literal["PENDING", "RUNNING", "TERMINATING", "TERMINATED", "SKIPPED", "INTERNAL_ERROR", "BLOCKED", "WAITING_FOR_RETRY"]
    result_state: Literal["SUCCESS", "FAILED", "TIMEDOUT", "CANCELED", "MAXIMUM_CONCURRENT_RUNS_REACHED", "EXCLUDED", "SUCCESS_WITH_FAILURES", "UPSTREAM_FAILED", "UPSTREAM_CANCELED"]
    user_cancelled_or_timedout: bool
    state_message: str

class DatabricksJobRunInfoScheduleType(TypedDict):
    quartz_cron_expression: str
    timezone_id: str
    pause_status: Literal["PAUSED", "UNPAUSED"]

class DatabricksJobRunInfoContinuousType(TypedDict):
    pause_status: Literal["PAUSED", "UNPAUSED"]

class DatabricksJobRunInfoTaskType(JobRunOutputMetadataTaskType): pass

class DatabricksJobRunInfoJobClusterNewClusterType(JobRunOutputMetadataTaskNewClusterType): pass

class DatabricksJobRunInfoJobClusterType(TypedDict):
    job_cluster_key: str
    new_cluster: DatabricksJobRunInfoJobClusterNewClusterType

class DatabricksJobRunInfoClusterSpecType(JobRunOutputMetadataClusterSpecType): pass

class DatabricksJobRunInfoClusterInstanceType(JobRunOutputMetadataClusterInstanceType): pass

class DatabricksJobRunInfoGitSourceType(JobRunOutputMetadataGitSourceType): pass

class DatabricksJobRunInfoOverridingParametersType(JobRunOutputMetadataOverridingParametersType): pass

class DatabricksJobRunInfoTriggerInfoType(JobRunOutputMetadataTriggerInfoType): pass

class DatabricksJobRunInfoRepairHistoryType(JobRunOutputMetadataRepairHistoryType): pass

class DatabricksJobRunInfoResponseType(TypedDict):
    job_id: int
    run_id: int
    creator_user_name: str
    original_attempt_run_id: int
    state: DatabricksJobRunInfoStateType
    schedule: DatabricksJobRunInfoScheduleType
    continuous: DatabricksJobRunInfoContinuousType
    tasks: List[DatabricksJobRunInfoTaskType]
    job_clusters: List[DatabricksJobRunInfoJobClusterType]
    cluster_spec: DatabricksJobRunInfoClusterSpecType
    cluster_instance: DatabricksJobRunInfoClusterInstanceType
    git_source: DatabricksJobRunInfoGitSourceType
    overriding_parameters: DatabricksJobRunInfoOverridingParametersType
    start_time: int
    setup_duration: int
    execution_duration: int
    cleanup_duration: int
    end_time: int
    trigger_info: DatabricksJobRunInfoTriggerInfoType
    run_duration: int
    trigger: Literal["PERIODIC", "ONE_TIME", "RETRY", "RUN_JOB_TASK", "FILE_ARRIVAL"]
    run_name: str
    run_page_url: str
    run_type: Literal["JOB_RUN", "WORKFLOW_RUN", "SUBMIT_RUN"]
    attempt_number: int
    repair_history: List[DatabricksJobRunInfoRepairHistoryType]