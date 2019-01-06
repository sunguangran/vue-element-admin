# -*- coding: utf-8 -*-
# Author: sunguangran (sunguangran@daixiaomi.com)
import json

from django.http import HttpResponse
from pynavi.view.request.url_refactor import url


@url(r'^record/info')
def get_record_info(request):
    # return {"a": 1}
    return HttpResponse(json.dumps({"a": 1}), content_type="application/json")
