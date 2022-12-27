import logging
import coloredlogs

from infaktApiClient import InfaktApiClient

coloredlogs.install(level="INFO")
log = logging.getLogger("Main")

infakt = InfaktApiClient()

invoices = infakt.listInvoices()

# log.info('Invoices: %s', invoices)
# log.info(len(invoices))
# log.info(invoices[0])
# invoice = infakt.findInvoice(invoices[0].id)
# log.info(invoice)
for invoice in invoices:
    infakt.generatePdf(invoice.id, "invoices")

log.info('OK')