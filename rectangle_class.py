class rectangle():
    def __init__(self,le,we):
        self.le=le
        self.we=we
    def pr_ans(b):
        length=b.le
        width=b.we
        ans=(length*width)
        print("area of the rectangle",ans)
c=rectangle(int(input("Enter the length")),int(input("Enter the width")))
c.pr_ans()
