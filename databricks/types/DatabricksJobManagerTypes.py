from typing import (
    Dict,
    List,
    Literal,
    TypedDict
)

class DatabricksCreateJobTasksDependsOnType(TypedDict):
    task_key: str

class DatabricksCreateJobTasksNewClusterAzureAttrLogAnalyticsInfoType(TypedDict):
    log_analytics_workspace_id: str
    log_analytics_primary_key: str

class DatabricksCreateJobTasksNewClusterAzureAttrType(TypedDict):
    log_analytics_info: DatabricksCreateJobTasksNewClusterAzureAttrLogAnalyticsInfoType
    first_on_demand: int
    availability: Literal["SPOT_AZURE", "ON_DEMAND_AZURE", "SPOT_WITH_FALLBACK_AZURE"]
    spot_bid_max_price: float

class DatabricksCreateJobTasksNewClusterClusterLogInfoDBFSType(TypedDict):
    destination: str

class DatabricksCreateJobTasksNewClusterClusterLogInfoType(TypedDict):
    dbfs: DatabricksCreateJobTasksNewClusterClusterLogInfoDBFSType

class DatabricksCreateJobTasksNewClusterInitScriptsWorkspaceType(TypedDict):
    destination: str

class DatabricksCreateJobTasksNewClusterInitScriptsType(TypedDict):
    workspace: DatabricksCreateJobTasksNewClusterInitScriptsWorkspaceType

class DatabricksCreateJobTasksNewClusterWorkloadClientsType(TypedDict):
    notebooks: bool
    jobs: bool

class DatabricksCreateJobTasksNewClusterWorkloadType(TypedDict):
    clients: DatabricksCreateJobTasksNewClusterWorkloadClientsType

class DatabricksCreateJobTasksNewClusterDockerImageBasicAuthType(TypedDict):
    username: str
    password: str

class DatabricksCreateJobTasksNewClusterDockerImageType(TypedDict):
    url: str
    basic_auth: DatabricksCreateJobTasksNewClusterDockerImageBasicAuthType

class DatabricksCreateJobTasksNewClusterAutoScaleType(TypedDict):
    min_workers: int
    max_workers: int

class DatabricksCreateJobTasksNewClusterType(TypedDict):
    cluster_name: str
    spark_version: str
    spark_conf: Dict[str, str]
    azure_attributes: DatabricksCreateJobTasksNewClusterAzureAttrType
    node_type_id: str
    driver_node_type_id: str
    ssh_public_keys: List[str]
    custom_tags: Dict[str, str]
    cluster_log_conf: DatabricksCreateJobTasksNewClusterClusterLogInfoType
    init_scripts: List[DatabricksCreateJobTasksNewClusterInitScriptsType]
    spark_env_vars: Dict[str, str]
    autotermination_minutes: int
    enable_elastic_disk: bool
    cluster_source: Literal["UI", "JOB", "API", "SQL", "MODELS", "PIPELINE", "PIPELINE_MAINTENANCE"]
    instance_pool_id: str
    policy_id: str
    enable_local_disk_encryption: bool
    driver_instance_pool_id: str
    workload_type: DatabricksCreateJobTasksNewClusterWorkloadType
    runtime_engine: Literal["NULL", "STANDARD", "PHOTON"]
    docker_image: DatabricksCreateJobTasksNewClusterDockerImageType
    data_security_mode: Literal["NONE", "SINGLE_USER", "USER_ISOLATION", "LEGACY_TABLE_ACL", "LEGACY_PASSTHROUGH", "LEGACY_SINGLE_USER"]
    single_user_name: str
    num_workers: int
    autoscale: DatabricksCreateJobTasksNewClusterAutoScaleType

class DatabricksCreateJobTasksNotebookTaskType(TypedDict):
    notebook_path: str
    source: Literal["WORKSPACE", "GIT"]
    base_parameters: Dict[str, str]

class DatabricksCreateJobTasksSparkJarTaskType(TypedDict):
    main_class_name: str
    parameters: List[str]

class DatabricksCreateJobTasksSparkPythonTaskType(TypedDict):
    python_file: str
    source: Literal["WORKSPACE", "GIT"]
    parameters: List[str]

class DatabricksCreateJobTasksSparkSubmitTaskType(TypedDict):
    parameters: List[str]

class DatabricksCreateJobTasksPipelineTaskType(TypedDict):
    pipeline_id: str
    full_refresh: bool

class DatabricksCreateJobTasksPythonWheelTaskType(TypedDict):
    package_name: str
    entry_point: str
    parameters: List[str]
    named_parameters: Dict[str, str]

