from pydantic import BaseModel 

class update_task_scheme(BaseModel):
    name: str=None
    des: str=None
    priority:int=None

task=update_task_scheme(name="123", des="asdfasd")
cols=[]
for col in task:
    cols.append(col[0])

cols='('+','.join(cols)+')'
print(cols)