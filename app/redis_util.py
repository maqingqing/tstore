import redis

# Redis Key
# hash object
OVERALL_CAPACITY = 'capacity'
VOLUME_STATUS = 'status'
VOLUME_USAGE = 'usage'
VOLUME_PREFIX = 'volume:'
SNAPSHOT_PREFIX = 'snapshot:'
BRICK_PREFIX = 'brick:'
VOLUME_NFS = 'nfs'
VOLUME_SAMBA = 'samba'
VOLUME_ISCSI = 'iscsi' 
VOLUME_SWIFT = 'swift'

# set object
VOLUME_NAMES = 'volume:names'
NETWORKIO_IN = 'network_io_in:names'
NETWORKIO_OUT = 'network_io_out:names'


# single object
CLUSTER_DISKS = 'cluster:disks'
CLUSTER_LIST = 'cluster:list'
CLUSTER_RESOURCE = 'cluster:resource'

CLUSTER_DEVICE = 'cluster:devices'
# list object
MEMORY_USAGE_PREFIX = 'memory_usage:'  # memory_usage:192.168.1.150
CPU_USAGE_PREFIX = 'cpu_usage:'  # cpu_usage:192.168.1.150:1 cpu_usage:192.168.1.150:2 etc
READ_SPEED_PREFIX = 'read_speed:'
WRITE_SPEED_PREFIX = 'write_speed:'
DISKWRITE = 'diskio_write:'
DISKREAD = 'diskio_read:'
DISKWRITEALL = 'disk_writes:'
DISKREADALL = 'disk_reads:'
DISK_NAME_WRITE = 'disk_name_write:'
DISK_NAME_READ = 'diskname_read:'
NETWORKIO_NAME_IN_INIT = 'network_machine_in_init:'
NETWORKIO_NAME_OUT_INIT = 'network_machine_out_init:'
NETWORKIO_IN_SUM_INIT = 'networkio_in_sum_init:'
NETWORKIO_OUT_SUM_INIT = 'networkio_out_sum_init:'

TIMESTAMP = 'timestamp:'

# Redis Value
VOLUME_STATUS_STARTED = 'Started'
VOLUME_STATUS_STOPPED = 'Stopped'
VOLUME_CAPACITY = 'capacity'
VOLUME_USAGE = 'usage'
TIME = "time"
DATA = "data"

# redis mq
VOLUME_OPERATE = 'tstore_operate_v2'
VOLUME_OPERATE_CREATE_VALUE = 'create'
VOLUME_OPERATE_DELETE_VALUE = 'remove'
VOLUME_OPERATE_START_VALUE = 'start'
VOLUME_OPERATE_STOP_VALUE = 'stop'
VOLUME_OPERATE_RESTART_VALUE = 'restart'
TSTORE_CREATE_VOLUME = 'tstore_createVolume_v2'
TSTORE_DELETE_VOLUME = 'tstore_deleteVolume_v2'
TSTORE_START_VOLUME = 'tstore_startVolume_v2'
TSTORE_STOP_VOLUME = 'tstore_stopVolume_v2'
TSTORE_RESTART_VOLUME = 'tstore_restartVolume_v2'
TSTORE_MQ_TAG = 'tstor_mq_tag'
TSTORE_MQ_TAG_CREATE = "volume_create"
TSTORE_MQ_TAG_DELETE = 'volume_delete'
TAG_CREATE_CALLBACK = 'create_callback'
TAG_DELETE_CALLBACK = 'volume_delete_callback'
CREATE_CALLBACK_VOLUMENAME = 'callback_name'
CREATE_CALLBACK_USERNAME = 'callback_user'
TSTORE_VOLUME_NAME = 'volume_name'
SUCCESS = 'success'
OUT = 'out'
TSTORE_CREATE_RESULT = 'tstore_create_result_v2'
TSTORE_DELETE_RESULT = 'tstore_delete_result_v2'
TSTORE_START_RESULT = 'tstore_start_result_v2'
TSTORE_STOP_RESULT = 'tstore_stop_result_v2'
TSTORE_RESTART_RESULT = 'tstore_restart_result_v2'
CLUSTERLIST = 'cluster_list'
MAX_DICT_IDX = 'max_dict_idx'
VOLUME_START1 = 'volume_start1'
VOLUME_START2 = 'volume_start2'
VOLUME_START3 = 'volume_start3'
VOLUME_STOP1 = 'volume_stop1'
VOLUME_STOP2 = 'volume_stop2'
ENABLE_VOLUME_QUOTA = 'enable_volume_quota'
SET_VOLUME_QUOTA = 'set_volume_quota'
HMSET = 'hmset'
REFRESH_CREATE_VOLUME = 'refresh_createvolume_status'
REDIS_REM = 'redis_rem'
REDIS_DELBRICK = 'redis_delbrick'
REDIS_DELVOL = 'redis_delvol'
VOLUMESAMBA = 'volume_samba'

# queery status
CREATE_STATUS = 'create_status'
RESTART_STATUS = 'restart_status'
LOCK_PASS = 'pass'
LOCK_PASS_VALUE = 'volume_pass'
CREATE_STATUS_STEP1 = 'create1'
CREATE_STATUS_STEP2 = 'create2'
CREATE_STATUS_STEP3 = 'create3'
READY = 'ready'
REDIS_USERNAME = 'user_name'

# ajax
NAME = 'name'
CAPACITY = 'capacity'
REDUNDANCY_RATIO = 'redundancy_ratio'
USERNAME = 'username'


# This class is wrapper for a redis instance
class Redis:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    @staticmethod
    def set(name, value):
        Redis.r.set(name, value)

    @staticmethod
    def psetex(name, time, value):
        Redis.r.psetex(name, time, value)

    @staticmethod
    def setex(name, time, value):
        Redis.r.setex(name, time, value)

    @staticmethod
    def pttl(name):
        Redis.r.pttl(name)

    @staticmethod
    def ttl(name):
        Redis.r.ttl(name)

    @staticmethod
    def get(name):
        return Redis.r.get(name)

    @staticmethod
    def delete(name):
        Redis.r.delete(name)

    @staticmethod
    def hset(name, key, value):
        Redis.r.hset(name, key, value)

    @staticmethod
    def hmset(name, mapping):
        Redis.r.hmset(name, mapping)

    @staticmethod
    def hget(name, key):
        return Redis.r.hget(name, key)

    @staticmethod
    def hgetall(name):
        return Redis.r.hgetall(name)

    @staticmethod
    def sadd(name, value):
        Redis.r.sadd(name, value)

    @staticmethod
    def sget(name):
        return Redis.r.smembers(name)

    @staticmethod
    def srem(name, key):
        return Redis.r.srem(name, key)

    @staticmethod
    def lrem(name, value,num):
        Redis.r.lrem(name, value,num)

    # append to list
    @staticmethod
    def rpush(name, key):
        Redis.r.rpush(name, key)

    @staticmethod
    def lrange(name, start, end):
        return Redis.r.lrange(name, start, end)

    @staticmethod
    def lpop(name):
        return Redis.r.lpop(name)

    @staticmethod
    def blpop(name, timeout):
        return Redis.r.blpop(name, timeout)