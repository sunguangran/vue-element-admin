# -*- coding: utf-8 -*-
# Author: sunguangran (sunguangran@daixiaomi.com)
from pynavi.view.request.url_refactor import url


@url(r'^record/info')
def get_record_info(request):
    return {"a": 1}
