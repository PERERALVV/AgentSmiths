from typing import List
class Environment:

    employees: List[object]

    def hire(self, employees: List[type]):
        self.employees = [employee() for employee in employees]
        return self
        
    async def start(self):
        # should be implemented by the child class
        raise NotImplementedError
        