class DatabricksCreateJobTasksSqlTaskQueryType(TypedDict):
    query_id: str

class DatabricksCreateJobTasksSqlTaskSubscriptionsType(TypedDict):
    user_name: str
    destination_id: str

class DatabricksCreateJobTasksSqlTaskDashboardType(TypedDict):
    dashboard_id: str
    subscriptions: List[DatabricksCreateJobTasksSqlTaskSubscriptionsType]
    custom_subject: str
    pause_subscriptions: bool

class DatabricksCreateJobTasksSqlTaskAlertType(TypedDict):
    alert_id: str
    subscriptions: List[DatabricksCreateJobTasksSqlTaskSubscriptionsType]
    pause_subscriptions: bool

class DatabricksCreateJobTasksSqlTaskFileType(TypedDict):
    path: str

class DatabricksCreateJobTasksSqlTaskType(TypedDict):
    query: DatabricksCreateJobTasksSqlTaskQueryType
    dashboard: DatabricksCreateJobTasksSqlTaskDashboardType
    alert: DatabricksCreateJobTasksSqlTaskAlertType
    file: DatabricksCreateJobTasksSqlTaskFileType
    parameters: Dict[str, str]
    warehouse_id: str

class DatabricksCreateJobTasksDbtTaskType(TypedDict):
    project_directory: str
    commands: List[str]
    schema: str
    warehouse_id: str
    catalog: str
    profiles_directory: str

class DatabricksCreateJobTasksJobRunTaskType(TypedDict):
    job_id: int

class DatabricksCreateJobTasksLibrariesPypiType(TypedDict):
    package: str
    repo: str

class DatabricksCreateJobTasksLibrariesMavenType(TypedDict):
    coordinates: str
    repo: str
    exclusions: List[str]

class DatabricksCreateJobTasksLibrariesCranType(TypedDict):
    package: str
    repo: str

class DatabricksCreateJobTasksLibrariesType(TypedDict):
    jar: str
    egg: str
    pypi: DatabricksCreateJobTasksLibrariesPypiType
    maven: DatabricksCreateJobTasksLibrariesMavenType
    cran: DatabricksCreateJobTasksLibrariesCranType
    whl: str

class DatabricksCreateJobTasksEmailNotificationType(TypedDict):
    on_start: List[str]
    on_success: List[str]
    on_failure: List[str]
    on_duration_warning_threshold_exceeded: List[str]

class DatabricksCreateJobTasksNotificationSettingsType(TypedDict):
    no_alert_for_skipped_runs: bool
    no_alert_for_canceled_runs: bool
    alert_on_last_attempt: bool

class DatabricksCreateJobTasksHealthRulesType(TypedDict):
    metric: str
    op: str
    value: int

class DatabricksCreateJobHealthType(TypedDict):
    rules: List[DatabricksCreateJobTasksHealthRulesType]

class DatabricksCreateJobTasksType(TypedDict):
    task_key: str
    description: str
    depends_on: List[DatabricksCreateJobTasksDependsOnType]
    run_if: Literal["ALL_SUCCESS", "AT_LEAST_ONE_SUCCESS", "NONE_FAILED", "ALL_DONE", "AT_LEAST_ONE_FAILED", "ALL_FAILED"]
    existing_cluster_id: str
    new_cluster: DatabricksCreateJobTasksNewClusterType
    job_cluster_key: str
    notebook_task: DatabricksCreateJobTasksNotebookTaskType
    spark_jar_task: DatabricksCreateJobTasksSparkJarTaskType
    spark_python_task: DatabricksCreateJobTasksSparkPythonTaskType
    spark_submit_task: DatabricksCreateJobTasksSparkSubmitTaskType
    pipeline_task: DatabricksCreateJobTasksPipelineTaskType
    python_wheel_task: DatabricksCreateJobTasksPythonWheelTaskType
    sql_task: DatabricksCreateJobTasksSqlTaskType
    dbt_task: DatabricksCreateJobTasksDbtTaskType
    run_job_task: DatabricksCreateJobTasksJobRunTaskType
    libraries: List[DatabricksCreateJobTasksLibrariesType]
    email_notifications: DatabricksCreateJobTasksEmailNotificationType
    notification_settings: DatabricksCreateJobTasksNotificationSettingsType
    timeout_seconds: int
    health: DatabricksCreateJobHealthType
    max_retries: int
    min_retry_interval_millis: int
    retry_on_timeout: bool

