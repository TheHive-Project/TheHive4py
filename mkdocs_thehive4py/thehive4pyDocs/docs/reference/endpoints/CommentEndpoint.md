#CommentEndpoint

Class representing TheHive's comment endpoint.


####create_in_alert(self, alert_id, comment)

Creates a comment in the specified alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert                            |required         |
|```comment```       |```InputComment```            |An object containing the comment data          |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputComment```      |An object containing the created comment data  |      



####create_in_case(self, case_id, comment)

Creates a comment in the specified alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case                             |required         |
|```comment```       |```InputComment```            |An object containing the comment data          |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputComment```      |An object containing the created comment data  |      


####get(self, comment_id)

Gets the comment data for the specified comment.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```comment_id```    |```str```                     |The ID of the commment                         |required         |

           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputComment```      |An object containing the created comment data  |   



####delete(self, comment_id)

Deletes the specified comment.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```comment_id```    |```str```                     |The ID of the comment to delete                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  



####update(self, comment_id, fields)

Delete an existing case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```comment_id```    |```CaseId```                  |The ID of the case to delete The ID of the comment to update                                                                                              |required         |
|```fields```        |```InputUpdateComment```      | An object containing the updated comment data |required         |
      
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  
