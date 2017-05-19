"""
53.73%

看答案的
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]

pmap = collections.defaultdict(list)
for c, p in zip(pid, ppid): pmap[p].append(c)
这两句得到的是
defaultdict(<type 'list'>, {0: [3], 3: [1, 5], 5: [10]})
对于处理树结构很有用


for i in result:
    result.extend(pmap.get(i, []))
这一句也很有意思
list在extend一个list的时候，会继续遍历下去
"""

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if kill not in pid and kill not in ppid:
            return None

        pmap = collections.defaultdict(list)
        for c, p in zip(pid, ppid): pmap[p].append(c)
        result = [kill]
        for i in result:
            result.extend(pmap.get(i, []))
        return result

            
