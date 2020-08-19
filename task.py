# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 16:49
# @Author  : annie.hu
# @FileName: task.py
import threadpool


class Task:
    pools = 800     # 连接池

    @classmethod
    def run(cls, func, nums, threads=10, rows_per_thread=100):
        """
        根据需要的数据量创建测试数据
        :param func:            目标任务函数
        :param nums:            数据总量
        :param threads:         运行线程数
        :param rows_per_thread: 每个线程每次执行的任务量
        """
        start, stop = 0, 0  # 偏移量，停止点
        step = rows_per_thread  # 步长,每个线程每次执行的任务量
        pool = threadpool.ThreadPool(cls.pools)  # 创建线程池

        # 运行流程
        while True:
            tasks_list = []
            for thread_id in range(threads):
                stop = start + step
                threads_task = (None, {"start": start, "stop": stop, "thread_id": thread_id})
                tasks_list.append(threads_task)
                start += step
            tasks = threadpool.makeRequests(func, tasks_list)  # param_list传线程参数
            [pool.putRequest(req) for req in tasks]  # 将任务放到线程池中
            pool.wait()  # 运行task
            if stop >= nums:    # 结束条件
                break

