import sys
import os

import globals
import logging
import grpc

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Client(object):
  def client_greet(node_ip):
    logger.info("connecting to port".format(node_ip + ":" + str(globals.port))
    channel = gprc.insecure_channel(node_ip + ":" + str(globals.port))
