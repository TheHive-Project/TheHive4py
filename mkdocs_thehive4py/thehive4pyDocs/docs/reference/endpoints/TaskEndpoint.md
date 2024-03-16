#TaskEndpoint

####create(self, case_id, task)

Creates a new task in a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The case to create the task within             |required         |
|```task```          |```InputTask```               |The task to create                             |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTask```         |The created task                               |      


####get(self, task_id)

Retrieves an existing task .

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```        |```str```                     |The ID of the task to retrieve                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTask```         |The retrieved task                          |   
 

####delete(self, task_id)

Deletes an existing task.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to delete                   |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update(self, task_id, fields)

Update an existing task.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to update                   |required         |
|```fields```        |```InputUpdateTask```         |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####bulk_update(self, fields)

Updates multiple tasks.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```fields```        |```InputBulkUpdateTask```     |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####get_required_actions(self, task_id)

Retrieves the required actions for a specific task.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to retrieve required actions for |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```dict```               |A dictionary containing information about the required actions for the task|  


####set_as_required(self, task_id, org_id)

Set an organization as required to take action for a specific task..

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to set the organization as required for|required |
|```org_id```        |```str```                     |The ID of the organisation to set as required for the task.|required |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####set_as_done(self, task_id, org_id)

Set an organization as required to take action for a specific task..

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to set the organization as done for|required  |
|```org_id```        |```str```                     |The ID of the organization to mark the action as done for|required|
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####find(self, filters, sortby, paginate)

Find tasks based on the specified filters, sort order, and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputTask]```      |A list of matching tasks                       |


####count(self, filters)

Count the number of tasks that match the specified filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```int```                   |The number of matching tasks                   | 


####create_log(self, task_id, task_log)

Creates a new task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The task to create the task log for            |required         |
|```task_log```      |```InputTaskLog```            |The task log to create                         |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTaskLog```      |The created task log                           |  


####find_logs(self, task_id, filters, sortby, paginate)

Find task logs based on the specified filters, sort order, and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The ID of the task to retrieve the logs for    |required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputTaskLog]```   |A list of matching task logs                   |
