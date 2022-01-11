import os
import platform


HOME = os.environ['HOME'] if platform.system() == 'Linux' else os.environ['USERPROFILE']

CFG_DIR = f'{HOME}/.dst_run'
CFG_PATH = f'{CFG_DIR}/cfg.yaml'
LOG_PATH = f'{CFG_DIR}/dst_run.log'
CUSTOM_TEMPLATE_DIR = f'{CFG_DIR}/cluster_template'
GAME_LOG_DIR = f'{CFG_DIR}/log'
GAME_LOG_PATH = f'{GAME_LOG_DIR}/log.txt'
GAME_LOG_BACKUP_DIR = f'{GAME_LOG_DIR}/backup'

PROGRAM_DIR = f'{HOME}/dst_run'
TEMPLATE_DIR = f'{PROGRAM_DIR}/cluster_template'

STEAMCMD_DIR = f'{HOME}/steamcmd'
DST_DIR = f'{HOME}/dst'
MOD_SETUP_PATH = f'{HOME}/dst/mods/dedicated_server_mods_setup.lua'

CLUSTERS_DIR = f'{HOME}/.klei/DoNotStarveTogether'
CLUSTERS_BACKUP_DIR = f'{CLUSTERS_DIR}/backup'
CLUSTER_NAME = 'Cluster'
ROOM_SETTING_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/cluster.ini'
ADMIN_LIST_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/adminlist.txt'
CLUSTER_TOKEN_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/cluster_token.txt'
MASTER_WORLD_SETTING_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/Master/leveldataoverride.lua'
MASTER_MOD_SETTING_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/Master/modoverrides.lua'
CAVES_WORLD_SETTING_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/Caves/leveldataoverride.lua'
CAVES_MOD_SETTING_PATH = f'{CLUSTERS_DIR}/{CLUSTER_NAME}/Caves/modoverrides.lua'
