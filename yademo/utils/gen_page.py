
# -*- coding: utf-8 -*-

# @author: xuhe
# @date: 15/2/10
# @description: 


def gen_page(page_total, page_num, cur_page):
    if page_total <= page_num:
        return range(1, page_total+1)

    else:
        pre = (page_num-1)/2
        post = page_num - (pre+1)

        temp_list = []
        for i in range(pre, 0, -1):
            temp = cur_page - i
            if temp <= 0:
                temp = cur_page + page_num - i
            temp_list.append(temp)

        temp_list.append(cur_page)

        for j in range(post, 0, -1):
            temp = cur_page + j
            if temp > page_total:
                temp = cur_page - page_num + j
            temp_list.append(temp)
        temp_list.sort()
        return temp_list