class DatabricksCreateJobJobClusterType(TypedDict):
    job_cluster_key: str
    new_cluster: DatabricksCreateJobTasksNewClusterType


class DatabricksCreateJobEmailNotificationType(TypedDict):
    on_start: List[str]
    on_success: List[str]
    on_failure: List[str]
    on_duration_warning_threshold_exceeded: List[str]
    no_alert_for_skipped_runs: bool


class DatabricksCreateJobTriggerFileArrivalType(TypedDict):
    url: str
    min_time_between_triggers_seconds: int
    wait_after_last_change_seconds: int

class DatabricksCreateJobTriggerType(TypedDict):
    pause_status: Literal["PAUSED", "UNPAUSED"]
    file_arrival: DatabricksCreateJobTriggerFileArrivalType

class DatabricksCreateJobWebhookNorificationStartType(TypedDict):
    id: str

class DatabricksCreateJobWebhookNorificationSuccessType(TypedDict):
    id: str

class DatabricksCreateJobWebhookNorificationFailureType(TypedDict):
    id: str

class DatabricksCreateJobWebhookNorificationDurationWarningType(TypedDict):
    id: str

class DatabricksCreateJobWebhookNorificationType(TypedDict):
    on_start: List[DatabricksCreateJobWebhookNorificationStartType]
    on_success: List[DatabricksCreateJobWebhookNorificationSuccessType]
    on_failure: List[DatabricksCreateJobWebhookNorificationFailureType]
    on_duration_warning_threshold_exceeded: List[DatabricksCreateJobWebhookNorificationDurationWarningType]

class DatabricksCreateJobNotificationSettingsType(TypedDict):
    no_alert_for_skipped_runs: bool
    no_alert_for_canceled_runs: bool

class DatabricksCreateJobScheduleType(TypedDict):
    quartz_cron_expression: str
    timezone_id: str
    pause_status: Literal["PAUSED", "UNPAUSED"]

class DatabricksCreateJobContinuousType(TypedDict):
    pause_status: Literal["PAUSED", "UNPAUSED"]

class DatabricksCreateJobGitSourceType(TypedDict):
    git_url: str
    git_provider: Literal["gitHub", "bitbucketCloud", "azureDevOpsServices", "gitHubEnterprise", "bitbucketServer", "gitLab", "gitLabEnterpriseEdition", "awsCodeCommit"]
    git_branch: str
    git_tag: str
    git_commit: str

class DatabricksCreateJobRunAsType(TypedDict):
    user_name: str
    service_principal_name: str

class DatabricksCreateJobAccessControlType(TypedDict):
    user_name: str
    group_name: str
    service_principal_name: str
    permission_level: Literal["CAN_MANAGE", "CAN_RESTART", "CAN_ATTACH_TO", "IS_OWNER", "CAN_MANAGE_RUN", "CAN_VIEW", "CAN_READ", "CAN_RUN", "CAN_EDIT", "CAN_USE", "CAN_MANAGE_STAGING_VERSIONS", "CAN_MANAGE_PRODUCTION_VERSIONS", "CAN_EDIT_METADATA", "CAN_VIEW_METADATA", "CAN_BIND"]

class DatabricksCreateJobRequestType(TypedDict):
    name: str
    tags: Dict[str, str]
    tasks: List[DatabricksCreateJobTasksType]
    job_clusters: List[DatabricksCreateJobJobClusterType]
    email_notifications: DatabricksCreateJobEmailNotificationType
    trigger: DatabricksCreateJobTriggerType
    webhook_notifications: DatabricksCreateJobWebhookNorificationType
    notification_settings: DatabricksCreateJobNotificationSettingsType
    timeout_seconds: int
    health: DatabricksCreateJobHealthType
    schedule: DatabricksCreateJobScheduleType
    continuous: DatabricksCreateJobContinuousType
    max_concurrent_runs: int
    git_source: DatabricksCreateJobGitSourceType
    run_as: DatabricksCreateJobRunAsType
    access_control_list: List[DatabricksCreateJobAccessControlType]

class DatabricksCreateJobResponseType(TypedDict):
    job_id: int

class DatabricksListJobsJobSettingsType(DatabricksCreateJobRequestType):
    pass

class DatabricksListJobsJobType(TypedDict):
    job_id: int
    creator_user_name: str
    settings: DatabricksListJobsJobSettingsType
    created_time: int

class DatabricksListJobsResponseType(TypedDict):
    jobs: List[DatabricksListJobsJobType]
    has_more: bool
    next_page_token: str
    prev_page_token: str