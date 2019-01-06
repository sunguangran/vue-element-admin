# -*- coding: utf-8 -*-
# Author: sunguangran (sunguangran@daixiaomi.com)
from pynavi.view.request.url_refactor import url_patterns_maker

pandora_patterns = url_patterns_maker(module=__name__, manager='^pandora1/manager/', default='^pandora1/')
