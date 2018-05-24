import shutil
from metashare import settings
import logging
import os

# Setup logging support.
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(settings.LOG_HANDLER)


def remove_resource(storage_object, keep_stats=False):
    """
    Completely removes the given storage object and its associated language 
    resource from the storage layer.
    Also includes deletion of statistics and recommendations; use keep_stats
    optional parameter to suppress deletion of statistics and recommendations.
    """
    try:
        resource = storage_object.resourceinfotype_model
    except:
        # pylint: disable-msg=E1101
        LOGGER.error('PROBLEMATIC: %s - count: %s', storage_object.identifier,
                     str(1), exc_info=True)
        raise

    folder = os.path.join(settings.STORAGE_PATH, storage_object.identifier)
    shutil.rmtree(folder)
    resource.delete_deep(keep_stats=keep_stats)
    storage_object.delete()
