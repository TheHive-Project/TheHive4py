#UserEndpoint

####create(self,user)

Create a new user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user```          |```InputUser```               |The data for the new user                      |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputUser```         |The created profile                            |      


####get(self, user_id)

Retrieve a user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```  |```str```                     |The ID of the user to get                      |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputUser```         |The retrieved user                             |


####get_current(self)

Get the current user.

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputUser```         |The current user                               | 


####delete(self, user_id, organisation)

Delete an existing user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user to delete              |required         |
|```organisation```  |```Optional[str]```           |The ID of the user to delete              |None             |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update(self, user_id, fields)

Update an existing user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user to update                   |required         |
|```fields```        |```InputUpdateUser```         |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####lock(self, user_id)

Lock the user with the given `user_id`.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user to be locked                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |


####unlock(self, user_id)

Unlocks the user with the given `user_id`.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user to be unlocked              |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |


####set_organisations(self, user_id, organisation)

Set an organisation for a user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user whose organisations will be set|required      |
|```organisations``` |```List[InputUserOrganisation]```|A list of `InputUserOrganisation` objects representing the organisations to be set                                                                             |None             |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputUserOrganisation]```|A list of `OutputUserOrganisation` objects representing the updated organisations|  


####set_password(self, user_id, password)

Set password for a user.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user whose password will be set|required      |
|```password```      |```str```                     |The new password to be set                     |None             |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               | 


####get_apikey(self, user_id)

Retrieve the API key for the user with the given `user_id`.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user whose API key will be retrieved|required      |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```str```                |The API key for the user                       | 

####remove_apikey(self, user_id)

Removes the API key for the user with the given `user_id`.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user whose API key will be removed|required      |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               | 


####renew_apikey(self, user_id)

Renews the API key for the user with the given `user_id`.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```user_id```       |```str```                     |The ID of the user whose API key will be renewed|required        |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```str```                |The new API key for the user                   | 


####find(self, filters, sortby, paginate)

Find users matching the given filters, sort expressions and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
|```sortby```        |```Optional[SortExpr]```      | The sorting criteria to apply to the search   |required         |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |required         |
        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputUser]```      |A list of the matching users                   | 


####count(self, filters)

Count users matching the given filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |

**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```int```                   |The number of matching users                   | 