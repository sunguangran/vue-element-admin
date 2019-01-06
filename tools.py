# -*- coding: utf-8 -*-
# Author: sunguangran (sunguangran@daixiaomi.com)
from __future__ import print_function

import functools

from django.shortcuts import render
from pynavi.view.request.url_refactor import url


def render_view(page, regex=None):
    if regex is None:
        regex = page

    def func_wrapper(func):
        @url(regex)
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            return render(request, page, func(request, *args, **kwargs))

        return wrapper

    return func_wrapper
