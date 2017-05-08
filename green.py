import datetime
import os

# from heavy import special_commit


def modify():
	#第一个参数改为zero.md所在的路径
    file = open('D:/work/git/smuwjs/brush-contribution-green/zero.md', 'r') 
    flag = int(file.readline()) == 0
    file.close()
	#第一个参数改为zero.md所在的路径
    file = open('D:/work/git/smuwjs/brush-contribution-green/zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m "test"')


def set_sys_time(year, month, day):
    os.system('date %04d/%02d/%02d' % (year, month, day))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2016, 5, 8), datetime.date(2017, 5, 8))
	#第一个参数为开始日期（小绿点表格左上），第二个结束日期（小绿点表格右下）