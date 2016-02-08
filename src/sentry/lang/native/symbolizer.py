from symsynd.driver import Driver
from symsynd.report import ReportSymbolizer

from sentry.lang.native.dsymcache import dsymcache


driver = Driver()


def make_symbolizer(project, binary_images):
    dsym_path, loaded = dsymcache.fetch_dsyms(
        [x['uuid'] for x in binary_images])
    return ReportSymbolizer(driver, dsym_path, binary_images)