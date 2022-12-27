import logging
import coloredlogs

import infaktApiClient

coloredlogs.install(level="INFO")
log = logging.getLogger("Main")

infakt = infaktApiClient.InfaktApiClient()

invoice = infakt.findInvoice(52055856)

log.info('OK')