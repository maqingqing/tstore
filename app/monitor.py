#!/usr/bin/python
import threading
from command import *
from redis_util import *
from log import *


class Monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # localExecutor = LocalExecutor()

    def run(self):
        count = 0
        while True:
            # try:
                while True:
                    time.sleep(3)
                    whichOperate = Redis.lpop(VOLUME_OPERATE)
                    if whichOperate:
                        if whichOperate == VOLUME_OPERATE_CREATE_VALUE:
                            logging.info("2")
                            logging.info(whichOperate)
                            i = 0
                            while i < 6:
                                message = Redis.blpop(TSTORE_CREATE_VOLUME, 20)
                                if message:
                                    dict_message = eval(message[1])
                                    logging.info("3")
                                    logging.info(dict_message)
                                    if dict_message[TSTORE_MQ_TAG] == TSTORE_MQ_TAG_CREATE:
                                        # create volume
                                        Redis.set(CREATE_STATUS, CREATE_STATUS_STEP1)
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        success1, out1, actual_capacity = volume_create(dict_message[CLUSTERLIST],
                                                                                        dict_message[MAX_DICT_IDX],
                                                                                        dict_message[TSTORE_VOLUME_NAME],
                                                                                        dict_message[CAPACITY],
                                                                                        dict_message[REDUNDANCY_RATIO])
                                        logging.info("moni1")
                                        logging.info(success1)
                                        logging.info(out1)
                                        if not success1:
                                            Redis.delete(TSTORE_CREATE_VOLUME)
                                            create_result1 = {TSTORE_MQ_TAG: TAG_CREATE_CALLBACK, SUCCESS: success1,
                                                              OUT: out1, CREATE_CALLBACK_VOLUMENAME:
                                                                  dict_message[TSTORE_VOLUME_NAME],
                                                              CREATE_CALLBACK_USERNAME: dict_message[USERNAME]}
                                            Redis.rpush(TSTORE_CREATE_RESULT, create_result1)
                                            break
                                    if dict_message[TSTORE_MQ_TAG] == VOLUME_START1:
                                        # volume start
                                        Redis.set(CREATE_STATUS, CREATE_STATUS_STEP2)
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        volume_start(dict_message[TSTORE_VOLUME_NAME])
                                    if dict_message[TSTORE_MQ_TAG] == ENABLE_VOLUME_QUOTA:
                                        # enable volume quota
                                        Redis.set(CREATE_STATUS, CREATE_STATUS_STEP3)
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        enable_volume_quota(dict_message[TSTORE_VOLUME_NAME])
                                    if dict_message[TSTORE_MQ_TAG] == SET_VOLUME_QUOTA:
                                        # set volume quota
                                        Redis.set(CREATE_STATUS, CREATE_STATUS_STEP3)
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        success2, out2 = set_volume_quota(dict_message[TSTORE_VOLUME_NAME],
                                                                          actual_capacity)
                                        if not success2:
                                            logging.info("moni2")
                                            logging.info(success2)
                                            Redis.delete(TSTORE_CREATE_VOLUME)
                                            create_result1 = {TSTORE_MQ_TAG: TAG_CREATE_CALLBACK, SUCCESS: success2,
                                                              OUT: out2,
                                                              CREATE_CALLBACK_VOLUMENAME:
                                                                  dict_message[TSTORE_VOLUME_NAME],
                                                              CREATE_CALLBACK_USERNAME: dict_message[USERNAME]}
                                            Redis.rpush(TSTORE_CREATE_RESULT, create_result1)
                                            break
                                    if dict_message[TSTORE_MQ_TAG] == HMSET:
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        Redis.hmset(VOLUME_PREFIX + dict_message[TSTORE_VOLUME_NAME],
                                                    {VOLUME_CAPACITY: actual_capacity, VOLUME_USAGE: 0,
                                                     VOLUME_NFS: 'on',
                                                     VOLUME_SAMBA: 'off',
                                                     VOLUME_ISCSI: 'off', VOLUME_SWIFT: 'off'})
                                    if dict_message[TSTORE_MQ_TAG] == REFRESH_CREATE_VOLUME:
                                        # refresh create_volume status
                                        Redis.set(CREATE_STATUS, CREATE_STATUS_STEP3)
                                        Redis.set(REDIS_USERNAME, dict_message[USERNAME])
                                        refresh_createvolume_status(dict_message[TSTORE_VOLUME_NAME])
                                        create_result2 = {TSTORE_MQ_TAG: TAG_CREATE_CALLBACK, SUCCESS: success1, OUT: out1,
                                                          CREATE_CALLBACK_VOLUMENAME: dict_message[TSTORE_VOLUME_NAME],
                                                          CREATE_CALLBACK_USERNAME: dict_message[USERNAME]}
                                        Redis.rpush(TSTORE_CREATE_RESULT, create_result2)
                                    i += 1
                                else:
                                    logging.info("no message")
                                    break
                        elif whichOperate == VOLUME_OPERATE_DELETE_VALUE:
                            logging.info(whichOperate)
                            i = 0
                            while i < 5:
                                message = Redis.blpop(TSTORE_DELETE_VOLUME, 20)
                                if message:
                                    dict_message = eval(message[1])
                                    if dict_message[TSTORE_MQ_TAG] == TSTORE_MQ_TAG_DELETE:
                                        success, out = volume_delete(dict_message[TSTORE_VOLUME_NAME])
                                        if not success:
                                            Redis.delete(TSTORE_DELETE_VOLUME)
                                            volume_delete_result = {TSTORE_MQ_TAG: TAG_DELETE_CALLBACK,
                                                                    SUCCESS: success, OUT: out}
                                            Redis.rpush(TSTORE_DELETE_RESULT, volume_delete_result)
                                            break
                                    if dict_message[TSTORE_MQ_TAG] == REDIS_REM:
                                        Redis.srem(VOLUME_NAMES, dict_message[TSTORE_VOLUME_NAME])
                                        logging.info("srem")
                                    if dict_message[TSTORE_MQ_TAG] == REDIS_DELBRICK:
                                        Redis.delete(BRICK_PREFIX + dict_message[TSTORE_VOLUME_NAME])
                                        logging.info("srem2")
                                    if dict_message[TSTORE_MQ_TAG] == REDIS_DELVOL:
                                        Redis.delete(VOLUME_PREFIX + dict_message[TSTORE_VOLUME_NAME])
                                        logging.info("srem3")
                                    if dict_message[TSTORE_MQ_TAG] == VOLUMESAMBA:
                                        volume_samba(dict_message[TSTORE_VOLUME_NAME], enable=False)
                                        logging.info("srem4")
                                        volume_delete_result = {TSTORE_MQ_TAG: TAG_DELETE_CALLBACK,
                                                                SUCCESS: success, OUT: out}
                                        Redis.rpush(TSTORE_DELETE_RESULT, volume_delete_result)
                                    i += 1
                                else:
                                    logging.info("no message")
                                    break
                        elif whichOperate == VOLUME_OPERATE_START_VALUE:
                            logging.info(whichOperate)
                            message = Redis.blpop(TSTORE_START_VOLUME, 20)
                            if message:
                                dict_message = eval(message[1])
                                if dict_message[TSTORE_MQ_TAG] == VOLUME_START2:
                                    success, out = volume_start(dict_message[TSTORE_VOLUME_NAME])
                                    volume_start2_result = {TSTORE_MQ_TAG: "volume_start2_result", SUCCESS: success,
                                                            OUT: out}
                                    Redis.rpush(TSTORE_START_RESULT, volume_start2_result)
                            else:
                                logging.info("no message")
                                break
                        elif whichOperate == VOLUME_OPERATE_STOP_VALUE:
                            logging.info(whichOperate)
                            message = Redis.blpop(TSTORE_STOP_VOLUME, 20)
                            if message:
                                dict_message = eval(message[1])
                                logging.info(dict_message)
                                if dict_message[TSTORE_MQ_TAG] == VOLUME_STOP1:
                                    logging.info(dict_message[TSTORE_MQ_TAG])
                                    success, out = volume_stop(dict_message[TSTORE_VOLUME_NAME])
                                    volume_stop1_result = {TSTORE_MQ_TAG: "volume_stop1_result", SUCCESS: success,
                                                           OUT: out}
                                    Redis.rpush(TSTORE_STOP_RESULT, volume_stop1_result)
                            else:
                                logging.info("no message")
                                break
                        elif whichOperate == VOLUME_OPERATE_RESTART_VALUE:
                            logging.info(whichOperate)
                            i = 0
                            while i < 2:
                                message = Redis.blpop(TSTORE_RESTART_VOLUME, 20)
                                if message:
                                    dict_message = eval(message[1])
                                    logging.info(dict_message)
                                    if dict_message[TSTORE_MQ_TAG] == VOLUME_STOP2:
                                        Redis.set(RESTART_STATUS, "stop")
                                        stop_success, stop_out = volume_stop(dict_message[TSTORE_VOLUME_NAME])
                                        logging.info("restart stop")
                                        logging.info(stop_success)
                                        if not stop_success:
                                            Redis.delete(TSTORE_RESTART_VOLUME)
                                            volume_stop2_result = {TSTORE_MQ_TAG: "volume_restart_result",
                                                                   SUCCESS: stop_success, OUT: stop_out}
                                            Redis.rpush(TSTORE_RESTART_RESULT, volume_stop2_result)
                                    if dict_message[TSTORE_MQ_TAG] == VOLUME_START3:
                                        Redis.set(RESTART_STATUS, "start")
                                        start_success, start_out = volume_start(dict_message[TSTORE_VOLUME_NAME])
                                        volume_start3_result = {TSTORE_MQ_TAG: "volume_start3_result",
                                                                SUCCESS: start_success,
                                                                OUT: start_out}
                                        Redis.rpush(TSTORE_RESTART_RESULT, volume_start3_result)
                                    i += 1
                                else:
                                    logging.info("no message")
                                    break
                    else:
                        logging.info("no operate")
                        Redis.delete(VOLUME_OPERATE)
                        Redis.delete(TSTORE_CREATE_VOLUME)
                        Redis.delete(TSTORE_DELETE_VOLUME)
                        Redis.delete(TSTORE_START_VOLUME)
                        Redis.delete(TSTORE_STOP_VOLUME)
                        Redis.delete(TSTORE_RESTART_VOLUME)
                        Redis.delete(TSTORE_CREATE_RESULT)
                        Redis.delete(REDIS_USERNAME)
                        Redis.delete(CREATE_STATUS)
                        Redis.delete(TSTORE_DELETE_RESULT)
                        Redis.delete(TSTORE_START_RESULT)
                        Redis.delete(TSTORE_STOP_RESULT)
                        Redis.delete(TSTORE_STOP_RESULT)
                        Redis.delete(LOCK_PASS)
                        break

                res = refresh_pool_list()
                determine = Redis.get("Refresh")
                if not determine:
                    logging.info("helloh")
                    refresh_machine_resource()
                    refresh_volume_status()
                else:
                    logging.info(determine)

                # query_volume_perf()
                refresh_disk_io()
                refresh_network_io()
                time.sleep(5)
                count += 1
                if count == 12:
                    # refresh_volume_data()
                    count = 0
            # except Exception, e:
            #     logging.warning(e)
            #     break


if __name__ == '__main__':
    Monitor.run()
