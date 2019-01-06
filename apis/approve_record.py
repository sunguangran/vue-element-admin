# -*- coding: utf-8 -*-
# Author: sunguangran (sunguangran@daixiaomi.com)
from pandora.tools import render_view


@render_view(page='index.html', regex=r'^record/info')
def get_record_info(request):
    return {"a": 1}
