from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
import random

from db_table.models import AttemptsInfo


class MyPaginator(Paginator):   # 继承Paginator
    def __init__(self, object_list, per_page, show_count=2, orphans=0, allow_empty_first_page=True):  # show_count代表要展示的当前页之前或之后的页码数，默认展示3页
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)  # 继承父类的属性和方法
        self.show_count = show_count
        self.has_previous_more = True  # 定义show_count之前是否还有更多页码
        self.has_next_more = True   # 定义show_count之后是否还有更多页码
    #  覆写page方法

    def page(self, number):
        self.number = int(number)
        #  判断当前页之前是否还有show_count显示的页码数
        if self.number <= self.show_count + 2:
            self.has_previous_more = False
            self.previous_range = range(1, self.number)
        else:
            self.previous_range = range(self.number - self.show_count, self.number)
        #  判断当前页之后是否还有show_count显示的页码数
        if self.number >= self.num_pages - self.show_count - 1:
            self.has_next_more = False
            self.next_range = range(self.number + 1, self.num_pages + 1)
        else:
            self.next_range = range(self.number + 1, self.number + self.show_count + 1)
        return super().page(number)

def attempts(request):
    return attempts_page(request, 1)

def attempts_page(request, page_index):
    attempt_list = AttemptsInfo.objects.filter(User = request.user)
    paginator = MyPaginator(attempt_list, 10)
    int(page_index)
    page = paginator.page(page_index)
    context = {"page": page}
    return render(request, "attempts/attempts.html", context)