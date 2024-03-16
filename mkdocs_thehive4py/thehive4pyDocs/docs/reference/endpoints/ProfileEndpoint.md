#ProfileEndpoint


####create(self, profile)

Create a new profile.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```profile```       |```InputProfile```            |The data for the new profile                   |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputProfile```      |The created profile                            |      


####get(self, profile_id)

Get an existing profile.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```profile_id```    |```str```                     |The ID of the profile to get                   |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputProfile```      |The retrieved profile                          |   
 


####delete(self, profile_id)

Delete an existing profile.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```profile_id```    |```str```                     |The ID of the profile to delete                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update(self, profile_id, fields)

Update an existing profile.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```profile_id```    |```str```                     |The ID of the profile to update                |required         |
|```fields```        |```InputUpdateProfile```      |The fields to update                           |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####find(self, filters, sortby, paginate)

Finds profiles based on filters, sort experssions and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
|```sortby```        |```Optional[SortExpr]```      | The sorting criteria to apply to the search   |required         |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |required         |
        
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputProfile]```   |A list of the matching profiles                | 


####count(self, filters)

Count profiles matching the given filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```int```                   |The number of matching profiles                | 


