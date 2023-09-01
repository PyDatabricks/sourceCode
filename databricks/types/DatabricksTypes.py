from typing import (
    Dict,
    List,
    Literal,
    TypedDict
)


class DatabricksClusterAzureAttributesLogAnalyticsInfoType(TypedDict):
    log_analytics_workspace_id: str
    log_analytics_primary_key: str

class DatabricksClusterAzureAttributesType(TypedDict):
    log_analytics_info: DatabricksClusterAzureAttributesLogAnalyticsInfoType
    first_on_demand: int
    availability: Literal[ "SPOT_AZURE", "ON_DEMAND_AZURE", "SPOT_WITH_FALLBACK_AZURE" ]
    spot_bid_max_price: float

class DatabricksClusterSpecsClusterLogConfDBFSType(TypedDict):
    destination: str

class DatabricksClusterSpecsClusterLogConfType(TypedDict):
    dbfs: DatabricksClusterSpecsClusterLogConfDBFSType

class DatabricksClusterSpecsInitScriptsWorkspaceType(TypedDict):
    destination: str

class DatabricksClusterSpecsInitScriptsDBFSType(TypedDict):
    destination: str

class DatabricksClusterSpecsInitScriptsType(TypedDict):
    workspace: DatabricksClusterSpecsInitScriptsWorkspaceType
    dbfs: DatabricksClusterSpecsInitScriptsDBFSType


class DatabricksClusterSpecsWorkloadClientsType(TypedDict):
    notebooks: bool
    jobs: bool

class DatabricksClusterSpecsWorkloadType(TypedDict):
    clients: DatabricksClusterSpecsWorkloadClientsType


class DatabricksClusterSpecsDockerImageBasicAuthType(TypedDict):
    username: str
    password: str

class DatabricksClusterSpecsDockerImageType(TypedDict):
    url: str
    basic_auth: DatabricksClusterSpecsDockerImageBasicAuthType



class DatabricksClusterSpecsAutoScaleType(TypedDict):
    min_workers: int
    max_workers: int

class DatabricksClusterSpecsDriverType(TypedDict):
    private_ip: str
    public_dns: str
    node_id: str
    instance_id: str
    start_timestamp: int
    host_private_ip: str

class DatabricksClusterSpecsExecutorsType(TypedDict):
    private_ip: str
    public_dns: str
    node_id: str
    instance_id: str
    start_timestamp: int
    host_private_ip: str
    

class DatabricksClusterSpecsClusterLogStatusType(TypedDict):
    last_attempted: int
    last_exception: str


