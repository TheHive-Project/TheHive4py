#TaskLogEndpoint

####create(self, task_id, task_log)

Create a new task log for a given task.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_id```       |```str```                     |The task to create the task log for            |required         |
|```task_log```      |```InputTaskLog```            |The task log to create                         |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTaskLog```      |The created task log                           |      


####get(self, task_log_id)

Retrieves an existing task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_log_id```   |```str```                     |The ID of the task log to retrieve             |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTaskLog```      |The retrieved task log                         |   
 

####delete(self, task_log_id)

Deletes an existing task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_log_id```   |```str```                     |The ID of the task log to delete               |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update(self, task_log_id, fields)

Update an existing task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_log_id```   |```str```                     |The ID of the task log to update               |required         |
|```fields```        |```InputUpdateTaskLog```      |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####add_attachments(self, task_log_id, attachment_paths)

Add one or more attachments to a task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_log_id```   |```str```                     |The ID of the task log to add the attachments to |required         |
|```attachment_paths``` |```List[str]```            |A list of file paths for the attachments to add  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####delete_attachment(self, task_log_id, attachment_id)

Delete an attachment from a task log.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```task_log_id```   |```str```                     |The task log's id                              |required         |
|```attachment_id``` |```str```                     |The attachment's id                            |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  






