#!/usr/bin/env python3
import logging
import logging.config
import yaml

logging.config.dictConfig(yaml.load(open('logconfig.conf')))
logger = logging.getLogger("myLogger")

logger.info('Dit is een test');
logger.error('Dit is een tweede test');
logger.critical('Jaaa dat is wel een serieus probleem');