class DatabricksClusterSpecsTerminationReasonType(TypedDict):
    code: Literal[
        "UNKNOWN",
        "USER_REQUEST",
        "JOB_FINISHED",
        "INACTIVITY",
        "CLOUD_PROVIDER_SHUTDOWN",
        "COMMUNICATION_LOST",
        "CLOUD_PROVIDER_LAUNCH_FAILURE",
        "INIT_SCRIPT_FAILURE",
        "SPARK_STARTUP_FAILURE",
        "INVALID_ARGUMENT",
        "UNEXPECTED_LAUNCH_FAILURE",
        "INTERNAL_ERROR",
        "INSTANCE_UNREACHABLE",
        "REQUEST_REJECTED",
        "TRIAL_EXPIRED",
        "DRIVER_UNREACHABLE",
        "SPARK_ERROR",
        "DRIVER_UNRESPONSIVE",
        "METASTORE_COMPONENT_UNHEALTHY",
        "DBFS_COMPONENT_UNHEALTHY",
        "EXECUTION_COMPONENT_UNHEALTHY",
        "AZURE_RESOURCE_MANAGER_THROTTLING",
        "AZURE_RESOURCE_PROVIDER_THROTTLING",
        "NETWORK_CONFIGURATION_FAILURE",
        "CONTAINER_LAUNCH_FAILURE",
        "INSTANCE_POOL_CLUSTER_FAILURE",
        "SKIPPED_SLOW_NODES",
        "ATTACH_PROJECT_FAILURE",
        "UPDATE_INSTANCE_PROFILE_FAILURE",
        "DATABASE_CONNECTION_FAILURE",
        "REQUEST_THROTTLED",
        "SELF_BOOTSTRAP_FAILURE",
        "GLOBAL_INIT_SCRIPT_FAILURE",
        "SLOW_IMAGE_DOWNLOAD",
        "INVALID_SPARK_IMAGE",
        "NPIP_TUNNEL_TOKEN_FAILURE",
        "HIVE_METASTORE_PROVISIONING_FAILURE",
        "AZURE_INVALID_DEPLOYMENT_TEMPLATE",
        "AZURE_UNEXPECTED_DEPLOYMENT_TEMPLATE_FAILURE",
        "SUBNET_EXHAUSTED_FAILURE",
        "BOOTSTRAP_TIMEOUT",
        "STORAGE_DOWNLOAD_FAILURE",
        "CONTROL_PLANE_REQUEST_FAILURE",
        "BOOTSTRAP_TIMEOUT_CLOUD_PROVIDER_EXCEPTION",
        "AWS_INSUFFICIENT_INSTANCE_CAPACITY_FAILURE",
        "DOCKER_IMAGE_PULL_FAILURE",
        "AZURE_VNET_CONFIGURATION_FAILURE",
        "NPIP_TUNNEL_SETUP_FAILURE",
        "AWS_AUTHORIZATION_FAILURE",
        "NEPHOS_RESOURCE_MANAGEMENT",
        "STS_CLIENT_SETUP_FAILURE",
        "SECURITY_DAEMON_REGISTRATION_EXCEPTION",
        "AWS_REQUEST_LIMIT_EXCEEDED",
        "AWS_INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET_FAILURE",
        "AWS_UNSUPPORTED_FAILURE",
        "AZURE_QUOTA_EXCEEDED_EXCEPTION",
        "AZURE_OPERATION_NOT_ALLOWED_EXCEPTION",
        "NFS_MOUNT_FAILURE",
        "K8S_AUTOSCALING_FAILURE",
        "K8S_DBR_CLUSTER_LAUNCH_TIMEOUT",
        "SPARK_IMAGE_DOWNLOAD_FAILURE",
        "AZURE_VM_EXTENSION_FAILURE",
        "WORKSPACE_CANCELLED_ERROR",
        "AWS_MAX_SPOT_INSTANCE_COUNT_EXCEEDED_FAILURE",
        "TEMPORARILY_UNAVAILABLE",
        "WORKER_SETUP_FAILURE",
        "IP_EXHAUSTION_FAILURE",
        "GCP_QUOTA_EXCEEDED",
        "CLOUD_PROVIDER_RESOURCE_STOCKOUT" ,
        "GCP_SERVICE_ACCOUNT_DELETED",
        "AZURE_BYOK_KEY_PERMISSION_FAILURE",
        "SPOT_INSTANCE_TERMINATION",
        "AZURE_EPHEMERAL_DISK_FAILURE",
        "ABUSE_DETECTED",
        "IMAGE_PULL_PERMISSION_DENIED",
        "WORKSPACE_CONFIGURATION_ERROR",
        "SECRET_RESOLUTION_ERROR",
        "UNSUPPORTED_INSTANCE_TYPE",
        "CLOUD_PROVIDER_DISK_SETUP_FAILURE"
    ]
    type: Literal[ "SUCCESS", "CLIENT_ERROR", "SERVICE_FAULT", "CLOUD_FAILURE" ]
    parameters: Dict[str, str]

    

class DatabricksClusterInfoType(TypedDict):
    cluster_name: str
    spark_version: str
    spark_conf: Dict[str, str]
    azure_attributes: DatabricksClusterAzureAttributesType
    node_type_id: str
    driver_node_type_id: str
    ssh_public_keys: List[str]
    custom_tags: Dict[str, str]
    cluster_log_conf: DatabricksClusterSpecsClusterLogConfType
    init_scripts: List[DatabricksClusterSpecsInitScriptsType]
    spark_env_vars: Dict[str, str]
    autotermination_minutes: int
    enable_elastic_disk: bool
    cluster_source: Literal[ "UI", "JOB", "API", "SQL", "MODELS", "PIPELINE", "PIPELINE_MAINTENANCE" ]
    instance_pool_id: str
    policy_id: str
    enable_local_disk_encryption: bool
    driver_instance_pool_id: str
    workload_type: DatabricksClusterSpecsWorkloadType
    runtime_engine: Literal[ "NULL", "STANDARD", "PHOTON" ]
    docker_image: DatabricksClusterSpecsDockerImageType
    data_security_mode: Literal[ "NONE", "SINGLE_USER", "USER_ISOLATION", "LEGACY_TABLE_ACL", "LEGACY_PASSTHROUGH", "LEGACY_SINGLE_USER" ]
    single_user_name: str
    num_workers: int
    autoscale: DatabricksClusterSpecsAutoScaleType
    cluster_id: str
    creator_user_name: str
    driver: DatabricksClusterSpecsDriverType
    executors: List[DatabricksClusterSpecsExecutorsType]
    spark_context_id: int
    jdbc_port: int
    state: Literal[ "PENDING", "RUNNING", "RESTARTING", "RESIZING", "TERMINATING", "TERMINATED", "ERROR", "UNKNOWN" ]
    state_message: str
    start_time: int
    terminated_time: int
    last_state_loss_time: int
    last_restarted_time: int
    cluster_memory_mb: int
    cluster_cores: int
    default_tags: Dict[str, str]
    cluster_log_status: DatabricksClusterSpecsClusterLogStatusType
    termination_reason: DatabricksClusterSpecsTerminationReasonType
    

class DatabricksListClustersResponseType(TypedDict):
    clusters: List[DatabricksClusterInfoType]