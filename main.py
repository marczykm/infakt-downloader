import logging
import coloredlogs

from infaktApiClient import InfaktApiClient

coloredlogs.install(level="INFO")
log = logging.getLogger("Main")

infakt = InfaktApiClient()

invoices = infakt.listInvoices()

log.info('Invoices: %s', invoices)
log.info(len(invoices))

log.info('OK')