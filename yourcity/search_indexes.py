from councilmatic_core.haystack_indexes import BillIndex as BaseBillIndex
from haystack import indexes


class BillIndex(BaseBillIndex, indexes.Indexable):

    #
    # Haystack is a rich and extensively configurable search app for Django.
    # Modify this class to change the behavior of searching in your local
    # Councilmatic instance.
    #
    # Haystack's SearchIndex API
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~
    # http://django-haystack.readthedocs.org/en/v2.4.1/searchindex_api.html
    #

    pass